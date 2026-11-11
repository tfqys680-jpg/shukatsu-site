# 公開用実装（2026-11-11）

運営者がコミット・プッシュ・PR作成・マージ・公開を明示承認。記事は `/column/welfare-equipment-trial-checklist/` に移動し、noindex解除、公開日/更新日2026-11-11を設定。トップ・ハブ・sitemap・台帳を更新。[3]専門相談員と選択制、[4]印刷頁3の調整・説明・定期確認を原文照合済み。専門家レビューと実端末CLS実測は未実施。

以下は前段階の下書き検証の履歴。保存済みharness-report.jsonのblockedは未コミット時点の記録で、公開時の結果はPRのCI及び新しい共通ハーネスで確認する。

---

# 福祉用具を試す前に：実装報告

2026-11-11（日本時間）。対象は tfqys680-jpg/shukatsu-site のみ。
基準main: `4aacf46e20561e99ff04272a71986139d062295e`。
ローカル未コミットの下書きとして実装。コミット・プッシュ・PR作成・マージ・デプロイ・公開は実施していない。

## 判断と実装

新規追加。keyword-mapと既存記事を確認し、「福祉用具を試す前の準備・質問・導入後の相談」は介護費用軽減、在宅看取り、住宅選び、一人暮らしの見守りとは検索意図が異なると判断。同名slugのPR検索結果は0件。

- 下書き: `drafts/welfare-equipment-trial-checklist/index.html`
- 公開予定URL: `https://shukatsu-guide.jp/column/welfare-equipment-trial-checklist/`（今回未追加・未公開）
- 原稿本文、質問例、7項目チェックリスト、FAQ3件、CTA、出典4件、人手確認事項を反映。本文・FAQ・チェックリストを原稿の各行と照合し、欠落0件。
- article-draft.txt全文とimage-details.txtを本ディレクトリへ原文保全。原稿のSEO指示はメタデータ、画像案は同梱画像とalt、実装指示は適切な実装・管理情報として使用。news-brief.txtは本文に不使用。
- 既存の静的HTML・共通CSS・ヘッダー/フッター・FAQ開閉に従う。グローバルCSS/JS変更なし。
- title、description、canonical、OGP/Twitter画像、Article、BreadcrumbListを設定。未確認の監修者は追加していない。
- 直近の参考記事と同様、FAQは表示のみでFAQPageは付与しない。一般情報サイトとしてリッチリザルト適格性を確認できず、表示も保証しない。
- 介護ガイド、住まい・見守りガイド、終活チェックリスト、相談窓口への実在リンクを設定。無料相談・販売・専門家紹介の提供約束なし。
- drafts/の既存方式に従いnoindex。公開日/更新日は未定、ArticleのdatePublished/dateModifiedは未設定。canonical等は公開予定URLを用いる既存下書き方式。
- sitemapを確認し非掲載を維持。公開ページからの下書きへの導線は追加していない。content-inventoryとkeyword-mapを下書き状態で追加、YMYLキュー・出典台帳を更新。管理方式の新設なし。

## 画像

| ファイル | 寸法 | バイト数 |
|---|---|---:|
| public/images/shukatsu/welfare-equipment-trial-hero.png | 1672×941 | 2,335,890 |
| images/column-welfare-equipment-trial-800.webp | 800×450 | 44,358 |
| images/column-welfare-equipment-trial-1200.webp | 1200×675 | 82,188 |
| images/column-welfare-equipment-trial-1600.webp | 1600×900 | 124,556 |

Pillow、Lanczosリサイズ、WebP quality=82/method=6。1600px版は元PNG比94.7%削減。
元PNGは無変更で保全し、入力とのバイト一致を確認。SHA-256:
`a7da92ebb3e7dd61ca15df39a0f5bbdd140054b5cf9131faaac1e96d65d559a1`

