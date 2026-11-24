# 川崎市終活情報登録：下書き実装時点の確認報告（履歴）

> 公開承認後の更新：ユーザーは同日、公開・デプロイ・コミット・プッシュ・PR作成・マージを指示。記事は `/column/shukatsu-information-registration-checklist/` へ移動し、公開日・更新日・台帳・sitemap・導線を同期した。以下は承認前の実装履歴であり、現在の公開状態ではない。最終の検証証跡はPR本文を参照。

2026年11月24日（日本時間）。未公開・確認待ち。公開、デプロイ、コミット、プッシュ、PR作成、マージは未実施。

## 設置先と予定URL

- 下書き：`drafts/shukatsu-information-registration-checklist/index.html`
- 予定URL：`https://shukatsu-guide.jp/column/shukatsu-information-registration-checklist/`（未公開）
- 元原稿：同じディレクトリの `article-draft.txt` をバイト一致で保存。
- 静的HTMLサイト。package.json、ビルド処理、lint/型チェック専用コマンドは存在しない。既存方式のCSS、ナビ、FAQ details、js/main.js、Google tagに合わせた。
- 最新main fd7d484806d0415495a442c1782cbc244193a348から新規チェックアウト。開始時git status空。他セッションの既存変更は触っていない。GitHubの同題open PR検索は0件。

## 重複判断

比較対象は `/column/end-of-life-local-support-consultation-checklist/`（奈良市を例にした支援・相談先・契約・費用）、`/column/ohitorisama-shukatsu-checklist/`（一般的な準備シート）、`/column/mimoto-hosho-keiyaku-checklist/`（契約前確認）。
既存記事への川崎市の紹介追記も検討したが、今回の中心は川崎市の対象・申請・同意・照会・変更であり、奈良市とは申請方法や対象が違う。既存記事の地域条件に混在させず新規下書きとして用意。遺言・ACP・契約の詳細解説は増やさず既存記事への内部リンクで補完。水増しの地域展開や既存記事削除・統合はしていない。公開前に検索意図の分担を再確認できる状態。

## 公式資料確認と原稿からの差分

本文・メタ・H2/H3・チェックリスト7件・FAQ3件・CTA・出典1〜5を原稿から取り込み。news-brief.txtは本文に使用していない。公式案内と社協説明書を出典6〜7として補足。

- 発表2026-11-12、開始2026-11-16。要綱の制定・施行2026-10-01とは区別。
- 市内居住、年齢制限なし、無料、希望項目のみ。全国一律と説明しない。
- 本人または成年後見人が申請。未成年者は法定代理人の同意。保佐人・補助人は申請不可。
- 連絡先の同意書、本人確認書類、成年後見人の登記事項証明、住所相違時の居住確認資料を公式条件として補足。メモ作り・整理手順は編集提案として分離。
- 照会を受けて回答する方式。指定した家族等の照会には開示請求書と身分確認が必要。登録だけで見守り・自動通報・遺言・医療同意・葬儀発注・死後事務委任が成立するとは記載しない。
- 変更申請、市外転出時の廃止を確認。
- 報道発表資料・社協説明書は平日8:30〜17:00、土日祝・年末年始除外。市Web本文の申請先も8:30。一方、同ページ末尾の問い合わせ欄は9:00。本文は一次資料の8:30を維持し、不一致と窓口への最新確認を出典欄に明記。

確認URL：

1. https://www.city.kawasaki.jp/templates/prs/350/0000191619.html
2. https://www.city.kawasaki.jp/templates/prs/cmsfiles/contents/0000191/191619/jouhoutouroku-syuukatu.pdf
3. https://www.city.kawasaki.jp/templates/outline/cmsfiles/contents/0000191/191367/syukatsujouhoutourokuyoukou-.pdf
4. https://www.mhlw.go.jp/acp-jinseikaigi/about/
5. https://csw-kawasaki.or.jp/senior-info/end-of-life/
6. https://www.city.kawasaki.jp/350/page/0000191344.html
7. 社協終活支援ページにリンクされた「取扱説明書」PDF（原稿に正確なURLを設定）。

公式PDFの初回直接取得は失敗したが、公式ページからのリンク経由で報道資料・要綱・社協説明書の本文を取得し照合。一般情報の照合であり、専門家監修ではない。

## 画像

共通配置先：`public/images/shukatsu/`。静的サイトではこのパスがそのまま配信パスになるため `/public/images/shukatsu/` で参照。

| ファイル | 実寸 | 用途 |
|---|---|---|
| shukatsu-information-registration-hero.png | 1672×941 | 添付PNG原本・変更せず保存 |
| shukatsu-information-registration-hero-640.webp | 640×360 | モバイル |
| shukatsu-information-registration-hero-1200.webp | 1200×675 | 標準・高密度 |
| shukatsu-information-registration-hero-1600.webp | 1600×900 | 高密度 |
| shukatsu-information-registration-ogp.webp | 1200×630 | OGP・Article image |

