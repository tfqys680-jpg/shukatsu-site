// shukatsu-site 品質チェック
// - 内部リンク存在・ページ内アンカー・タグ整合
// - JSON-LD構文・FAQ/パンくずのDOM↔JSON-LD一致
// - title重複・H1数・sitemap照合・drafts混入
// 実行: node tools/check-site.js
const fs = require("fs");
const path = require("path");
const ROOT = path.resolve(__dirname, "..");

const htmlFiles = [];
(function walk(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === ".git" || e.name === "node_modules") continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith(".html")) htmlFiles.push(p);
  }
})(ROOT);

let errors = [];
let checkedLinks = 0;
const relOf = f => path.relative(ROOT, f).split(path.sep).join("/");
const isSitePage = rel => !rel.startsWith("tools/") && !rel.startsWith("docs/") && !rel.startsWith("drafts/");

// 法務コピーの回帰防止（2026-08-10 Codex P2レビュー対応）
const prohibitedLegalClaims = [
  "相続税がかからないご家庭でも、財産を誰にどう渡すかという話し合い（遺産分割協議）は必要になります",
  "全員の署名・押印が必要な話し合い",
  "財産を渡す意思を法的な形で残せるのは遺言書",
  "財産の分け方はエンディングノートやメモでは法的効力がありません。遺言書が必要です",
  "財産の分け方など、法的な意思表示が必要なことは別途遺言書が必要です",
  "財産の分け方など法的に有効な意思表示をしたい場合は、遺言書の作成が必要です",
  "法的な効力を持たせたい場合は、遺言書の作成をご検討ください",
  "法的に決めたいことは遺言書へ"
];
const requiredLegalCopy = {
  "column/will-for-ordinary-families/index.html": [
    "遺産分割協議が不要なこともあります",
    "生前贈与、死因贈与、信託"
  ]
};

for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  const dir = path.dirname(file);
  const rel = relOf(file);

  for (const claim of prohibitedLegalClaims) {
    if (html.includes(claim)) errors.push(`${rel}: misleading legal claim returned: ${claim}`);
  }
  if (rel.startsWith("tools/") || rel.startsWith("docs/")) continue; // PDFソース等はリンク・構造検査の対象外
  for (const required of requiredLegalCopy[rel] || []) {
    if (!html.includes(required)) errors.push(`${rel}: required legal qualification missing: ${required}`);
  }

  // collect ids in this file
  const ids = new Set();
  for (const m of html.matchAll(/id="([^"]+)"/g)) ids.add(m[1]);

  // href / src links
  for (const m of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const url = m[1];
    if (/^(https?:|mailto:|tel:|data:)/.test(url)) continue;
    checkedLinks++;
    if (url.startsWith("#")) {
      const id = url.slice(1);
      if (id && !ids.has(id)) errors.push(`${rel}: page anchor not found: #${id}`);
      continue;
    }
    const [pathPart, hash] = url.split("#");
    if (pathPart === "") continue;
    const target = pathPart.startsWith("/") ? path.join(ROOT, pathPart) : path.resolve(dir, pathPart);
    if (!fs.existsSync(target)) {
      errors.push(`${rel}: broken link: ${url}`);
      continue;
    }
    if (hash && target.endsWith(".html")) {
      const targetHtml = fs.readFileSync(target, "utf8");
      if (!new RegExp(`id="${hash}"`).test(targetHtml)) {
        errors.push(`${rel}: anchor #${hash} not found in ${pathPart}`);
      }
    }
  }

  // tag balance for key tags
  for (const tag of ["script", "style", "main", "header", "footer", "article", "section", "table", "details", "summary", "nav", "ul", "ol", "title", "head", "body", "html"]) {
    const open = (html.match(new RegExp(`<${tag}(\\s[^>]*)?>`, "g")) || []).length;
    const close = (html.match(new RegExp(`</${tag}>`, "g")) || []).length;
    if (open !== close) errors.push(`${rel}: <${tag}> open=${open} close=${close}`);
  }

  // required marks in articles
  if (rel.startsWith("articles")) {
    if (!html.includes("執筆・監修：終活カウンセラー1級")) errors.push(`${rel}: missing 執筆・監修 line`);
    if (!html.includes("アフィリエイト広告を利用しています")) errors.push(`${rel}: missing ad notice`);
    if (!html.includes('"@type": "Article"')) errors.push(`${rel}: missing Article JSON-LD`);
  }

  // drafts は noindex 必須
  if (rel.startsWith("drafts/") && !/name="robots"[^>]*noindex/.test(html)) {
    errors.push(`${rel}: draft page missing noindex meta`);
  }

  // JSON-LD parse check + FAQ/Breadcrumb consistency
  const ldDocs = [];
  for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try { ldDocs.push(JSON.parse(m[1])); } catch (e) { errors.push(`${rel}: invalid JSON-LD: ${e.message}`); }
  }
  const strip = s => s.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/\s+/g, "").trim();
  const faqLd = ldDocs.find(d => d["@type"] === "FAQPage");
  if (faqLd) {
    const domQ = [...html.matchAll(/<summary>([\s\S]*?)<\/summary>/g)].map(m => strip(m[1]).replace(/^Q\d+\./, ""));
    const domA = [...html.matchAll(/<p class="faq-a">([\s\S]*?)<\/p>/g)].map(m => strip(m[1]));
    const ldQ = faqLd.mainEntity.map(q => strip(q.name));
    const ldA = faqLd.mainEntity.map(q => strip(q.acceptedAnswer.text));
    if (JSON.stringify(domQ) !== JSON.stringify(ldQ)) errors.push(`${rel}: FAQ questions mismatch DOM vs JSON-LD`);
    domA.forEach((a, i) => { if (a !== ldA[i]) errors.push(`${rel}: FAQ answer #${i + 1} mismatch DOM vs JSON-LD`); });
    if (domA.length !== ldA.length) errors.push(`${rel}: FAQ answer count mismatch`);
  }
  const bcLd = ldDocs.find(d => d["@type"] === "BreadcrumbList");
  if (bcLd) {
    const bcHtml = (html.match(/<div class="container breadcrumb">([\s\S]*?)<\/div>/) || [])[1] || "";
    const domCrumbs = [...bcHtml.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => strip(m[1]));
    const ldCrumbs = bcLd.itemListElement.map(i => strip(i.name));
    if (JSON.stringify(domCrumbs) !== JSON.stringify(ldCrumbs)) errors.push(`${rel}: breadcrumb mismatch DOM ${JSON.stringify(domCrumbs)} vs JSON-LD ${JSON.stringify(ldCrumbs)}`);
  }
}

