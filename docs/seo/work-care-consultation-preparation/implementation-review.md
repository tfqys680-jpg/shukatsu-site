# 職場への介護相談の準備：実装・公開承認記録

2026年11月21日（日本時間）。**運営者がコミット・プッシュ・PR作成・マージ・公開・デプロイを明示承認。公開用ファイルの準備済み。**

以下のローカル実装報告は公開承認前の履歴。現在の実装先は `column/work-care-consultation-preparation/index.html`、公開日・更新日は2026-11-21。noindex解除、sitemap・トップ・親の終活ハブ・SEO台帳を同期済み。元原稿の編集者向け確認項目は本報告とymyl-review-queue.mdに保持し、読者向け注意事項を本文に掲載。専門家監修は未実施のまま。

## ローカル下書き時点の実装と検索意図

- 記事：`drafts/work-care-consultation-preparation/index.html`。
- SEOタイトル：親の介護が始まったら｜退職を決める前に職場へ相談する準備。title末尾は既存方式のサイト名。
- 正式予定URL：`https://shukatsu-guide.jp/column/work-care-consultation-preparation/`。現時点はローカル下書きのみ。
- 最新main `6b0576b1a4c7439a04e39a179d608fdd6f7697ff` を新規チェックアウト。開始時の差分なし。他の作業環境は変更せず、HEADも維持。作業ブランチは `local/work-care-consultation-preparation`。
- AGENTS.md、CLAUDE.md、README、共通ハーネス、SEO戦略・台帳・公開制御、既存記事・CSS・JS・検証コードを確認。手書き静的HTMLでpackage.json・ビルド工程・lint/型設定なし。
- 既存の `drafts/parent-care-without-burnout/` は家族会議・費用・介護全般の計画。仕事との両立の段落はあるが、本稿は職場面談前の必要時間・希望・確認質問・情報共有範囲に限定し主検索意図を分離。既存記事を削除・統合・変更していない。GitHubの未完了PRを「介護」で検索し該当なし。
- 導入、H2本文3節・H3全6件、チェックリスト7項目、FAQ3件、CTA、出典2件、注意事項を保持。原稿31ブロックを照合済み。news-brief.txtを本文へ転載していない。原稿全文と画像説明を同ディレクトリに保存。
- 共通の記事デザイン、目次、FAQ、CTA、ナビ・フッター、JSと計測方式を使用。制度の一般説明と編集提案を区別。専門家監修未実施を明記し、法務・労務・医療・税務の確認先を案内。架空のサービス・監修者・金額・効果は追加していない。

## 公開制御・SEO

- noindex、sitemap非掲載、公開記事一覧・ハブからの流入導線なし。正式URLのHTMLは未作成。
- canonical・og:url・Article/mainEntityOfPage・BreadcrumbListは既存下書きと同じく正式予定URL。Article、BreadcrumbList、表示内容と一致するFAQPageを設定。検索でのFAQ表示は保証しない。
- 公開日未定。datePublished/dateModified・公開日時の仮置きなし。作成日・ニュース日を公開日として流用しない。
- content-inventory、keyword-map、editorial-calendar、internal-link-map、source-policy、ymyl-review-queueへ下書きとして登録。公開日・最終実質更新日とも未定。自動運用の最終公開日時は変更なし。
- コミット・プッシュ・PR作成・マージ・公開・デプロイは一切実施していない。

## 実際の画像配置・最適化

すべて `public/images/shukatsu/work-care-consultation-preparation-` に続く名前。

| ファイル末尾 | 実寸 | バイト数 |
|---|---|---:|
| hero.png | 1672×941 | 2,044,100 |
| hero-640.webp | 640×360 | 22,652 |
| hero-960.webp | 960×540 | 43,134 |
| hero-1600.webp | 1600×900 | 93,274 |
| ogp.webp | 1200×630 | 57,210 |

原本は添付PNGとバイト一致。SHA-256：`feb53be56ae30ed13b497d2d3a3aa207049256ba1126dc697080d8e358ed646b`。

本文は960版を標準に640/960/1600wのsrcset。sizesは `(max-width: 760px) calc(100vw - 36px), 724px`。実際の標準画像と一致するwidth=960/height=540、width:100%・height:autoにより領域確保。fetchpriority=high・decoding=async、lazyなし。altは指定どおり「親の介護と仕事の予定を、自宅で話し合う母親と娘のイメージ」。

通常版は全体縮小し人物を切らない。OGP版は全体を1200×630の枠へ収め、左右に淡い余白を付けて人物を保持。OGP・Article imageは同じ生成画像由来のOGP版。原本とOGP画像ファイルは目視確認済み。新規画像生成・外部素材取得はなし。画像依存部分の未配置はなし。

## 検証結果