Pillowで派生画像を生成。元の縦横比を維持（整数丸めのみ）。OGPは元画像を全体縮小し左右に余白を付け、顔・手・ノートをトリミングしない。原本とOGPを目視確認済み。
altは指定文と完全一致。figure/figcaptionで生成AIのイメージと表示。width/height=1672/941、aspect-ratio、sizes=(max-width:760px) calc(100vw - 36px), 724px、srcset=640w/1200w/1600w。fetchpriority=high、lazyなし、decoding=async。実ブラウザの候補選択・CLS/LCP測定は未実施。

## SEO・公開防止・アクセシビリティ

- title/H1/og:title/Article headline一致、description/OGP/Article description一致。
- canonical・og:url・Article mainEntityOfPageは予定正式URL。下書きでは既存方式のnoindex。
- Article、BreadcrumbList、FAQPageを既存方式で実装。FAQ表示とJSON-LDを既存チェックで照合。検索結果でのFAQ表示は保証しない。
- 実際の初回公開日が未定のためdatePublished/dateModifiedと公開台帳の日付は空欄。本文では原稿作成・確認日と公開日を区別。
- sitemap.xmlは確認したうえで変更なし。未公開なので追加しない。公開一覧・公開記事からの導線なし。公開時に移動、noindex解除、日付・sitemap・台帳・公開導線の更新が必要。
- エンディングノート、遺言、身元保証/死後事務、ACP、自治体支援の記事は実在確認してリンク。外部出典/CTAはtarget=_blank、rel=noopener noreferrer。架空の監修者・資格・相談サービス・実績は追加しない。
- h1は1件、H2→H3の順序。FAQはキーボード操作可能な標準details/summary。明示的なfocus-visibleを追加。実表示と操作確認は下記の理由で未完了。

## チェック結果

| チェック | 結果 |
|---|---|
| node tools/check-site.js | PASS：HTML65、内部リンク2193。リンク/アンカー、構造化データ、FAQ、パンくず、sitemap/台帳整合等 |
| node tools/check-click-tracking.js | PASS：既存CTA等の計測回帰なし |
| python3 tools/agent-harness/test_runner.py | PASS：4テスト（ハーネス内で実行） |
| 共通ハーネス | 3検査PASS、全体blocked：ユーザーのコミット禁止に従った未コミット変更があるため |
| git diff --check | PASS（CSV追記の改行をLFへ統一） |
| ビルド・lint・型チェック | 専用設定なし。手書きHTMLサイトのため該当コマンドなし |
| モバイル320/375/390・デスクトップ・フォーカス | 未確認：PlaywrightからChromium起動時にsocket() Operation not permittedで終了。承認昇格なし |
| 画像・OGPの目視 | PASS：原本と1200×630 OGPで顔・手・ノートを確認 |

## 公開前の人による確認・未解決事項

1. 法務：最新の対象者・同意・申請者・照会手続き・必要書類を確認。遺言や委任契約の効力と混同しない。専門家レビューは未実施。
2. 医療：意向登録を個別の医療同意や治療の自動決定としない。主治医等への確認を案内。専門家レビューは未実施。
3. 税務：登録による税軽減・申告免除の示唆なし。具体的税務説明を加える場合は税務署・税理士へ確認。
4. 公式資料内の8:30/9:00の不一致は、公開直前に窓口で確認する。
5. ブラウザが使える環境で320/375/390pxの表示、フォーカス、メニュー・FAQ操作、画像候補、LCP/CLSを確認する。
6. 画像不足はなし。公開日未定・公開操作未承認。確認待ちで停止。

## 変更ファイル一覧

既存変更：

- docs/seo/content-inventory.csv
- docs/seo/keyword-map.csv
- docs/seo/internal-link-map.csv
- docs/seo/ymyl-review-queue.md
- docs/seo/run-log.md

新規：

- drafts/shukatsu-information-registration-checklist/index.html
- docs/seo/shukatsu-information-registration-checklist/article-draft.txt
- docs/seo/shukatsu-information-registration-checklist/implementation-review.md（この報告）
- docs/seo/shukatsu-information-registration-checklist/verification.json
- public/images/shukatsu/shukatsu-information-registration-hero.png
- public/images/shukatsu/shukatsu-information-registration-hero-640.webp
- public/images/shukatsu/shukatsu-information-registration-hero-1200.webp
- public/images/shukatsu/shukatsu-information-registration-hero-1600.webp
- public/images/shukatsu/shukatsu-information-registration-ogp.webp
