## 2026-11-07 公開前再検証（この節が現在状態）

- PR #80は未マージ。本番URLは2026-11-07 09:40 JSTにHTTP 404。今回の利用者指示により再承認までマージ・公開禁止。
- 公開対象は `column/car-sale-retirement-checklist/index.html`。以下の下書きパス・noindex・日付未設定の記録は11月6日の実装時点の履歴。現在の公開用HTMLはnoindexなし。
- 公開予定日を2026-11-07へ同期。原稿確認日2026-11-06と過去の承認履歴は維持。承認・公開が翌日以降なら実際の公開日に再同期する。
- 最新head 78031dcの共通ハーネスを再実行：4回帰テスト、HTML53・内部リンク1766、アフィリエイト38・CTA13が成功。CIの検証対象はマージ予定SHA a6b4f1e（成功）。
- 出典3件を公式本文で直接再照合。2026-11-05注意喚起と2024-06-18解説は別資料。電話番号・受付時間、申告済み修復歴等の条件に不一致なし。専門家レビュー未実施は継続。
- 320/375/390pxのiframeで表示確認（実機ではない）。画像・見出し・表を確認。

---
以下は実装時点の履歴です。

# 公開承認後の更新（2026-11-06）

運営者が「コミット・プッシュ・PR作成・マージ・公開してください」と明示承認。
`column/car-sale-retirement-checklist/index.html`へ移動、noindex解除、実際の公開作業日2026-11-06を公開日・更新日に設定。トップ新着3件・全記事一覧、親の終活ハブ、sitemapと既存管理台帳を同期。既存記事の日付はリンク追加のみのため据え置き。
法務等の専門家レビュー未実施の表示は維持。原稿原本と画像は維持。本文の「公開前に人が確認すべき事項」は公開状態に合わせ「専門家への確認が必要な事項」へ変更（各確認項目は保持）。

以下は公開承認前の実装・検証履歴。下書きパス・未公開・未コミット・停止の記述は当時の状態を表す。現在の状態は冒頭とPR・GitHub Actionsの実行結果を参照。

---

# 車を手放す前の終活チェック：実装・検証報告

確認日：2026-11-06（日本時間）。対象 `tfqys680-jpg/shukatsu-site`。取得時HEAD `6505dc582d234bde34126d333115eb6e5098d316`。取得時の作業ツリーはクリーン。Roadは未操作。コミット・プッシュ・PR・マージ・デプロイ・公開は実施していない。

## 判定と公開状態

新規記事。keyword-map全体と既存記事を確認し、article16は「免許返納の切り出し方」、article12は「持ち物整理全般」で、本記事の「査定・売却契約・入金確認」と分離できる。同テーマの未完了PRは確認されなかった（オープンPR #76/#74/#62/#58/#57/#52/#50/#47/#45/#44/#43）。

- 実装：`drafts/car-sale-retirement-checklist/index.html`
- 公開予定URL：`https://shukatsu-guide.jp/column/car-sale-retirement-checklist/`（未公開）
- noindex。canonical/OGP/Article/mainEntityOfPageは既存下書き方式の公開予定URL。
- datePublished/dateModifiedは省略、公開日・実質更新日は未定。原稿確認日2026-11-06を公開日に流用しない。
- Article/BreadcrumbList実装。FAQ本文3件は維持、一般情報サイトのFAQリッチリザルト適格性が未確認のためFAQPageは追加しない。
- 一覧・カテゴリ・sitemapは未公開に合わせて掲載しない。content-inventory/keyword-map/editorial-calendarに下書き状態を登録。internal-link-mapは実際のdraftsから公開記事へのリンクを記録。
- 元原稿全文を `docs/seo/car-sale-retirement-checklist-source.txt` に無改変で保存。本文・表・FAQ・CTA・出典・人手確認事項を使用。SEO指定はmetadata、画像案は提供画像とalt、実装指示は管理記録に反映。
- 出典3件の照合方法・結果はsource-policy.mdへ追記。[1]は直接取得エラー後、公式ページの検索取得本文を確認。[2][3]は公式本文を直接確認。一次資料照合と専門家レビューは区別。

## 画像

すべて同梱画像から作成。外部取得・別画像生成なし。PNG原本はZIPとバイト単位で一致。既存のPillow WebP q80/method6・1600/1200/800px方式に合わせ、16:9へごく小さく中央クロップ。

| 実パス（リポジトリルート基準） | 寸法 | 容量 |
|---|---|---:|
| public/images/shukatsu/car-sale-retirement-checklist-hero.png | 1672×941 | 2,350,389 B |
| images/column-car-sale-retirement-checklist.webp | 1600×900 | 116,256 B |
| images/column-car-sale-retirement-checklist-1200.webp | 1200×675 | 78,246 B |
| images/column-car-sale-retirement-checklist-800.webp | 800×450 | 42,354 B |

