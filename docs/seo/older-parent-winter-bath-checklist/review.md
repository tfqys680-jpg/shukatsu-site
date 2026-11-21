# 冬の入浴準備記事 — 実装と公開記録

2026年11月21日（日本時間）。運営者が公開・デプロイ・コミット・プッシュ・PR・マージを明示承認。正式記事をcolumnへ移動し、公開日・最終更新日を2026-11-21に設定、index/follow、sitemapとトップ/ハブ導線、SEO台帳を同期した。公開処理の実際の成否はPR・Actionsと本番レスポンスで確認する。

以下は先行するローカル下書き作成時点の履歴。操作禁止・未定日付・未公開という記述は当時の状態であり、上記公開承認と今回の実装更新で置き換えられる。harness-report.json/harness-summary.mdも下書き時点の証跡であり、公開版の最終証跡ではない。公開版はコミット後のクリーンな状態でハーネスを再実行し、PRに結果を記録する。

## 作業対象と既存変更の保護

- GitHubのmain `6b0576b1a4c7439a04e39a179d608fdd6f7697ff` と作業コピーのHEADが一致することを確認。
- 別セッションの未コミット変更（介護と仕事の記事・SEO台帳・画像）を発見したため、その作業コピーは編集せず独立コピーを作成した。
- 作業場所：`/workspace/scratch/c7943e631b1c/shukatsu-site`。
- ブランチ：`codex/older-parent-winter-bath-draft`。コミットなし。
- AGENTS.md、CLAUDE.md、README、SEO戦略・出典方針、共通ハーネス、既存記事・下書きテンプレート・CSS・JS・検証実装を確認。package.json・ビルド・lint・型チェック専用設定なし。手書き静的HTMLと既存検証を利用。
- 同一テーマの未完了PR検索で該当なし。ただしGitHubの検索対象に含まれない外部原稿・未共有作業は確認不能。

## 検索意図の照合

| 既存ページ | 既存の中心意図 | 本稿との区別 |
|---|---|---|
| /parent-shukatsu/living-alone/ | 合鍵・安否確認・孤立防止・転倒予防 | 本稿は冬の入浴前の環境・声かけ・連絡に限定 |
| /column/obon-family-planning-talk/ | 帰省で終活の話を切り出す | 本稿は入浴準備という個別場面 |
| /column/parents-home-old-appliance-safety-checklist/ | 古い家電の点検・使用中止・相談 | 本稿は入浴環境と本人の希望の整理 |

同じ検索意図のページは確認されず、新規下書きが可能と判断。既存本文の統合・削除はしていない。上記ページは本稿から関連リンク。非公開のため既存公開ページから本稿への導線は追加していない。

## 原稿・公開制御・SEO

- `drafts/older-parent-winter-bath-checklist/index.html` に実装。
- article-draft.txtの本文、H2 3件・H3 6件、チェック6件、FAQ3件、CTA、出典、注意事項を省略せず反映。SEO指定はmetadataへ。原稿全文は同ディレクトリのarticle-draft.txtへ保全。
- news-brief.txtは記事・管理原稿へ取り込んでいない。
- 公的助言と会話例・分担・チェックリスト等の編集提案を明示。一般情報・個別判断の境界、医療職への相談、服薬を自己変更しないこと、事故予防・安全を保証しないことを表示。専門家監修未実施。
- 医療・法務・税務に関する原稿の人手確認項目を保持。架空のサービス・監修・相場・安全保証なし。
- robots=`noindex, nofollow`。sitemap非掲載。公開導線なし。noindexは認証やアクセス制限ではない。mainへ取り込むとGitHub Pagesの配信対象になるため、本作業では取り込まない。
- canonical・og:url・Article/mainEntityOfPage・BreadcrumbListは既存下書き方式どおり将来の正式URL `https://shukatsu-guide.jp/column/older-parent-winter-bath-checklist/` に統一。現時点でそのURLの配信は作成していない。
- title・description・OGP/Twitter、Article、BreadcrumbList、本文と一致するFAQPageを設定。専門職による監修を構造化データに追加していない。
- datePublished/dateModifiedは未設定、本文の公開日・最終公開更新日は未定。2026-11-16は公式資料の更新日、2026-11-21は原稿・出典確認日として区別。公開時に実際の日付で一括同期する。
- content-inventoryはdrafts URLと下書き状態、keyword-mapは正式予定URLと下書き状態。公開日・最終実質更新日欄は空欄。sitemap.xmlは無変更。

## 画像

指定PNGを `public/images/shukatsu/older-parent-winter-bath-hero.png` に配置。ZIP原本とのバイト一致を確認。1672×941px、2,049,523 bytes。別画像の生成・外部取得はなし。

既存のPillow WebP（quality82/method6）方式で全画面を縮小。トリミングなし。

| 変換ファイル（images/） | 寸法 | サイズ |
|---|---|---|
| column-older-parent-winter-bath-checklist-800.webp | 800×450 | 25,820 B |
| column-older-parent-winter-bath-checklist-1200.webp | 1200×675 | 50,018 B |
| column-older-parent-winter-bath-checklist.webp | 1600×900 | 75,590 B |