| 検証 | 結果 |
|---|---|
| node tools/check-site.js | PASS：HTML62件・内部リンク2073件。JSON-LD構文、FAQ/パンくずの表示との一致、noindex、sitemap除外等 |
| node tools/check-click-tracking.js | PASS：スクリプト固有集計でHTML58・アフィリエイト38・CTA13・商品12。下書きは公開されていない |
| 共通ハーネス | 内部チェック3件PASS（回帰テスト4件含む）。総合status=blocked / release_ready=false。指示どおり未コミットでdirty=trueのため、総合合格と扱わない |
| 原稿・画像・公開状態照合 | PASS：原稿31ブロック、H3×6、チェックリスト7、FAQ3、原本一致、srcset寸法、画像標準寸法、CSV列数、公開HTML無変更 |
| git diff --check | PASS |
| build / lint / 型チェック | 設定・工程が存在しないため対象外。実行成功とは数えない |
| PC・スマートフォン実画面 | **未実施**。ローカルChromiumがsocket作成制限で起動失敗。別のブラウザーからローカルHTTPへも接続できず。本文・余白・横スクロール・FAQ開閉・CTA遷移・CLS/LCP実測は未確認 |
| OGPのSNS上の表示 | **未実施**。ローカルのみのためクローラー取得は未確認。画像寸法・画像自体は確認済み |

共通ハーネス証跡：リポジトリ外 `../verification/harness-final/report.json` と `summary.md`。最後の画像width/height整合・本報告作成後にサイト検証を再実行。追加照合結果は `../verification/content-contract.json`。

## 出典確認と人の確認事項

公式2ページの原文を2026-11-21に確認。北海道のページ表示日11/11、情報基準2026年10月、相談チェックシートの案内を確認。厚労省の企業向けガイドと両立支援ツールの掲載を確認。新規公開日を推測せず、原稿の11/19は原稿作成時の確認日として保持。URL・詳細はsource-policy.mdと記事本文に記載。添付PDF全文、就業規則、制度の個別適用、給付額は未確認で、日数・金額を追記していない。

1. PCと320/375/390pxで本文・画像・FAQ・CTA・目次・余白・横スクロールを実画面確認する必要あり。
2. 法務・労務：制度の違い・申請条件・個人情報の共有範囲が誤解を招かないか。医療：診断や介護の必要性を独自判定していないか。税務：賃金・給付の税務扱いや手取りを断定していないか。専門家レビューは未実施のまま。
3. 生成画像の人物・手の自然さ、第三者との類似、利用先規約の最終確認。架空人物のイメージと表示済み。
4. 公開する場合は別途承認後、正式パス移動・noindex解除・実際の日付・sitemap・台帳・公開導線を一括同期して再検証。今回は確認待ちで停止。

## 下書き時点の変更ファイル一覧

- `docs/seo/work-care-consultation-preparation/article-draft.txt`
- `docs/seo/work-care-consultation-preparation/image-details.txt`
- `docs/seo/work-care-consultation-preparation/implementation-review.md`
- `drafts/work-care-consultation-preparation/index.html`
- `public/images/shukatsu/work-care-consultation-preparation-hero-1600.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero-640.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero-960.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero.png`
- `public/images/shukatsu/work-care-consultation-preparation-ogp.webp`
- `docs/seo/content-inventory.csv`
- `docs/seo/editorial-calendar.csv`
- `docs/seo/internal-link-map.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/source-policy.md`
- `docs/seo/ymyl-review-queue.md`

## 2026-11-21 公開準備での検証・制約

- 最新origin/mainは開始時と同じ6b0576b。未完了PRに本記事の重複なし。
- 公開用HTMLへの移動・noindex解除・Article日付・本文日付・台帳・sitemap・公開導線を同期し、原稿31ブロックの保持を再照合。
- node tools/check-site.js：PASS（HTML62件、内部リンク2075件）。node tools/check-click-tracking.js：PASS。git diff --check：PASS。
- コミット後に共通ハーネスを実行し、SHAに対応する証跡をリポジトリ外に保存する。結果はPR本文に記載。以前のblockedは未コミット時点の履歴であり、今回の合格根拠として流用しない。
- package.json・ビルド/lint/型設定は存在せず対象外。PC/スマホ実画面はローカル環境制約により未実施。公開後のHTTP・画像・metadata・導線確認を別途行い、結果をPRに記録する。
- 専門家レビュー未実施・制度条件の個別確認・画像の最終判断は、出典確認の完了や公開承認とは区別して保持する。

### 公開準備での全変更ファイル

- `column/work-care-consultation-preparation/index.html`
- `docs/seo/work-care-consultation-preparation/article-draft.txt`
- `docs/seo/work-care-consultation-preparation/image-details.txt`
- `docs/seo/work-care-consultation-preparation/implementation-review.md`
- `public/images/shukatsu/work-care-consultation-preparation-hero-1600.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero-640.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero-960.webp`
- `public/images/shukatsu/work-care-consultation-preparation-hero.png`
- `public/images/shukatsu/work-care-consultation-preparation-ogp.webp`
- `docs/seo/automation-state.json`
- `docs/seo/content-inventory.csv`
- `docs/seo/editorial-calendar.csv`
- `docs/seo/internal-link-map.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/run-log.md`
- `docs/seo/source-policy.md`
- `docs/seo/ymyl-review-queue.md`
- `index.html`
- `parent-shukatsu/index.html`
- `sitemap.xml`
