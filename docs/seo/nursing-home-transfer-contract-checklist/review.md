# 老人ホームの退去条件の記事：ローカル実装の確認記録

作業日：2026-11-22（日本時間）。ベースmain：577caca281ff42391e79507529a2f6ca27a3a059。新規取得直後のgit statusはクリーン。既存の作業差分なし。GitHubの未完了PR検索（対象語・全件）で該当なし。

## 実装

- 未公開ページ：`drafts/nursing-home-transfer-contract-checklist/index.html`。
- 公開予定のcanonical：`https://shukatsu-guide.jp/column/nursing-home-transfer-contract-checklist/`。現時点で本番ページを新設していない。
- 既存は手書き静的HTML・GitHub Pagesのルート配信。package.json、ビルド、lint、型チェック設定は未導入。そのため新規のフレームワークや管理方式は作成しない。
- 最新の職場相談記事と既存draftsの記事をテンプレートとして参照。共通CSS・JS・ヘッダー・フッターを使用。原稿全文・FAQ3件・CTA・調査対象・期間・注意事項を維持。news-briefは未使用。
- noindex、公開日未定。Articleの日付は未設定。原稿日を公開日に流用しない。sitemap・トップ・ハブ・既存公開ページは未変更。
- SEOタイトル・description・canonical・OGP・Article・BreadcrumbListを実装。FAQPageはサイト既存方針に従って可視FAQと同じ内容で設定。検索表示・リッチリザルトは未検証で保証しない。
- 架空の監修者・相談窓口・配布サービスを追加していない。既存サイト共通の運営者表示を継承し、本文には専門家監修未実施を明示。

## 重複確認と追記案

| 既存記事 | 重なる点 | 今回の差分・有用な追記案 |
|---|---|---|
| column/housing-type-nursing-home-registration-checklist/ | 医療対応・退去条件・前払金・書面確認 | 既存は住宅型の登録制と10項目の全体像。今回の中心は長期入院中の居室と料金・復帰手続き、本人の解約と施設の解除の区別、居室変更、連絡順。既存sec3へ「入院後の復帰条件」「返還と別請求の計算例」を短く追記して今回記事へ誘導する案が有用。公開前の配置判断待ちで既存記事は変更していない。 |
| column/senior-housing-registration-operation-checklist/ | 夜間体制・費用・入院中/退去時費用 | 既存はサ高住の登録/運営情報の読み方。今回は個別契約の退去・住み替えの確認手順。登録情報では不明な復帰条件は契約書で確認する補足と相互リンクが候補。 |
| column/care-facility-food-housing-cost-application-checklist/ | 施設費用 | 既存は食費・居住費の負担軽減申請。退去精算とは検索意図が異なるため関連記事として案内。 |

新規公開の最終判断前に上記の重なりを確認する。既存ページの削除・統合・書き換えは未実施。

## 画像

原本：`public/images/shukatsu/nursing-home-transfer-contract-hero.png`。ZIPとバイト一致、1672×941px、2,177,898 bytes。原本を維持しPillowでWebP（quality 82、method 6）へ変換。わずかな比率調整以外は中央切り抜き、拡大なし。

| 配信用 | 寸法 | bytes |
|---|---|---:|
| hero-1600.webp | 1600×900 | 96,630 |
| hero-1200.webp | 1200×675 | 63,368 |
| hero-640.webp | 640×360 | 24,022 |
| ogp.webp | 1200×630 | 70,974 |

上記は共通の `nursing-home-transfer-contract-` 接頭辞。指定altを設定。width/height・srcset/sizes・eager・fetchpriority=high・decoding=asyncを設定。本文幅724px、狭い画面は画面幅から余白36pxを引く。顔や手を不自然に切らない構図とOGPを目視。AI生成の架空の場面であることを本文画像直下に表示。LCP候補の見出し・画像・メタ・注記は既存JSの登場演出で隠さないよう記事限定CSSを追加。共通CSS/JSは未変更。

## 出典

2026-11-22に原文照合。[1]の公表日・集計対象・集計期間・約1割を確認。全国の転居率とは記述しない。[2]の重要書類・返還・入院等の不在時・居室変更・契約解除・原状回復・相談窓口を照合。[3]はHTTP200、PDF34,831,974 bytesを取得し、PDF65頁を画像として目視。正確な収録元・対象頁をリンクに補足。2020年の背景資料であり、最新法令や個別契約への適用を証明する資料ではない。本文に返還割合・期限・税控除等の断定を追加していない。