picture/sourceのWebP srcset+sizes、imgのフォールバックは指定PNG実パス。GitHub Pagesはルート配信のためPNG参照URLにも `/public/` を含める。width/heightとaspect-ratioで領域を確保。ファーストビューはlazyなし・fetchpriority=high・decoding=async。指定altと生成AI・架空人物・実際の相談者/被害者/推薦者ではない旨を表示。OGP/Twitter/Article画像は同じ1600px WebP。1.91:1と2:1の想定クロップで顔の欠けなしを目視確認。未公開のため実SNSクローラによる取得・キャッシュ表示は未確認。一覧に画像を追加していないため下方一覧画像のlazy判定は今回対象外（公開時追加ならlazyを検討）。

## 検証

| コマンド・確認 | 結果 |
|---|---|
| node tools/check-site.js | PASS：HTML53件・内部リンク1764件 |
| node tools/check-click-tracking.js | PASS：HTML49件・アフィリエイト38・CTA13・商品12 |
| python3 tools/agent-harness/test_runner.py | PASS：4テスト（共通ハーネス内で実行） |
| python3 tools/agent-harness/run.py --output /workspace/scratch/0689b83da56f/car-verification | 内部3チェックPASS、総合blocked（未コミット変更があるため）。終了コード1。成功扱いにしない |
| git diff --check | PASS |
| build / lint / 型チェック | package.json・専用定義なし。コマンドを新設せず未実行 |
| 原稿本文・原稿原本・PNG原本 | 本文段落保持、原本バイト一致を確認 |
| リンク/画像/srcset | ローカル21参照先の存在確認。ブラウザでヒーロー表示・WebP選択・CTA遷移を確認 |
| metadata/構造化データ/日付 | title/description/canonical/OGP/Twitter、Article/BreadcrumbList構文・パンくず一致、日付未設定を確認 |
| 公開管理 | CSV列数一致、noindex、一覧・カテゴリ・sitemap非掲載を確認 |

表示はクラウドブラウザのiframeビューポート320/375/390/1280pxで確認（実機ではない。スクロールバー幅15px分を除くclientWidth=305/360/375/1265）。各幅でscrollWidth=clientWidth、表と画像に横はみ出しなし。画像は16:9、800px WebP選択・読み込み完了。PC画像表示724×407.25px、モバイル269×151.3125/324×182.25/339×190.6875px。FAQ開閉、CTAのarticle02への遷移、パンくずを確認。CLSは領域確保を検証したが実測値は未計測。LCP実測・実端末・全外部リソースのHTTPステータス網羅は未実施。shellからプレビューHTTP接続は拒否されたため全21件HTTP200とは報告しない（ブラウザ経路は表示可能）。

初回クリック検証でgtag初期化不足を検出し既存方式へ修正、再検証PASS。追加照合の初回はbs4未導入で停止し、標準ライブラリへ変更して完了。既存共通CSS/JSと既存公開記事は未変更。

## 人手確認・残課題

- 法務：クーリング・オフ対象外と解除・取消し等の区別、口頭での契約成立、キャンセル料、申告内容に応じた減額要求、名義・相続・代理権限。専門家レビュー未実施。
- 医療：年齢から認知症や運転能力低下を推定せず、医学的判断をしない記述の確認。診断・運転助言を追記する場合は医療職確認。
- 税務：売却益・自動車税・還付の具体的説明は追加していない。追加時は用途・登録状況等を税理士へ照合。
- 編集：出典の申告条件、相談年月日未公表、2026年注意喚起と2024年既存解説の区別、本人の意思尊重を公開前に再確認。
- 公開を指示された後にのみdrafts→column移動、noindex解除、実際の公開日設定、一覧・ハブ・sitemapと各台帳の同期を行う。今回は確認待ちで停止。

## 変更ファイル

- `docs/seo/automation-state.json`
- `docs/seo/car-sale-retirement-checklist-review.md`
- `docs/seo/car-sale-retirement-checklist-source.txt`
- `docs/seo/content-inventory.csv`
- `docs/seo/editorial-calendar.csv`
- `docs/seo/internal-link-map.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/run-log.md`
- `docs/seo/source-policy.md`
- `docs/seo/ymyl-review-queue.md`
- `drafts/car-sale-retirement-checklist/index.html`
- `images/column-car-sale-retirement-checklist-1200.webp`
- `images/column-car-sale-retirement-checklist-800.webp`
- `images/column-car-sale-retirement-checklist.webp`
- `public/images/shukatsu/car-sale-retirement-checklist-hero.png`