picture/sourceのsrcset（800/1200/1600w）とsizesを既存記事に合わせて設定。PNGをフォールバックに使用。width/heightとaspect-ratioで領域確保、eager/fetchpriority=high/async。人物をトリミングせず、OGPも同画像の1600×900 WebPを使用。指定altを設定し、AI生成・架空人物・イベント実写や仕様図ではない旨を表示。画像目視では明瞭な文字・ロゴや顔の切断を認めない。人物や用具の技術的正確性・権利関係を保証するものではない。

## 検証

| コマンド・確認 | 結果 |
|---|---|
| node tools/check-site.js | 成功。HTML59件・内部リンク2007件。タグ・アンカー・JSON-LD・パンくず・sitemap等 |
| node tools/check-click-tracking.js | 成功（共通ハーネス内実行）。公開HTML55件・affiliate38件・CTA13件・products12件 |
| python3 tools/agent-harness/test_runner.py | 成功（共通ハーネス内実行）。4テスト |
| python3 tools/agent-harness/run.py --output /workspace/scratch/5b0988c03563/equipment-harness | 個別3チェック成功、総合blocked。未コミット変更があるため。ユーザーのコミット禁止を優先し、合格扱いしていない |
| git diff --check | 成功 |
| build / lint / 型チェック | package.json及び専用コマンドなし。静的HTMLでビルド工程なし。未定義のため未実施 |
| 原稿照合 | 本文・FAQ・チェックリスト欠落0、元原稿も全文保全 |
| 画像・srcset | 全ファイル存在、ブラウザでWebP選択と読み込みを確認 |
| PC/モバイル | ローカルChromeのiframe表示幅1280・320・375・390pxで確認。スクロールバー幅15pxを含む。全幅でscrollWidth=clientWidth、横はみ出しなし。PCと3幅の画像・見出し目視、FAQ開閉確認 |
| CLS | width/heightとaspect-ratioの領域確保を確認。CLSスコア・実端末・低速回線の実測は未実施 |

共通ハーネス記録: harness-report.json / harness-summary.md。対象SHAは基準mainであり、未コミット変更込みの検証である点に注意。

## 残課題・公開前の確認

1. 専門家レビューは未実施。法務・制度：保険対象、選択制、申請、契約・返品・修理条件。医療介護：PT/OT/福祉用具専門相談員等による安全・適合表現の確認。税務：控除・非課税を加筆する場合に税理士等が要件確認。
2. 一次資料は中野区イベント原文と厚労省PDF[2]の改訂説明を照合済み。[3]総合ページのリンク先詳細照合、画像PDF[4]の本文目視照合は未完了。取得成功と内容確認済みを区別する。
3. 公開直前に開催状況を再確認。2026-11-13の終了後は「予定」を過去の案内事例に変更し、実際に開催されたと無確認で断定しない。下書きの公開手順コメントとYMYLキューにも記録。
4. 公開承認後に実際の日付確定、column/移動、noindex解除、sitemap/公開導線/台帳を更新する。今回これらの公開操作は行わない。
5. 実端末CLS/LCPとSNS側のOGP表示確認は未実施。現在のOGP URLは未公開ファイルを指す公開準備設定。

## 変更ファイル一覧

- `docs/seo/content-inventory.csv`
- `docs/seo/keyword-map.csv`
- `docs/seo/source-policy.md`
- `docs/seo/welfare-equipment-trial/article-draft.txt`
- `docs/seo/welfare-equipment-trial/harness-report.json`
- `docs/seo/welfare-equipment-trial/harness-summary.md`
- `docs/seo/welfare-equipment-trial/image-details.txt`
- `docs/seo/welfare-equipment-trial/implementation-report.md`
- `docs/seo/ymyl-review-queue.md`
- `drafts/welfare-equipment-trial-checklist/index.html`
- `images/column-welfare-equipment-trial-1200.webp`
- `images/column-welfare-equipment-trial-1600.webp`
- `images/column-welfare-equipment-trial-800.webp`
- `public/images/shukatsu/welfare-equipment-trial-hero.png`