// title重複・H1数（公開ページのみ）
const titleMap = {};
for (const file of htmlFiles) {
  const rel = relOf(file);
  if (!isSitePage(rel)) continue;
  const html = fs.readFileSync(file, "utf8");
  const t = (html.match(/<title>([\s\S]*?)<\/title>/) || [])[1];
  if (t) (titleMap[t.trim()] = titleMap[t.trim()] || []).push(rel);
  const h1c = (html.match(/<h1[\s>]/g) || []).length;
  if (h1c !== 1) errors.push(`${rel}: h1 count=${h1c}`);
}
for (const [t, files] of Object.entries(titleMap)) {
  if (files.length > 1) errors.push(`duplicate title "${t.slice(0, 30)}…": ${files.join(", ")}`);
}

// sitemap coverage（drafts/tools/docs は対象外。draftsの混入は検出）
const sitemap = fs.readFileSync(path.join(ROOT, "sitemap.xml"), "utf8");
for (const file of htmlFiles) {
  const rel = relOf(file);
  if (rel.startsWith("drafts/")) {
    if (sitemap.includes(rel.replace(/\/index\.html$/, "/"))) errors.push(`sitemap.xml: draft page included: ${rel}`);
    continue;
  }
  if (!isSitePage(rel)) continue;
  const relDir = rel.endsWith("/index.html") ? rel.slice(0, -10) : null;
  const url = relDir ? `https://shukatsu-guide.jp/${relDir}` : rel === "index.html"
    ? "https://shukatsu-guide.jp/"
    : `https://shukatsu-guide.jp/${rel}`;
  if (!sitemap.includes(`<loc>${url}</loc>`)) errors.push(`sitemap.xml: missing ${url}`);
}

console.log(`HTML files: ${htmlFiles.length}, internal links checked: ${checkedLinks}`);
if (errors.length) {
  console.log("ERRORS:");
  errors.forEach(e => console.log("  " + e));
  process.exit(1);
} else {
  console.log("ALL CHECKS PASSED");
}
