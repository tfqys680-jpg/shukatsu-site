
## 2026-11-09 公開指示による更新

運営者がコミット・プッシュ・PR作成・マージ・公開を明示指示。以下の下書き・禁止記録は前段階の履歴。column/へ移動、noindex解除、公開日/更新日・URL・台帳・sitemap・トップ新着/一覧・相談先記事からの入口を同期。専門家レビュー未実施は継続。
# 無料相談の準備記事・実装確認記録

2026-11-09（日本時間）。対象 tfqys680-jpg/shukatsu-site。基点 main 3414ec6412a72eead2a200e6c444d487bfa70646。

## 状態と配置

ローカル実装のみ。未コミット・未プッシュ・PRなし・未マージ・未公開。最新のユーザー指示を優先し停止する。

- 下書き: `/drafts/shukatsu-free-consultation-preparation/`
- 公開予定: `https://shukatsu-guide.jp/column/shukatsu-free-consultation-preparation/`（現在の公開URLではない）
- noindexあり。sitemap非掲載。トップや公開記事からの入口は未追加。
- datePublished/dateModifiedは未設定。原稿・出典確認日と公開日を区別。
- canonical/OGP/Article/mainEntityOfPage/BreadcrumbListは現在のdrafts URLで一致。公開時にcolumn URLへ一括変更。

## 実装と原稿

article-draft.txtの導入・全見出し・本文・チェックリスト6件・FAQ3件は機械照合で全文一致。SEOタイトルとdescription、出典4URL、注意事項と人手確認事項を保持。実装用の指示文は表示せず適用。news-brief.txtは不使用。
既存のcolumn/car-sale-retirement-checklist/のレイアウト・共通CSS/JS・ヘッダー/フッターと、drafts/parent-care-without-burnout/の下書き運用を参照。
where-to-askは最初の窓口選び、本記事は無料相談前後の準備と費用確認に特化。既存の窓口記事に準備メモの重なりはあるが、無料相談の範囲・担当者・継続依頼の確認を主検索意図として新規追加。公開後は検索意図の重複を観察する。
ArticleとBreadcrumbListを実装。FAQは最新記事同様に可視FAQのみ。既存記事のFAQPage利用は一律ではなく、当記事への追加は見送り。リッチリザルトは保証しない。
内部リンク先: where-to-ask、article11、questions、article02。架空の無料相談受付・専門家紹介は追加していない。

## 画像

元画像: `public/images/shukatsu/shukatsu-free-consultation-preparation-hero.png`、1672×941、1,987,211 bytes。ZIP内原本とバイト一致、変更なし。
最適化: 16:9中央クロップ、WebP quality 80。

| images/配下の実ファイル | 実寸 | 容量 |
|---|---|---:|
| column-shukatsu-free-consultation-preparation.webp | 1600×900 | 76,880 B |
| column-shukatsu-free-consultation-preparation-1200.webp | 1200×675 | 52,696 B |
| column-shukatsu-free-consultation-preparation-800.webp | 800×450 | 30,070 B |

本文はsrcset/sizes、width=1600/height=900、aspect-ratio:16/9、loading=eager、fetchpriority=high。OGP/Twitter/Articleは同じ1600px画像。既存16:9比率で両者の顔が収まることを目視確認。別のSNSによる任意の切り抜きは未保証。
指定altを使用し、生成AIの架空人物・実際の相談会写真でないと明記。

## 検証

- `node tools/check-site.js`: PASS（HTML54件・内部リンク1790件）。H1、タグ、アンカー、内部リンク、JSON-LD、下書きsitemap混入を確認。
- `node tools/check-click-tracking.js`: PASS（public HTML50、affiliate38、CTA13、products12）。
- `git diff --check`: PASS。
- `python3 tools/agent-harness/run.py --output /workspace/scratch/f015471e5457/harness-evidence`: 総合 blocked。harness-regression/site/click-trackingは全passedだがdirty_before/after=true。ユーザーのコミット禁止指示に従うためで、最終コミットの検証成功ではない。release_ready=false。
- package.jsonなし。独立のビルド・lint・型チェックは未定義。
- 原稿全文照合・元PNG一致・Article/BreadcrumbListのJSONパース: PASS。
- ブラウザ表示: iframe外寸320/375/390/1280pxで確認。縦スクロールバー15pxを除いた有効幅305/360/375/1265pxでscrollWidth=clientWidth、画像読み込み成功、H1各1件。PC単独表示1348pxも横はみ出しなし。FAQ Q1の開閉を確認。スマホ実機ではない。
- CLS対策: 画像寸法と比率の予約を確認。PerformanceObserver等によるCLSの数値測定は未実施。CLS=0とは報告しない。

## 出典照合

2026-11-09にWeb取得で確認。原稿URLは変更なし。
- 福津市: 11/6更新、11/22相談会、宮司コミュニティセンター、無料、申込なし参加可能、一般社団法人えん主催を照合。市主催とは書かない。
- 法テラス: 収入・資産条件と原則事前予約を照合。
- 国民生活センター: 支払総額・提供内容・解約条件の確認、理解できなければ即決せず相談という助言を照合。既存注意喚起として区別。
- 消費者庁: 補助資料URLを取得。

## 人手確認・残課題

法務: 相談職種の業務範囲、本人同意・代理権、無料条件、契約表現、主催者の明記。専門家レビュー未実施。
医療: 診断・治療助言は追加していない。医療・介護案内を加筆する際は担当窓口と確認。
税務: 個別税額・期限・節税効果は追加していない。加筆時は税理士確認。
編集: 公開直前に11/22イベントの変更・開催前後・出典リンクを再確認。終了後なら過去の事例へ修正し募集を促さない。
公開時は運営者の確認後、公開パス・日付・noindex・入口リンク・sitemap・各台帳を一括同期し、実コミットでハーネスを再実行する。

## 変更ファイル一覧

- `docs/seo/shukatsu-free-consultation-preparation-review.md`
- `drafts/shukatsu-free-consultation-preparation/index.html`
- `images/column-shukatsu-free-consultation-preparation-1200.webp`
- `images/column-shukatsu-free-consultation-preparation-800.webp`
- `images/column-shukatsu-free-consultation-preparation.webp`
- `public/images/shukatsu/shukatsu-free-consultation-preparation-hero.png`
- `docs/seo/automation-state.json`
- `docs/seo/content-inventory.csv`
- `docs/seo/editorial-calendar.csv`
- `docs/seo/internal-link-map.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/run-log.md`
- `docs/seo/source-policy.md`
- `docs/seo/ymyl-review-queue.md`

## 2026-11-10 マージ・公開指示への対応

PR #83の公開済み内容を保持してmainを統合。トップ新着は成年後見・無料相談・車売却の3本。無料相談の公開日を2026-11-10へ本文・Article・sitemap・台帳・トップ新着で同期し、11月9日の原稿・出典確認日は保持。福津市の11月22日相談会案内を一次資料で再確認。check-site: HTML55・内部リンク1818、click-tracking成功。専門家レビュー・実機・CLS実測は未実施のまま。
