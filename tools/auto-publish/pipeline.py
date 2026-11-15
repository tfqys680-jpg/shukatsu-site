#!/usr/bin/env python3
"""ChatGPT（執筆）× Claude（審査・推敲）の自動記事パイプライン。

1. docs/seo/auto-queue.csv から次のテーマを選ぶ（空なら両AIでテーマを補充）
2. ChatGPT が記事原稿をJSONで作成
3. 出典URLを実際に取得し、本文を Claude に渡して照合・推敲（最大 max_review_rounds 回）
4. 機械検証（禁止表現・構成・出典数・内部リンク）
5. column/<slug>/index.html を生成し、トップ・sitemap・SEO台帳・実行ログを更新
6. 結果を --result のJSONに書く（GitHub Actions がPR作成・自動マージを判断）

外部ライブラリ不要（Python標準ライブラリのみ）。
環境変数: OPENAI_API_KEY, OPENAI_MODEL, ANTHROPIC_API_KEY, ANTHROPIC_MODEL
テスト用: AUTO_PUBLISH_MOCK=<フィクスチャのディレクトリ> でAPIと出典取得を差し替える。
"""
import argparse
import csv
import datetime as dt
import html
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prompts  # noqa: E402

ROOT = Path(os.environ.get("AUTO_PUBLISH_ROOT", Path(__file__).resolve().parents[2]))
JST = dt.timezone(dt.timedelta(hours=9))
MOCK = os.environ.get("AUTO_PUBLISH_MOCK")
_mock_calls = {"openai": 0, "claude": 0}


class PipelineError(Exception):
    pass


# ---------------------------------------------------------------- utilities

def today() -> dt.date:
    forced = os.environ.get("AUTO_PUBLISH_DATE")
    return dt.date.fromisoformat(forced) if forced else dt.datetime.now(JST).date()


def jp_date(d: dt.date) -> str:
    return f"{d.year}年{d.month}月{d.day}日"


def read_csv(rel):
    with open(ROOT / rel, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]


