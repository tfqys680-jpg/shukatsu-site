# はじめての終活ガイド（shukatsu-guide.jp）

終活カウンセラー1級が執筆・監修する終活情報サイト。手書き静的HTML＋GitHub Pages（mainブランチ/ルート配信、独自ドメイン shukatsu-guide.jp）。

## 構成

- `index.html` / `about.html` / `privacy.html` / `disclaimer.html` — 固定ページ
- `articles/article01〜15.html` — 記事（URLは恒久維持。変更しない）
- `ending-note/family-story/` — 体験談LP（柱記事）
- `parent-shukatsu/` — 親の終活カテゴリーハブ／`parent-shukatsu/questions/` — 30項目記事
- `downloads/` — 配布PDF（生成物。ソースは tools/pdf/）
- `docs/seo/` — SEO運用管理ファイル（戦略・カレンダー・キーワードマップ・実行ログ等）
- `.claude/prompts/shukatsu-seo-routine.md` — 週次SEOルーチンの定期実行プロンプト
- `drafts/` — レビュー待ち下書き（noindex必須・sitemap非掲載。詳細は docs/seo/ymyl-review-queue.md）

## 検証（コミット前に必ず実行）

```
node tools/check-site.js
```

内部リンク・アンカー・タグ整合・JSON-LD構文・FAQ/パンくずのDOM↔構造化データ一致・title重複・H1数・sitemap照合・drafts混入を検査します。

## PDFの再生成

配布PDFのソースは `tools/pdf/*.html`（印刷用CSS内蔵）。Chromeヘッドレスで生成します。

```
powershell -ExecutionPolicy Bypass -File tools/build-pdf.ps1
```

`tools/pdf/<name>.html` → `downloads/<name>.pdf` に出力されます。内容を変更したらHTMLソース内の版番号（例: v1.0）と日付も更新してください。

## デプロイ

mainへのpushで GitHub Pages に自動反映されます。**作業はブランチ＋PRで行い、mainへ直接コミットしないこと。**

## 運用ルール

docs/seo/seo-strategy.md と .claude/prompts/shukatsu-seo-routine.md を参照。