- picture/sourceでWebPのsrcset（800/1200/1600w）とsizes（最大表示724px、狭幅は100vw−36px）。PNGは指定実パスでフォールバック。
- 指定alt、width=1672/height=941、aspect-ratio=1672/941、width:100%、height:auto、object-fit:containで領域確保。端数丸め以外の構図変更なし。人物を切らない。
- ファーストビュー付近のヒーローをLCP候補と判断しloading=eager・fetchpriority=high・decoding=async。lazyは不使用。
- OGP・Twitter・Article imageは1600px WebP。画像を目視し、着衣の母娘・脱衣所入口・不審な文字やロゴが目立たないことを確認。生成AIの架空人物・家庭と表示。
- CLS対策のマークアップを検証。実ブラウザのCLS/LCP値、SNSクローラの画像取得・切り抜き、実スマホでの人物表示は未確認。

## 出典照合

2026-11-21に検索・ページ取得で公式本文を確認。

1. 新潟県 https://www.pref.niigata.lg.jp/sec/kenko/heatshock.html ：2026-11-16更新、脱衣所・浴室を暖めること、41℃以下・10分までの目安、同居者への声かけ、独居時の扉そばの携帯電話、服薬と入浴、事故時の救急要請を確認。
2. 厚生労働省 https://kakarikata.mhlw.go.jp/kakaritsuke/urgency.html ：救急車の呼び方・意識や呼吸の状況を伝えること・指令員の指示に従うことを補足照合。原稿の救急案内は維持し、補足出典を追加。

個別の病状・服薬の適切な時間・家族ごとの対応可否は判定していない。

## 検証結果

| 検証 | 結果 |
|---|---|
| node tools/check-site.js | 成功：HTML62、内部リンク2077。タグ・JSON-LD・FAQ/パンくず一致・sitemap等 |
| node tools/check-click-tracking.js | 成功（既存GA・main.js方式を維持） |
| python3 tools/agent-harness/test_runner.py | 成功：4テスト |
| python3 tools/agent-harness/run.py | **blocked**：全3チェック成功。ただしdirty_before/after=trueのため総合合格ではない。コミット禁止の指示に従い未コミットを維持 |
| 原稿全文とHTMLの照合 | 成功：本文・全見出し・チェック・FAQ・CTA・出典・注意事項の文字列一致 |
| PNG原本・srcset全参照・CSV列数・日付未設定・noindex確認 | 成功 |
| git diff --check | 成功 |
| build / lint / 型チェック | 専用設定なし。実行済みとはしない |
| PC/スマホ（320/375/390/1280px）の表示・FAQ開閉・CTA実操作 | **未実施**。ローカルChromiumはsocket生成がOperation not permittedで起動不可。クラウドブラウザも127.0.0.1への接続拒否。成功扱いにしない |
| 内部リンクのHTTP応答・外部リンク全件HTTP検査 | 未実施。内部リンク先のファイル・アンカー存在は既存検証で確認。出典の公式本文は取得済み |

共通ハーネスの最終report.jsonとsummary.mdを同フォルダのharness-report.json/harness-summary.mdに保存。対象HEADは上記SHAであり、今回の差分はその上の未コミット作業ツリー。初回はGA定義を省いた下書きがクリック検証で失敗したため、既存方式を復元し最終実行で全3チェック成功。検証コードの条件を緩めていない。

## 人手確認・未確認事項

- PCとスマホ幅で人物の見え方、本文・目次の読みやすさ、FAQ3件の開閉、CTAと関連記事への実遷移を確認する。
- 主治医への個別相談と一般的な目安が混同されないか、本人意思・プライバシーへの配慮が十分か確認する。医療・法務・税務の専門家レビューは未実施。
- 生成画像の指・人物の自然さ、第三者との類似、利用先規約の最終判断は運営者確認。
- 公開時は別途指示を受け、正式ルートへの移動、日付、noindex解除、公開導線、各SEO台帳とsitemapを同期し再検証する。今回は確認待ちで停止。

## 変更ファイル一覧（14ファイル）

- `docs/seo/content-inventory.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/source-policy.md`
- `docs/seo/ymyl-review-queue.md`
- `docs/seo/older-parent-winter-bath-checklist/article-draft.txt`
- `docs/seo/older-parent-winter-bath-checklist/harness-report.json`
- `docs/seo/older-parent-winter-bath-checklist/harness-summary.md`
- `docs/seo/older-parent-winter-bath-checklist/image-details.txt`
- `docs/seo/older-parent-winter-bath-checklist/review.md`
- `drafts/older-parent-winter-bath-checklist/index.html`
- `images/column-older-parent-winter-bath-checklist-1200.webp`
- `images/column-older-parent-winter-bath-checklist-800.webp`
- `images/column-older-parent-winter-bath-checklist.webp`
- `public/images/shukatsu/older-parent-winter-bath-hero.png`