def write_csv(rel, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    (ROOT / rel).write_text(buf.getvalue(), encoding="utf-8")


def append_csv_row(rel, row):
    text = (ROOT / rel).read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    buf = io.StringIO()
    csv.writer(buf, lineterminator="\n").writerow(row)
    (ROOT / rel).write_text(text + buf.getvalue(), encoding="utf-8")


def parse_json(text):
    text = text.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if m:
        text = m.group(1)
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < 0:
        raise PipelineError("AIの応答にJSONが見つかりません")
    return json.loads(text[start:end + 1])


def http_post(url, headers, payload, timeout=600):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise PipelineError(f"API error {e.code}: {e.read().decode()[:500]}") from e


def require_env(name):
    v = os.environ.get(name, "").strip()
    if not v:
        raise PipelineError(f"環境変数 {name} が未設定です（GitHubのSecrets/Variablesを確認）")
    return v


def mock_response(kind):
    _mock_calls[kind] += 1
    path = Path(MOCK) / f"{kind}_{_mock_calls[kind]}.json"
    if not path.exists():
        raise PipelineError(f"mock fixture missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def ask_openai(system, user):
    if MOCK:
        return mock_response("openai")
    data = http_post(
        "https://api.openai.com/v1/chat/completions",
        {"Authorization": f"Bearer {require_env('OPENAI_API_KEY')}", "Content-Type": "application/json"},
        {
            "model": require_env("OPENAI_MODEL"),
            "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        },
    )
    return parse_json(data["choices"][0]["message"]["content"])


def ask_claude(system, user):
    if MOCK:
        return mock_response("claude")
    data = http_post(
        "https://api.anthropic.com/v1/messages",
        {
            "x-api-key": require_env("ANTHROPIC_API_KEY"),
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        {
            "model": require_env("ANTHROPIC_MODEL"),
            "max_tokens": 32000,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    return parse_json(text)


def html_to_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def fetch_source(url):
    """出典URLを取得し (ok, 本文抜粋) を返す。"""
    if MOCK:
        table = json.loads((Path(MOCK) / "sources.json").read_text(encoding="utf-8"))
        return (url in table, table.get(url, "取得失敗（mock）"))
    if not url.startswith("https://"):
        return False, "https以外のURL"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (shukatsu-guide auto-publish source check)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status != 200:
                return False, f"HTTP {r.status}"
            ctype = r.headers.get("Content-Type", "")
            body = r.read(1_500_000)
            if "pdf" in ctype.lower():
                return False, "PDFは自動照合できないため除外"
            charset = r.headers.get_content_charset() or "utf-8"
            text = html_to_text(body.decode(charset, errors="replace"))
            if len(text) < 200:
                return False, "本文が取得できない"
            return True, text[:12000]
    except Exception as e:  # noqa: BLE001
        return False, f"取得失敗: {e}"[:200]


# ---------------------------------------------------------------- queue

def load_queue(cfg):
    return read_csv(cfg["queue_file"])


def existing_keywords():
    _, rows = read_csv("docs/seo/keyword-map.csv")
    return [(r[0], r[4]) for r in rows if len(r) > 4]


def existing_text():
    return "\n".join(f"- {kw}（{url}）" for url, kw in existing_keywords())


def refill_queue(cfg):
    proposed = ask_openai(prompts.TOPIC_SYSTEM, prompts.TOPIC_USER.format(today=today().isoformat(), existing=existing_text()))
    reviewed = ask_claude(prompts.TOPIC_REVIEW_SYSTEM, json.dumps(proposed, ensure_ascii=False))
    header, rows = load_queue(cfg)
    known = {r[0] for r in rows} | {u.strip("/").split("/")[-1] for u, _ in existing_keywords()}
    added = 0
    for t in reviewed.get("topics", []):
        slug = re.sub(r"[^a-z0-9-]", "", str(t.get("slug", "")).lower())
        if not slug or slug in known:
            continue
        rows.append([slug, t.get("テーマ", ""), t.get("主キーワード", ""), t.get("補助キーワード", ""),
                     t.get("想定読者", ""), t.get("YMYL区分", "中"), "待機", "自動提案: " + t.get("備考", "")])
        known.add(slug)
        added += 1
    write_csv(cfg["queue_file"], header, rows)
    return added


def pick_task(cfg):
    header, rows = load_queue(cfg)
    for r in rows:
        if r[6] == "待機":
            return dict(zip(header, r))
    if refill_queue(cfg):
        return pick_task(cfg)
    return None


def set_queue_status(cfg, slug, status):
    header, rows = load_queue(cfg)
    for r in rows:
        if r[0] == slug:
            r[6] = status
    write_csv(cfg["queue_file"], header, rows)


# ---------------------------------------------------------------- validation

def all_text(article):
    parts = [article.get(k, "") for k in ("title", "description", "conclusion", "lead", "next_step", "breadcrumb")]
    parts += article.get("can_do", []) + article.get("checklist", [])
    for s in article.get("sections", []):
        parts.append(s.get("heading", ""))
        for b in s.get("blocks", []):
            parts += [b.get("text", ""), b.get("label", "")] + b.get("items", []) + b.get("lines", []) + b.get("headers", [])
            for row in b.get("rows", []):
                parts += row
    for f in article.get("faq", []):
        parts += [f.get("q", ""), f.get("a", "")]
    return "\n".join(str(p) for p in parts)


def prohibited_legal_claims():
    src = (ROOT / "tools/check-site.js").read_text(encoding="utf-8")
    block = re.search(r"prohibitedLegalClaims = \[([\s\S]*?)\];", src)
    return re.findall(r'"([^"]+)"', block.group(1)) if block else []


def validate(article, cfg):
    errs = []
    for key in ("title", "breadcrumb", "description", "conclusion", "lead", "next_step"):
        if not str(article.get(key, "")).strip():
            errs.append(f"{key} が空")
    if not 20 <= len(article.get("title", "")) <= 45:
        errs.append(f"title の文字数が範囲外（{len(article.get('title', ''))}字）")
    if not 60 <= len(article.get("description", "")) <= 140:
        errs.append(f"description の文字数が範囲外（{len(article.get('description', ''))}字）")
    if not 4 <= len(article.get("sections", [])) <= 9:
        errs.append("H2の数が4〜9の範囲外")
    if not 3 <= len(article.get("faq", [])) <= 6:
        errs.append("FAQの数が3〜6の範囲外")
    if not 4 <= len(article.get("checklist", [])) <= 12:
        errs.append("チェックリストの数が範囲外")
    sources = article.get("sources", [])
    if len(sources) < cfg["min_verified_sources"]:
        errs.append(f"確認済み出典が{len(sources)}件（{cfg['min_verified_sources']}件以上必要）")
    text = all_text(article)
    if re.search(r"<[a-zA-Z/][^>]*>", text):
        errs.append("本文にHTMLタグが含まれる")
    for n in {int(x) for x in re.findall(r"\[(\d+)\]", text)}:
        if not 1 <= n <= len(sources):
            errs.append(f"存在しない出典番号 [{n}]")
    checked = text.replace("必ずしも", "")
    for phrase in cfg["banned_phrases"] + prohibited_legal_claims():
        if phrase in checked:
            errs.append(f"禁止表現: {phrase}")
    for seg in re.split(r"[。！？\n]", text):
        if "エンディングノート" in seg and re.search(r"法的(?:な)?効力\s*(?:は|が)?\s*(?:ありません|ない|なし)", seg) \
                and not re.search(r"原則|通常|それだけ|だけでは|書いただけ|財産を移す", seg):
            errs.append("エンディングノートの法的効力を限定なしで否定")
    for rel in article.get("related", []):
        if rel not in cfg["allowed_related"]:
            errs.append(f"許可されていない内部リンク: {rel}")
    if len(article.get("related", [])) < 2:
        errs.append("関連記事が2件未満")
    body_len = sum(len(x) for x in text.split("\n"))
    if body_len < 2500:
        errs.append(f"本文が短すぎる（{body_len}字）")
    return errs


# ---------------------------------------------------------------- render

e = html.escape


def inline(text):
    out = e(str(text))
    return re.sub(r"\[(\d+)\]", r'<a href="#source\1" aria-label="出典\1">[\1]</a>', out)


def plain(text):
    return re.sub(r"\s*\[\d+\]", "", str(text)).strip()


def page_title(rel):
    p = ROOT / rel.lstrip("/")
    if p.is_dir() or rel.endswith("/"):
        p = p / "index.html"
    t = re.search(r"<title>([\s\S]*?)</title>", p.read_text(encoding="utf-8"))
    return html.unescape(t.group(1)).split("｜")[0].strip() if t else rel


def render_block(b):
    t = b.get("type")
    if t == "p":
        return f"<p>{inline(b['text'])}</p>"
    if t == "h3":
        return f"<h3>{e(plain(b['text']))}</h3>"
    if t in ("ul", "ol"):
        return f"<{t}>" + "".join(f"<li>{inline(i)}</li>" for i in b.get("items", [])) + f"</{t}>"
    if t == "example":
        lines = "".join(f"<p>{inline(x)}</p>" for x in b.get("lines", []))
        return f'<div class="memo-example"><p><strong>{e(b.get("label", "例"))}</strong></p>{lines}</div>'
    if t == "table":
        head = "".join(f"<th>{e(h)}</th>" for h in b.get("headers", []))
        body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in b.get("rows", []))
        return f'<div class="table-scroll"><table class="compare-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    return ""


def render(article, task, date, ymyl):
    slug = task["slug"]
    url = f"https://shukatsu-guide.jp/column/{slug}/"
    title, desc, crumb = article["title"], article["description"], plain(article["breadcrumb"])
    img = "https://shukatsu-guide.jp/images/ogp.jpg"
    ld_article = {
        "@context": "https://schema.org", "@type": "Article",
        "datePublished": date.isoformat(), "dateModified": date.isoformat(),
        "headline": title, "description": desc,
        "author": {"@type": "Organization", "name": "はじめての終活ガイド編集部"},
        "publisher": {"@type": "Organization", "name": "はじめての終活ガイド"},
        "image": img, "mainEntityOfPage": url,
    }
    ld_bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://shukatsu-guide.jp/"},
        {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]}
    ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(f["q"]), "acceptedAnswer": {"@type": "Answer", "text": plain(f["a"])}}
        for f in article["faq"]]}

    def ld(obj):
        return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + "\n</script>"

    sections = []
    for i, s in enumerate(article["sections"], 1):
        sections.append(f'<h2 id="sec{i}">{e(plain(s["heading"]))}</h2>\n' + "\n".join(render_block(b) for b in s.get("blocks", [])))
    can_do = "".join(f"<li>{inline(x)}</li>" for x in article["can_do"])
    checklist = "".join(f"<li>{inline(x)}</li>" for x in article["checklist"])
    faq = "\n".join(f'<details class="faq-item"><summary>{e(plain(f["q"]))}</summary><p class="faq-a">{e(plain(f["a"]))}</p></details>'
                    for f in article["faq"])
    srcs = "\n".join(f'<li id="source{i}"><a href="{e(s["url"])}">[{i}] {e(s["title"])}</a></li>' for i, s in enumerate(article["sources"], 1))
    related = "".join(f'<li><a href="../../{r.lstrip("/")}">{e(page_title(r))}</a></li>' for r in article["related"])
    first_related = article["related"][0]
    review_note = {"高": "法務・税務・医療に関わる内容を含みます。", "中": "契約・費用・制度に関わる内容を含みます。"}.get(ymyl, "")

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="/favicon.ico" sizes="48x48 32x32 16x16">
<link rel="icon" type="image/png" sizes="48x48" href="../../images/favicon-48.png">
<link rel="icon" type="image/png" sizes="32x32" href="../../images/favicon-32.png">
<link rel="icon" type="image/png" sizes="512x512" href="../../images/favicon.png">
<link rel="apple-touch-icon" href="../../images/apple-touch-icon.png">

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-M7NS8ZH6WL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-M7NS8ZH6WL');
</script>
<!-- 自動記事パイプライン（tools/auto-publish）で生成。ChatGPT下書き・Claude審査。 -->
<title>{e(title)}｜はじめての終活ガイド</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="はじめての終活ガイド">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="stylesheet" href="../../css/style.css">
{ld(ld_article)}
{ld(ld_bc)}
{ld(ld_faq)}
<style>
.checklist {{ list-style: none; margin: 0 0 18px; padding: 0; }}
.checklist li {{ position: relative; padding: 9px 0 9px 31px; border-bottom: 1px dashed var(--green-pale); }}
.checklist li::before {{ content: ""; position: absolute; left: 4px; top: 15px; width: 14px; height: 14px; border: 2px solid var(--green-soft); border-radius: 3px; }}
.compare-table {{ width: 100%; border-collapse: collapse; margin: 16px 0 10px; font-size: 15px; table-layout: fixed; }}
.compare-table th, .compare-table td {{ border: 1px solid var(--line-color); padding: 11px; text-align: left; vertical-align: top; overflow-wrap: anywhere; }}
.compare-table th {{ background: var(--green-pale); color: var(--green-deep); }}
.fact-box {{ background: var(--kinari); border-left: 5px solid var(--green-soft); border-radius: 8px; padding: 14px 16px; margin: 18px 0; }}
.memo-example {{ background: var(--kinari); border: 1px dashed var(--green-soft); border-radius: 8px; padding: 14px 16px; margin: 14px 0 18px; }}
.memo-example p {{ margin-bottom: 6px; }}
.src-list li {{ margin-bottom: 9px; overflow-wrap: anywhere; }}
.table-scroll {{ overflow-x: auto; }}
@media (max-width: 640px) {{
  .compare-table {{ font-size: 14px; }}
  .compare-table th, .compare-table td {{ padding: 8px; }}
}}
</style>
</head>
<body class="article-body">

<header class="site-header">
  <div class="header-inner">
    <p class="site-title"><a href="../../index.html">はじめての終活ガイド<span class="tagline">家族で考える、これからの暮らし</span></a></p>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="global-nav">メニュー</button>
    <nav class="global-nav" id="global-nav" aria-label="グローバルナビゲーション">
      <ul>
        <li><a href="../../index.html">ホーム</a></li>
        <li><a href="../../index.html#articles">記事一覧</a></li>
        <li><a href="../../about.html">運営者情報</a></li>
      </ul>
    </nav>
  </div>
</header>

<div class="container breadcrumb">
  <ol>
    <li><a href="../../index.html">ホーム</a></li>
    <li>{e(crumb)}</li>
  </ol>
</div>

<main class="article-container"><article><p class="pr-label">※本サイトはアフィリエイト広告を利用しています。</p><p class="author-line">作成：はじめての終活ガイド編集部（生成AIで作成）／専門家レビュー未実施</p><p class="article-meta">公開日：{jp_date(date)}／最終更新日：{jp_date(date)}／出典確認日：{jp_date(date)}</p><h1>{e(title)}</h1>
<div class="note-box">この記事は、生成AI（ChatGPT）で下書きし、別の生成AI（Claude）で出典との照合・推敲を行って公開した一般的な情報です。{review_note}運営者・専門家による個別の確認は行っていません。手続きや契約の判断は、各窓口や専門家に確認してください。</div>
<div class="fact-box"><p><strong>結論：</strong>{inline(article["conclusion"])}</p></div>
<p>{inline(article["lead"])}</p>
<h2 id="can-do">この記事でできること</h2><ul>{can_do}</ul>
{chr(10).join(sections)}
<h2 id="checklist">要点チェックリスト</h2><ul class="checklist">{checklist}</ul>
<h2 id="faq">よくある質問</h2>
{faq}
<h2 id="next">次の一歩</h2>
<p>{inline(article["next_step"])}</p>
<p><a class="btn btn-primary" href="../../{first_related.lstrip("/")}">{e(page_title(first_related))}を読む</a></p>
<h2 id="sources">参考にした公的情報・出典</h2><ol class="src-list">
{srcs}
</ol><p>確認日：{jp_date(date)}（自動取得した出典ページの本文と照合）。制度や窓口の情報は変わることがあるため、利用前に各機関の最新情報を確認してください。</p>
<section class="related"><h2>あわせて読みたい関連記事</h2><ul>{related}</ul></section>
</article></main>
<footer class="site-footer">
  <div class="container">
    <ul class="footer-nav">
      <li><a href="../../about.html">運営者情報</a></li>
      <li><a href="../../privacy.html">プライバシーポリシー</a></li>
      <li><a href="../../disclaimer.html">免責事項・広告掲載について</a></li>
    </ul>
    <p class="ad-notice">※本サイトはアフィリエイト広告を利用しています。Amazonのアソシエイトとして、当メディアは適格販売により収入を得ています。</p>
    <p class="copyright">&copy; <span class="js-year">2026</span> はじめての終活ガイド</p>
  </div>
</footer>

<button class="to-top" type="button" aria-label="ページ上部へ戻る">↑</button>
<script src="../../js/main.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- site updates

def update_index(slug, title, date):
    p = ROOT / "index.html"
    src = p.read_text(encoding="utf-8")
    li = (f'      <li><a href="column/{slug}/"><h3><span class="new-badge">NEW</span>{e(title)}</h3>'
          f'<p class="article-date">{jp_date(date)} 公開</p></a></li>\n')
    marker = "常に最新3本・公開日の新しい順） -->\n    <ul class=\"article-list\">\n"
    if marker not in src:
        raise PipelineError("index.html の新着記事リストが見つかりません")
    start = src.index(marker) + len(marker)
    end = src.index("    </ul>", start)
    items = re.findall(r"      <li>.*?</li>\n", src[start:end])
    src = src[:start] + li + "".join(items[:2]) + src[end:]
    all_marker = 'id="all-articles"'
    i = src.index(all_marker)
    j = src.index('<ul class="article-list">\n', i) + len('<ul class="article-list">\n')
    src = src[:j] + li + src[j:]
    p.write_text(src, encoding="utf-8")


def update_sitemap(slug, date):
    p = ROOT / "sitemap.xml"
    src = p.read_text(encoding="utf-8")
    src = re.sub(r"(<loc>https://shukatsu-guide.jp/</loc><lastmod>)[^<]+", r"\g<1>" + date.isoformat(), src)
    entry = f"  <url><loc>https://shukatsu-guide.jp/column/{slug}/</loc><lastmod>{date.isoformat()}</lastmod></url>\n"
    src = src.replace("</urlset>", entry + "</urlset>")
    p.write_text(src, encoding="utf-8")


def update_ledgers(task, article, date, ymyl, status, n_sources):
    url = f"/column/{task['slug']}/"
    title = article["title"]
    append_csv_row("docs/seo/content-inventory.csv", [url, "記事", title, title, date.isoformat(), date.isoformat(), status])
    append_csv_row("docs/seo/keyword-map.csv", [
        url, "記事", "親の終活（自動作成）", task["テーマ"], task["主キーワード"], task["補助キーワード"], task["想定読者"],
        task["テーマ"], "チェックリスト・手順・会話例・FAQ", "トップ", ";".join(article["related"]), status, ymyl,
        "未実施（自動公開）", date.isoformat(), date.isoformat()])
    append_csv_row("docs/seo/editorial-calendar.csv", [
        date.isoformat(), "新規(自動パイプライン)", title, url, status,
        f"ChatGPT下書き・Claude審査。自動取得で確認した出典{n_sources}件。専門家レビュー未実施"])
    append_csv_row("docs/seo/internal-link-map.csv", ["/", url, "トップ→記事", "新着記事・全記事一覧"])
    for r in article["related"]:
        append_csv_row("docs/seo/internal-link-map.csv", [url, r, "記事→関連", "関連記事欄"])


def update_state(note, date):
    p = ROOT / "docs/seo/automation-state.json"
    state = json.loads(p.read_text(encoding="utf-8"))
    state["last_run"] = f"{date.isoformat()}（自動記事パイプライン）"
    if note.get("published"):
        state["last_new_article"] = f"{date.isoformat()} {note['url']}（自動パイプライン）"
    state.setdefault("completed_tasks", []).append(f"{date.isoformat()} 自動パイプライン: {note['summary']}")
    p.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def append_run_log(date, lines):
    p = ROOT / "docs/seo/run-log.md"
    text = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(text + f"\n\n## {date.isoformat()} 自動記事パイプライン（ChatGPT×Claude）\n\n" + "\n".join(f"- {l}" for l in lines) + "\n",
                 encoding="utf-8")


# ---------------------------------------------------------------- main

def run(result_path):
    cfg = json.loads((ROOT / "tools/auto-publish/config.json").read_text(encoding="utf-8"))
    date = today()
    task = pick_task(cfg)
    if not task:
        return {"status": "skipped", "reason": "キューが空で、新しいテーマも採用されませんでした"}
    slug = task["slug"]
    if (ROOT / "column" / slug).exists():
        set_queue_status(cfg, slug, "重複のため除外")
        return {"status": "blocked", "slug": slug, "reason": "同名のページが既に存在", "auto_merge": True}
    if any(task["主キーワード"] == kw for _, kw in existing_keywords()):
        set_queue_status(cfg, slug, "重複のため除外")
        return {"status": "blocked", "slug": slug, "reason": "主キーワードが既存記事と重複", "auto_merge": True}

    existing = existing_text()
    writer_sys = prompts.WRITER_SYSTEM.replace("{allowed_related}", ", ".join(cfg["allowed_related"]))
    article = ask_openai(writer_sys, prompts.WRITER_USER.format(
        theme=task["テーマ"], main_kw=task["主キーワード"], sub_kw=task["補助キーワード"],
        reader=task["想定読者"], notes=task["備考"], existing=existing))

    fetched = {}
    verdict, ymyl, issues = "REVISE", task["YMYL区分"], []
    for _ in range(cfg["max_review_rounds"]):
        for s in article.get("sources", []):
            if s.get("url") and s["url"] not in fetched:
                fetched[s["url"]] = fetch_source(s["url"])
        src_report = "\n\n".join(
            f"### [{i}] {s.get('title')} {s.get('url')}\nverified={fetched.get(s.get('url'), (False, ''))[0]}\n{fetched.get(s.get('url'), (False, '未取得'))[1]}"
            for i, s in enumerate(article.get("sources", []), 1))
        review = ask_claude(prompts.REVIEWER_SYSTEM, prompts.REVIEWER_USER.format(
            theme=task["テーマ"], main_kw=task["主キーワード"], existing=existing,
            article=json.dumps(article, ensure_ascii=False, indent=1), sources=src_report))
        m = re.search(r"PASS|REVISE|BLOCK", str(review.get("verdict", "")).upper())
        verdict = m.group(0) if m else "BLOCK"
        issues += review.get("issues", [])
        article = review.get("article") or article
        # 審査結果のYMYLと、キュー登録時のYMYLの重い方を採用
        order = {"低": 0, "中": 1, "高": 2}
        ymyl = max([review.get("ymyl", "中"), task["YMYL区分"]], key=lambda x: order.get(x, 1))
        if verdict != "REVISE":
            break

    # 取得できた出典だけを残す（番号の付け直しはClaudeの責務。ここでは検証のみ）
    unverified = [s.get("url") for s in article.get("sources", []) if not fetched.get(s.get("url"), (False,))[0]]
    errs = validate(article, cfg)
    if unverified:
        errs.append(f"取得確認できない出典が残っている: {unverified}")
    if verdict != "PASS":
        errs.append(f"Claudeの審査結果が {verdict}")

    log = [f"テーマ: {task['テーマ']}（/column/{slug}/）", f"Claude審査: {verdict}／YMYL: {ymyl}",
           f"出典の取得確認: {sum(1 for v in fetched.values() if v[0])}/{len(fetched)}件"]
    log += [f"審査指摘: {x}" for x in issues[:20]]

    if errs:
        set_queue_status(cfg, slug, f"保留({date.isoformat()})")
        log += [f"不合格: {x}" for x in errs] + ["結果: 公開せず保留。記事ファイルは作成していません"]
        append_run_log(date, log)
        update_state({"summary": f"{slug} を保留（{'; '.join(errs)[:200]}）"}, date)
        (ROOT / "tools/auto-publish/last-rejected.json").write_text(json.dumps(
            {"slug": slug, "errors": errs, "issues": issues, "article": article}, ensure_ascii=False, indent=1), encoding="utf-8")
        return {"status": "blocked", "slug": slug, "reason": "; ".join(errs), "issues": issues, "auto_merge": True}

    auto_merge = cfg["auto_merge"] and ymyl in cfg["auto_merge_ymyl_levels"]
    status = "公開（自動パイプライン・AI作成・専門家レビュー未実施）" if auto_merge else "PR確認待ち（自動作成・高YMYL）"
    out_dir = ROOT / "column" / slug
    out_dir.mkdir(parents=True)
    (out_dir / "index.html").write_text(render(article, task, date, ymyl), encoding="utf-8")
    update_index(slug, article["title"], date)
    update_sitemap(slug, date)
    n_ok = len(article["sources"])
    update_ledgers(task, article, date, ymyl, status, n_ok)
    set_queue_status(cfg, slug, f"公開({date.isoformat()})" if auto_merge else f"PR確認待ち({date.isoformat()})")
    log.append("結果: " + ("検証通過後に自動マージ・公開" if auto_merge else "高YMYLのためPRで運営者確認待ち"))
    append_run_log(date, log)
    update_state({"published": auto_merge, "url": f"/column/{slug}/", "summary": f"{article['title']}（/column/{slug}/）{status}"}, date)
    (ROOT / "tools/auto-publish/last-rejected.json").unlink(missing_ok=True)
    return {"status": "created", "slug": slug, "title": article["title"], "ymyl": ymyl, "auto_merge": auto_merge,
            "issues": issues, "url": f"https://shukatsu-guide.jp/column/{slug}/"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--result", default="/tmp/auto-publish-result.json")
    args = ap.parse_args()
    try:
        result = run(args.result)
    except PipelineError as ex:
        result = {"status": "error", "reason": str(ex)}
    except Exception as ex:  # noqa: BLE001  想定外の失敗も結果ファイルに残して通知する
        import traceback
        result = {"status": "error", "reason": f"{type(ex).__name__}: {ex}", "trace": traceback.format_exc()[-2000:]}
    Path(args.result).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "error" else 0


if __name__ == "__main__":
    sys.exit(main())