- https://lifull.com/news/50786/
- https://www.mhlw.go.jp/content/12300000/001481759.pdf
- https://www.mhlw.go.jp/content/12300000/001259210.pdf#page=65

## 検証

- 作業前：既存check-site・check-click-tracking成功。
- 最終check-site：HTML64件、内部リンク2149件、全成功。リンク・アンカー・タグ整合・JSON-LD構文・FAQ/パンくずDOM整合・title/H1・sitemap非混入を検査。
- 最終check-click-tracking：成功。下書きも検査対象のため既存のgtag定義を維持。初回のgtag欠落失敗は修正済み。
- ハーネス回帰テスト：4件成功。最終ハーネス内の3チェックはいずれもpassed。ただし未コミット差分を保持しているため総合statusはblocked。コミット禁止のユーザー指示を優先し、コミット後のSHA検証は未実施。合格や公開可能とは報告しない。
- 原稿の導入・H2/H3・本文・チェックリスト・FAQについて行単位の欠落なし。原稿・画像のバイト一致、CSV列数、sitemap非掲載も確認。
- クラウドブラウザーでローカルプレビューを確認。320/375/390pxのiframe幅（スクロールバーを除いた実表示幅305/360/375px）で横はみ出しなし。PC表示幅724pxで画像の読込・構図を確認。FAQの展開と回答表示を確認。
- srcset全候補とOGPを実ファイルとして確認し、ブラウザーで本文画像の読込を確認。見出しはH1一つ、H2/H3の順序。代替テキスト、寸法予約、画像LCP対策を実装。Lighthouse/Web Vitalsの実測値、外部SNSのOGPクロール、本番URLのHTTP/検索登録は未検証。
- 既存公開HTML・CSS・JS・sitemapの差分なし。追加した下書きと管理資料のみがサイト検証対象の差分。プレビュー用コピー・設定は検証後削除。

## 変更ファイル一覧

- drafts/nursing-home-transfer-contract-checklist/index.html
- public/images/shukatsu/nursing-home-transfer-contract-hero.png
- public/images/shukatsu/nursing-home-transfer-contract-hero-1600.webp
- public/images/shukatsu/nursing-home-transfer-contract-hero-1200.webp
- public/images/shukatsu/nursing-home-transfer-contract-hero-640.webp
- public/images/shukatsu/nursing-home-transfer-contract-ogp.webp
- docs/seo/content-inventory.csv
- docs/seo/keyword-map.csv
- docs/seo/ymyl-review-queue.md
- docs/seo/nursing-home-transfer-contract-checklist/article-draft.txt
- docs/seo/nursing-home-transfer-contract-checklist/image-details.txt
- docs/seo/nursing-home-transfer-contract-checklist/review.md
- docs/seo/nursing-home-transfer-contract-checklist/verification-report.json
- docs/seo/nursing-home-transfer-contract-checklist/verification-summary.md

## 残る人の確認事項

1. 本文の表現と既存記事との分担。独立記事で公開するか、上記の追記案として活用するか。
2. 施設種別・契約・最新法令/経過措置による違い。医療対応・看取り・返還・税務について個別判断を保証しない表現になっているか。専門家による審査は未実施。
3. AI画像の手・顔・人物類似、生成サービス利用条件とサイト表示方針。人物・施設の取材写真や推薦の誤認がないか。
4. 正式な公開日と公開操作の承認。現時点では全て未実施。

## 承認後に行う公開手順（今回は実行しない）

draftsからcolumnへ移動、noindex解除、実際の公開日/更新日を確定して本文・Articleに同期。sitemap、トップ/ハブ、content-inventory、keyword-map、必要な内部リンク管理を同期。既存記事との相互リンクは重複判断後に追加。必要な検証とコミット後ハーネス、差分レビューを実施してから公開手順へ進む。

今回は公開・デプロイ・コミット・プッシュ・PR作成・マージを一切行っていない。

## 2026-11-22 公開準備への移行

上記は前回のローカル下書き時点の記録。今回ユーザーが公開・デプロイ・コミット・プッシュ・PR・マージを明示承認したため、columnへ移動し、noindex解除、実際の公開日を2026-11-22として記事と台帳・sitemapへ設定。トップ新着3本・全記事一覧・ハブ・既存登録制記事から導線を追加。原稿・生成画像・注意事項・専門家未監修の表示は維持。最新の検証証拠はPRに記録する。
