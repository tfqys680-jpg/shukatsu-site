# 実行ログ（run-log）

## 2026-08-17（週次・定期実行）

- 実行日時: 2026-08-17 09:18 JST（Asia/Tokyo。無人の定期実行）
- ブランチ: claude/seo-weekly-2026-08-17（新規ドラフトPR運用）
- 事前確認: git status（クリーン）／origin/main最新化（a8a92a3）／CLAUDE.md（リポジトリに存在せず）／docs/seo配下の管理ファイル一式／既存ブランチ・オープンPRを確認（オープンPRなし。重複作業なし）
- **管理ファイルのドリフトを検出**: 前回記録済みの実行（2026-08-10）以降、run-log.md・automation-state.jsonに記録のないまま55件のコミットがmainへ反映されていた（配色をローズ系→ブルー系パステルへ刷新、Polletアフィリエイト（/ihin-kaitori/）の削除、カスタム404ページの追加、column/legacy-giving-basics・column/obon-family-planning-talkの新設、GA4クリック計測の共通化、17ページへのBreadcrumbList構造化データ追加、新着記事セクションの独立化など）。いずれも別セッション経由（運営者からの直接依頼、または別のチャットセッション）でのマージと推測されるが、この定期実行の管理ファイルには反映されていなかった。`node tools/check-site.js`は全通過しておりサイト自体の技術的な健全性に問題はなかったため、優先順位1（サイト全体の障害）に該当する事象はなし。ただし content-inventory.csv・internal-link-map.csv が実際の公開状態と乖離していた（削除済みの/ihin-kaitori/を「公開」と記載、legacy-giving-basics・obon-family-planning-talkの行が欠落）ため、今回あわせて是正した（下記「管理ファイル更新」参照）。run-log.mdへの過去分の遡及的な完全記録（55コミット全件）は今回の1回では対応しきれないため、次回以降の各実行時に気づいた範囲で補完する方針とする
- 判定: 編集カレンダーの2026-08-17〜21週分は「親の終活を兄弟姉妹で進める役割分担（新規）」の1タスク。優先順位（本プロンプト3章、公開予定どおりの親の終活クラスタ新規記事）に該当し、期限どおりの週のため今回実施。前回大幅更新（2026-08-10 article05）から14日未経過だが、これは新規記事であり隔週の既存記事更新枠とは別のため対象。前回新規記事（2026-08-04 article18、運営者指示の臨時追加）からは13日経過
- 実施した作業:
  - `/parent-shukatsu/siblings/index.html` を新規作成（親の終活ハブのFAQ・状況別ケースで「準備中」としていた記事）:
    - 進め方の大原則3つ（親に話す前に足並みをそろえる／情報を持つ人を先に決める／平等ではなく時間・距離・得意分野で持ち寄る）
    - 役割の決め方3パターン（距離で分ける・得意分野で分ける・当番制にする）と、役割分担の具体例一覧表（情報の一元管理係・通院同行係・お金の記録係・連絡係・遠方サポート係・緊急連絡係）
    - 立て替え費用を「言った言わない」にしないための記録表（日付・項目・金額・立て替えた人・精算状況・領収書。記入例つき、印刷・コピーして使える書式）
    - 連絡ルールの決め方（手段を1つに絞る・頻度を決める・緊急連絡網）、話し合いを切り出す会話例3パターン、よくある失敗例5つ、状況別ケース5つ（遠方のきょうだい・ワンオペ状態・疎遠な関係・配偶者の関与・きょうだいがいない場合）
    - 専門家へ相談する境界線（財産分けの話が出たらarticle07/10へ、相続手続きが必要になったらarticle15へ、対立が深刻な場合は弁護士等の第三者へ）、FAQ5問、BreadcrumbList/FAQPage/Article構造化データ
    - 低YMYL区分（家族間コミュニケーションの一般的アドバイスのみで、価格・法制度・統計の記載なし）と判断し、article05と同様に外部一次情報の付与は行っていない。実在しない相談事例・統計は記載していない
  - 内部リンク: トップページ（新着記事セクションへ追加し、最も古かったcolumn/ai-shukatsu-first-step行を運用ルールどおり削除／全記事一覧へ追加）、親の終活ハブ（状況別ケース「兄弟姉妹がいる場合」カード・記事一覧・FAQ Q3の回答を「準備中」から本記事へのリンクに更新）から新規記事へリンク。新規記事側からはハブ・30項目記事・article05・article11・article15へリンク（article05→本記事の逆方向リンクは、article05のdateModifiedを不要に更新しないため今回は見送り、次回の内部リンク整備時に検討）
  - 管理ファイル更新: content-inventory.csv（新規行追加、トップ・ハブのlastmod更新、削除済み/ihin-kaitori/行を削除、article06/12/15/18の陳腐化した「公開(PR中)」表記を「公開」へ修正）、keyword-map.csv（新規行追加、あわせてlegacy-giving-basics・obon-family-planning-talkの欠落行を追加）、internal-link-map.csv（新規記事関連の行追加、/ihin-kaitori/関連4行を削除し削除済みの旨を記載、legacy-giving-basics・obon-family-planning-talkの欠落行を追加）、editorial-calendar.csv（該当タスクを完了に更新）、sitemap.xml（新規URL追加）
- 変更したURL: https://shukatsu-guide.jp/parent-shukatsu/siblings/（新規公開）／https://shukatsu-guide.jp/（新着記事・全記事一覧更新）／https://shukatsu-guide.jp/parent-shukatsu/（状況別ケース・記事一覧・FAQ更新）
- 検索意図: 「親 終活 兄弟姉妹」「終活 役割分担」「親の介護 兄弟姉妹 分担」をカバー。既存記事との検索意図の重複なし（keyword-map.csvで確認）
- 内部リンク: 上記「実施した作業」参照
- 技術変更: BreadcrumbList・FAQPage・Article構造化データを新規追加（DOM↔JSON-LD一致を`node tools/check-site.js`で確認）
- PDF/DOCX変更: なし（費用記録表はページ内の印刷可能な表として提供。独自PDF化は今回見送り、必要性があれば次回以降検討）
- 参考情報: 新規の法制度・統計・固有名詞の追加なし（本記事はアドバイス・会話例中心のコンテンツのため、source-policy.mdへの新規追加なし）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 35, internal links checked: 1041）。canonical（全ページ固有・重複なし）、meta description重複なし、robots.txt正常、意図しないnoindexなし、sitemap.xmlに新規URL反映済み・drafts混入なし、孤立ページなし（新規記事は4か所から被リンク）を個別確認。Playwright（ヘッドレスChromium）でモバイル(390px)・デスクトップ(1280px)のDOM計測（scrollWidth<=clientWidth）により横スクロールが発生しないことを確認し、主要セクション・表のスクリーンショットで表示崩れがないことも目視確認
- Search Console分析: `docs/seo/sc-data/` が引き続き未配置のためデータなし。表示回数・CTR・掲載順位・前月比較は「データ不足」として記録し、数値の推測は行っていない
- 季節需要（6〜10週間後＝2026-09-28頃〜2026-10-26頃）確認: 該当する強い季節需要イベントは秋のお彼岸（9/23、既に対応済みのarticle14の範囲）程度で、この時間軸に新規性の高い季節記事は該当なし。編集カレンダー上、この期間はarticle06のデジタル終活チェックリスト化（2026-09-28〜10-02）・実家の片付け記事（2026-10前半）が既に計画済みのため、今回の追加着手なし
- 編集カレンダー確認: 次回未着手タスクは2026-08-24〜28（一人暮らしの親の終活チェックリスト、新規、/parent-shukatsu/living-alone/）。過去の未完了タスクの新たな遅延なし
- YMYLレビュー待ち: 変更なし（本記事は低YMYL区分のため今回のレビュー対象への追加なし。既存のarticle18/15/07/10/17/30項目記事/column2件の項目は継続）
- 阻害要因: 前述のとおり、2026-08-10〜08-17の間に管理ファイルへ記録されないまま多数のサイト変更が行われていたことを確認した。実際のサイト状態と乖離していた箇所（content-inventory.csv・internal-link-map.csvの/ihin-kaitori/記載、legacy-giving-basics・obon-family-planning-talkの欠落）を是正し、**運営者のご指示により、同日中に遡及記録（上記「2026-08-10〜08-14」セクション）とsource-policy.mdのお盆記事分の台帳追記、article05→本記事の相互リンクまで実施した**。ただし遡及記録は`git log`とサイト実物から復元したものであり、各作業時点での判断根拠・検証内容までは復元できていない
- 追加実施（同日、運営者のご指示による）:
  - `articles/article05.html`: 拒否パターン5（きょうだい不一致型）の本文と関連記事欄から本記事への相互リンクを追加。**軽微なリンク追加のためdateModified・最終更新日は据え置き**（本文を変えず更新日だけを変える行為の禁止、およびその逆に軽微な変更で更新日を偽らない方針に従った）
  - `docs/seo/source-policy.md`: お盆記事の出典5件（国税庁タックスアンサー2件・法務省・民間2件）を台帳へ転記、本記事の「新規一次情報なし」を明記
  - `docs/seo/run-log.md`: 2026-08-10〜08-14の遡及記録セクションを新設
- 次回予定: 2026-08-24週の一人暮らしの親の終活チェックリスト（新規、/parent-shukatsu/living-alone/）に着手予定
- PR: ドラフトPRを作成（PR #32）

### 2026-08-19 追記（同PRへの追加コミット・運営者のご指示による）

- 未参照だった旧アイキャッチ画像 `images/column-legacy-giving-basics.webp` を削除（上記「2026-08-10〜08-14」セクションの残課題を解消）。削除前に参照が`-v2.webp`の3か所のみであることを全文検索で確認済み
- **PR #32 は2026-08-19時点で未マージ**（オープン・ドラフト・mergeable_state=clean・レビューコメントなし）。本番反映はmainへのマージ時にGitHub Pagesが自動デプロイするため、マージの実行は運営者のご判断に委ねている（定期実行プロンプトでも「デフォルトブランチへ直接マージしない」と定めているため、自動運用側からは実行しない）

## 2026-08-10〜08-14（遡及記録：定期実行の記録外で反映された変更のまとめ）

- 記録日: 2026-08-17（週次定期実行時に検出し、事後的に整理したもの）
- 経緯: 2026-08-10の週次実行以降、この定期実行の管理ファイルに記録されないまま、別セッション（運営者からの直接依頼と推測）で **55コミット（マージ含む／実質24コミット）** がmainへ反映されていた。以下は`git log`とサイト実物から復元した内容であり、**各作業時点での判断根拠・検証内容までは復元できていない**（当時のセッションでしか分からないため）。今後の齟齬を防ぐための記録として残す
- 反映されていた変更（テーマ別）:
  - **新規記事3本（すべて`/column/`配下）**: `will-for-ordinary-families`（遺言書はお金持ちだけのもの？／2026-08-10）、`ai-shukatsu-first-step`（AIで終活を始める方法／2026-08-11）、`legacy-giving-basics`（遺贈寄付とは？／2026-08-12）、`obon-family-planning-talk`（お盆に家族で終活の話を始める方法／2026-08-13）※計4本
  - **法務コピーの是正**: 「エンディングノートに法的効力はない」等の断定表現を「それだけでは通常、財産を移す法的効力は生じません」「生前贈与、死因贈与、信託など目的に合う方法を専門家と検討」へ全面的に修正。`tools/check-site.js`に**禁止表現13件と必須表現の回帰防止チェックが追加**されており、以後この表現は自動検出される
  - **YMYL運用方針の変更（2026-08-11、運営者方針）**: 法務に触れるcolumn記事は「運営者が一次情報を読んだ個人の感想・整理」の枠組みで記載し、冒頭・末尾に監修未実施を明記する運用へ。`ymyl-review-queue.md`に反映済み
  - **テクニカルSEO**: BreadcrumbList構造化データを17ページへ一括追加（実装率11/29→28/29）、カスタム404ページ追加、article02のtitle/descriptionに「手順」を追加
  - **計測**: アフィリエイトクリック計測（`affiliate_click`）を`js/main.js`へ追加し、CTA計測（`lp_cta_click`）を3ページのインラインから同ファイルへ集約。商品識別を`data-product-id`/`data-product-name`ベースへ安定化
  - **収益導線**: お盆記事にボイスメモ商品のアフィリエイトリンク4本を追加（もしも経由）。**サイト全体のアフィリエイトリンクは30本→34本**（article08=20／article16=4／article17=4／article09=2／obon=4）
  - **デザイン**: 配色を深緑系→ローズ系パステル→**淡い青系パステル**へ2段階で刷新（現行は青系）。トップページに新着記事セクションを新設（最新3本・公開日つき、「運営者について」直後へ配置）し、全記事一覧への導線ボタンを追加
  - **削除**: Pollet宅配買取LP（`/ihin-kaitori/`）をサイトから削除（アフィリエイト審査が通らなかった等の理由は記録になし）。同ページへの内部リンクも全て差し替え済み
  - **画像**: column記事3本にアイキャッチ画像を追加（`images/column-*.webp`）
- 管理ファイルへの反映状況（2026-08-17時点で確認）:
  - `source-policy.md`・`ymyl-review-queue.md`: **適切に更新されていた**（column記事3本分の一次情報台帳・レビュー方針とも記載あり）
  - `content-inventory.csv`・`keyword-map.csv`・`internal-link-map.csv`: **未更新**（削除済みの`/ihin-kaitori/`が「公開」のまま残存、`legacy-giving-basics`・`obon-family-planning-talk`の行が欠落）→ 2026-08-17の実行で是正
  - `run-log.md`・`automation-state.json`: **未更新** → 本セクションで遡及記録
  - `source-policy.md`のお盆記事分（在ページには出典5件を明記済み）だけ台帳へ未転記だったため、2026-08-17に追記
- 残課題（2026-08-19に解消）: `images/column-legacy-giving-basics.webp`（v2への差し替えで未参照になった旧画像）がリポジトリに残存していた。2026-08-19に運営者のご指示で削除（削除前に、参照が`-v2.webp`の3か所（og:image・JSON-LD image・本文img）のみであることをHTML/CSS/JS/XML/CSV全文検索で確認済み。git履歴には残るため復元可能）
- 再発防止の提案: 運営者からの直接依頼で変更を行う場合も、同じ`docs/seo/`の管理ファイル（特に`run-log.md`・`content-inventory.csv`・`internal-link-map.csv`）を同時に更新する運用に統一することを推奨する

## 2026-08-13（PR #23 最終レビュー対応）

- 最新`main`を取り込み、PR #23の計測変更を統合状態で再検証
- `affiliate_click`の商品識別を、ページごとの見出しではなく安定した`data-product-id` / `data-product-name`から取得するよう修正
- 配置ごとの見出しは`placement`として分離し、同一商品を記事横断で集計できるようにした
- 未知のもしもリンクをAmazon扱いしないよう`shop=other`を追加し、不正なURLエンコードでもクリック処理を止めないようにした
- もしもリンクの正しい内訳は article08=20本、article09=2本、article16=4本、article17=4本（合計30本）
- 30本全件、CTA 16本、二重発火、商品ID・商品名の整合を回帰テストで確認

## 2026-08-12（臨時・運営者からのチャット依頼 その2：アフィリエイトのクリック計測）

- 実行日時: 2026-08-12 JST（PR #21マージ後、運営者から「進めてください」との依頼）
- ブランチ: claude/affiliate-click-tracking-2026-08-12（新規ドラフトPR運用）
- 前提: Google Search Console / Google Analytics への接続手段は引き続きこのセッションに存在しない。実データ分析はできないため、コードから検証できる改善を継続
- 判定: 全29公開ページの外部リンクを監査したところ、**サイトの収益源であるアフィリエイトリンク30本（もしも経由 af.moshimo.com）にクリック計測が一切設定されていない**ことを検出。どのページ・どの商品が実際にクリックされているかを把握できない状態だったため、これを最優先で対応
  - 内訳: article08（10商品×Amazon/楽天＝20本）、article09（2本）、article16（4本）、article17（4本）
  - Pollet（/ihin-kaitori/）のCTAは既に`data-cta`付きで`lp_cta_click`が計測しているため今回の対象外（二重計測を避ける）
- 実施した作業:
  - `js/main.js` にクリック計測を集約（全29ページで読み込み済みのため、HTML側の変更なしに全ページへ適用される）
    - **アフィリエイトクリック計測（新規）**: `af.moshimo.com`へのリンクを自動検出し`affiliate_click`イベントを送信。パラメータは `shop`・`product_id`・`product`・`placement`・`page_path`。商品ID・商品名は`.product-box`の明示属性から取得し、同じ商品を記事横断で集計する
    - **CTA計測の共通化（重複解消）**: 従来 index.html / ending-note/family-story/ / ihin-kaitori/ の3ページに同一のインラインスクリプトを重複記述していた`lp_cta_click`計測を`js/main.js`へ移動し、3ページのインラインブロックを削除。今後CTAを設置するページで計測を書き忘れる事故を防ぐ
  - 変更ファイル: `js/main.js`（計測を追加）、`index.html`・`ending-note/family-story/index.html`・`ihin-kaitori/index.html`（重複インラインを削除）
- 変更したURL: なし（表示内容・本文・title・meta descriptionの変更は一切なし。計測コードのみ）
- 検索意図: 変更なし
- 内部リンク: 変更なし
- 技術変更: GA4イベント`affiliate_click`を新規追加。`lp_cta_click`をmain.jsへ集約
- PDF/DOCX変更: なし
- 参考情報: 新規の法制度・統計・固有名詞の追加なし
- テスト結果:
  - `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 33, internal links checked: 947）
  - `js/main.js` の構文チェック（node vm）→ OK
  - **ヘッドレスChromium（Playwright）で実ページを開き、実際にクリックして`dataLayer`へ送信されるイベントを検証**（11項目すべてOK / NG 0件）
    - CTA計測: トップ3種（ヒーロー・親の終活・体験談バナー）／Pollet LP／体験談LP の5パターンで`lp_cta_click`が発火し、インライン削除後も動作することを確認
    - アフィリエイト計測: article08のAmazon・楽天両方、article09・16・17で`affiliate_click`が発火し、`shop`と`product`が正しく取得できることを確認。例: `{"shop":"rakuten","product":"1. 一番わかりやすいエンディングノート（リベラル社）"}`
    - 二重発火チェック: Pollet CTAのクリックで発火するイベントが`lp_cta_click`の1件のみであることを確認
- Search Console分析: データなし（`docs/seo/sc-data/`が引き続き未配置。SC/Analyticsへの接続手段もこのセッションにないため）
- YMYLレビュー待ち: 変更なし（計測コードのみで本文の記述は変更していない）
- 未解決事項: 計測が実際にGA4へ届いているかは、マージ・デプロイ後にGA4の「リアルタイム」または「イベント」レポートで`affiliate_click`・`lp_cta_click`を運営者にご確認いただく必要がある
- 次回予定: GA4に`affiliate_click`のデータが蓄積されたら、どの記事・どの商品が実際にクリックされているかを踏まえて収益記事（article08/09）の構成・CTA配置を見直す。実データ（SC/Analytics）が共有されれば、そちらに基づく改善を優先する
- PR: ドラフトPRを作成

## 2026-08-12（臨時・運営者からのチャット依頼：テクニカルSEO改善の継続）

- 実行日時: 2026-08-12 JST（PR #6・#7のマージ完了後、運営者から「続きをお願いいたします」との依頼）
- ブランチ: claude/breadcrumb-structured-data-2026-08-12（新規ドラフトPR運用）
- 前提: Google Search Console / Google Analytics への接続手段は引き続きこのセッションに存在しない（`ListConnectors`で確認済み、接続済みはGoogle Driveのみでチャット内は無効）。実データに基づく分析はできないため、**コードから検証可能なテクニカルSEOの不足**を洗い出して対応した
- 判定: 全29公開ページを機械的に監査したところ、**17ページでパンくずリストの構造化データ（BreadcrumbList JSON-LD）が欠落**していることを検出。いずれもDOM上には`<div class="container breadcrumb">`のパンくずが表示されているのに構造化データだけがない状態で、Google検索結果でのパンくずリッチリザルト表示の機会を逃していた。本プロンプト4章「構造化データのJSON構文」および11章「パンくず」の定期確認項目に該当するため、今回これを一括で補完
- 実施した作業:
  - BreadcrumbList JSON-LDを17ページへ新規追加（既存実装ページ＝article05/11/12/14/18・column配下3件・ハブ・30項目・体験談LPと同一形式に統一）
    - 記事14ページ: article01/02/03/04/06/07/08/09/10/13/15/16/17、ihin-kaitori
    - 固定3ページ: about.html、disclaimer.html、privacy.html
  - 各ページのDOM内パンくず（`<li>`要素のテキスト）と`<link rel="canonical">`のURLから機械的に生成し、**DOM表示とJSON-LDの文言が必ず一致する**ようにした（`tools/check-site.js`のDOM↔JSON-LD照合チェックで検証）
  - 挿入位置は既存ページと揃え、記事ページはArticle JSON-LDの直後、固定ページは`</head>`直前とした
  - index.html（トップページ）はパンくず自体が存在せず構造化データも不要のため対象外（意図的な除外）
- 変更したURL: 上記17ページ（本文・title・meta descriptionの変更は一切なし。構造化データの追加のみ）
- 検索意図: 変更なし（各ページの検索意図・コンテンツには手を加えていない）
- 内部リンク: 変更なし
- 技術変更: BreadcrumbList JSON-LDを17ページへ追加。サイト全体のパンくず構造化データ実装率が 11/29 → **28/29ページ**（index.htmlを除く全ページ）へ
- PDF/DOCX変更: なし
- 参考情報: 新規の法制度・統計・固有名詞の追加なし（構造化データのマークアップのみのため、source-policy.mdへの追加なし）
- テスト結果:
  - `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 33, internal links checked: 947）。同チェッカーはDOMのパンくずとJSON-LDの`name`が完全一致することを検査するため、17ページすべてで表示と構造化データの整合が取れていることを機械的に確認済み
  - 全公開ページのJSON-LDブロック67件を個別にJSONパースし、構文エラーがないことを確認
- Search Console分析: データなし（`docs/seo/sc-data/`が引き続き未配置。SC/Analyticsへの接続手段もこのセッションにないため、表示回数・CTR・掲載順位の分析は実施できていない）
- YMYLレビュー待ち: 変更なし（構造化データの追加のみで、本文の記述は変更していない）
- 未解決事項: パンくずリッチリザルトが実際に検索結果へ表示されるかは、Googleの再クロール後にSearch Consoleの「拡張」→「パンくずリスト」レポートで確認が必要。運営者にてマージ・デプロイ後にご確認いただきたい
- 次回予定: GA4クリック計測（`lp_cta_click`）が現状トップページ・体験談LP・Pollet LPの3ページのみのため、記事ページへの展開を検討。ただし実データ（SC/Analytics）が共有されれば、そちらに基づく改善を優先する
- PR: ドラフトPRを作成

## 2026-08-10（週次・定期実行）

- 実行日時: 2026-08-10 09:20 JST（Asia/Tokyo。無人の定期実行）
- ブランチ: claude/seo-weekly-2026-08-10（新規ドラフトPR運用）
- 事前確認: git status（クリーン）／origin/main最新化（7bf89e9）／CLAUDE.md（リポジトリに存在せず）／docs/seo配下の管理ファイル一式／既存ブランチ・オープンPRを確認（オープンPRはPR #7「claude/lp-top-page-improvements-2026-07-31」のみで、トップページのクリック計測・CTA改善という別件のため対象外。同一タスクの未完了PRなし）
- 判定: 編集カレンダーの2026-08-10〜14週分は「article05を拒否・NG例まで拡張（大幅更新）」の1タスク。優先順位（本プロンプト3章、親の終活クラスターの柱記事＝優先度3）に該当し、期限どおりの週のため今回実施。前回大幅更新（2026-08-03 article09）から14日未経過だが、編集カレンダーに元々この週として計画されていた別記事のタスクであり、過去の運用実績（2026-07-19→07-27で8日しか空けずarticle12→article14の大幅更新を実施した前例）とも整合するため実施した。新規記事は編集カレンダー上、次回2026-08-17週（きょうだい役割分担）まで予定がないため今回は対象外
- 実施した作業:
  - `articles/article05.html`（親への切り出し方）を大幅改修:
    - 「逆効果になりやすいNGパターン」を4件→5件（新規追加：よその家と比較する）に拡張し、各パターンにNG会話例（実際にあった逆効果な言い方の具体例）と「なぜ逆効果か」「代わりにどうするか」を追加
    - 新規セクション「親が拒否したときの対応（パターン別）」を追加。先送り型・感情的拒否・無言型・自己完結型・きょうだい不一致型の5パターンごとに、対応方針と会話例を掲載
    - 冒頭に結論box・この記事でできるようになることboxを新設。既存の「それでも話が進まないときは」を「3つのステップ」として明確化し、地域の高齢者相談窓口という第三者の選択肢を明記（自治体講座・終活カウンセラーという既存の一般的表現の範囲内で追記、新たな統計・固有名詞は追加せず）
    - よくある質問（FAQ）4問を新設し、FAQPage JSON-LDを追加。BreadcrumbList JSON-LDも新規追加（他記事と同形式、DOM↔JSON-LD一致を確認）
    - `dateModified`・最終更新日を2026-08-10へ更新（本文構成を伴う実質更新）。公開日と最終更新日を併記する表記へ変更（他の大幅更新済み記事と統一）
    - title/meta description/OGPを「拒否されたときの対応」を含む内容に更新（検索意図・URLは変更なし）
  - 内部リンク修正: keyword-map.csvに以前から記載されていたarticle05→30項目（/parent-shukatsu/questions/）の内部リンクが本文に未実装だったため、「それでも話が進まないときの3つのステップ」内と関連記事欄に追加。あわせて関連記事欄へ親の終活ハブ（/parent-shukatsu/）へのリンクも追加し、internal-link-map.csvへ新規行を記録
  - 8月分の月次レビュー（本来8月最初の週次実行=2026-08-03で実施すべきだったが未実施だったため、今回catch-upで実施）:
    - 親の終活クラスタの内部リンク（hub⇄questions⇄article05⇄article11⇄article12等）を確認、internal-link-map.csvどおりで問題なし（今回追加したarticle05→30項目分を除く）
    - title重複: なし（tools/check-site.js検査でも確認）。meta description重複: 全26公開ページのdescriptionを機械比較し重複なし
    - 孤立ページ: なし（articles/ending-note/parent-shukatsu/ihin-kaitori配下の全ページが他ページから最低1件の内部リンクを受けていることを確認）
    - コンテンツカニバリゼーション: keyword-map.csv上、主検索意図の重複なし。article05の主検索意図「親 終活 切り出し方」は他記事と重複なし
    - 低品質ページの統合候補: なし
    - Search Consoleデータ分析: `docs/seo/sc-data/` が引き続き未配置のためデータなし。表示回数・CTR・掲載順位・前月比較は「データ不足」として記録し、数値の推測は行っていない
  - 季節需要（6〜10週間後＝2026-09-21頃〜2026-10-19頃）確認: 該当する敬老の日・秋のお彼岸向けの記事更新（article14）は2026-07-27に対応済み。次の季節需要（年末年始・帰省）はeditorial-calendar.csvの2026-11前半・12月前半タスクとして既に計画済みのため、今回の追加着手なし
  - 編集カレンダー確認: 次回未着手タスクは2026-08-17〜21（親の終活を兄弟姉妹で進める役割分担、新規記事）。過去の未完了タスクの新たな遅延なし
  - 個別確認: canonical（26ページ全て固有URLで設定済み、重複なし）、robots.txt（Allow all + Sitemap行で正常）、意図しないnoindex（サイト内に該当なし。drafts/ディレクトリ自体が現存しない）、画像alt（本記事は画像追加なし）、PDF/DOCXリンク（downloads/配下は今回変更なし、既存リンクは前回まで確認済み）、新たな孤立ページ（なし）
- 変更したURL: https://shukatsu-guide.jp/articles/article05.html（本文大幅追加、title/description更新。検索意図・URLは変更なし）
- 検索意図: 主意図「親 終活 切り出し方」は維持。「親 終活 拒否」「親 終活 話したがらない」の周辺意図もカバー範囲に追加（keyword-map.csv更新）
- 内部リンク: article05→/parent-shukatsu/questions/、article05→/parent-shukatsu/ を新規追加
- 技術変更: BreadcrumbList・FAQPage JSON-LDを新規追加（DOM↔JSON-LD一致を`node tools/check-site.js`で確認）
- PDF/DOCX変更: なし
- 参考情報: 新規の法制度・統計・固有名詞の追加なし（本記事はアドバイス・会話例中心のコンテンツのため、source-policy.mdへの新規追加なし）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 30, internal links checked: 807）。Playwright（ヘッドレスChromium）で390px幅のスクリーンショットを取得し、横スクロールが発生しないことをDOM計測（scrollWidth<=clientWidth）で確認
- Search Console分析: データなし（`docs/seo/sc-data/`未配置。上記の月次レビュー参照）
- YMYLレビュー待ち: 変更なし（article05はYMYL区分「低」・専門家レビュー不要のため今回のレビュー対象外。既存のarticle18/15/07/10/17/30項目記事の項目は継続）
- 未解決事項: なし
- 次回予定: 2026-08-17週のきょうだい役割分担記事（新規、/parent-shukatsu/siblings/）に着手予定
- PR: ドラフトPRを作成

## 2026-08-04（臨時・運営者からのチャット依頼：デジタル遺産の相続対策記事）

- 実行日時: 2026-08-04 JST（週次定期実行とは別の、運営者からの詳細仕様つき直接依頼）
- ブランチ: claude/dreamy-noether-i7w9sb（新規ドラフトPR運用。週次PR #6とは別PR）
- 依頼内容: 「デジタル遺産 相続」を主キーワードとする新規記事の実装・掲載。記事構成・SEO要件・CTA・参考一次情報URL（国民生活センター/Apple×2/Google/法務省）が運営者から指定された
- 対応:
  - `articles/article18.html` を新規作成（article16/17が使用済みのため、指定の16ではなく次の空き番号18を使用）
    - H1「デジタル遺産の相続対策｜スマホの中の資産を家族に残す7ステップ」。デジタル遺産/デジタル遺品/デジタル契約の比較表、困る5ケース、資産一覧表（6種類×記録情報×注意点）、生前整理7ステップ、エンディングノートと遺言書の使い分け表、遺族向け初動、FAQ5問、まとめ＋2択カードCTA
    - article06（デジタル遺品全般の整理）とのカニバリ回避のため、本記事は「経済的価値のある資産の発見・相続準備」に限定し、写真・SNS・サブスクはarticle06へ誘導
    - パスワード・暗証番号・秘密鍵・シードフレーズをノートへ直接書かない方針を明記し、「家族がログインする」のではなく「公式相続窓口へ問い合わせる」形を一貫して案内
    - Article/BreadcrumbList/FAQPage構造化データを追加（FAQはDOMと機械照合一致）
  - 指定された一次情報5件＋NISA・暗号資産の取り扱いを事実確認（詳細はsource-policy.md台帳）。**全対象ドメインへの直接WebFetchがブロックされたため、複数検索クエリの一致による確認**。未確認の数値（相談件数・手数料額など）は記事に記載していない
  - アフィリエイトリンクは新規作成せず、CTAはすべて内部記事（article08比較記事・article10専門家相談記事）への送客とした（運営者指定の方針どおり）
  - 既存ページの更新: article06（お金セクション・もしもの設定・注意書きからarticle18へ誘導＋パスコード共有と読める箇所を最小修正＋関連記事欄）、article15（相続財産の調査からarticle18へ誘導＋関連記事欄）、index.html・parent-shukatsu/（全記事一覧へ追加）、sitemap.xml（article18追加、article06/15のlastmod更新）
  - article06の安全性修正: ステップ4の「（パスコードを）信頼できる家族にだけ伝える」を「封筒の保管場所だけを伝える」に修正し、Apple公式のセキュリティ案内（パスワードを共有しない）と整合させた。ステップ5に公式機能の固有名（故人アカウント管理連絡先/アカウント無効化管理ツール）を追記
  - 管理ファイル更新: content-inventory.csv／keyword-map.csv／internal-link-map.csv／editorial-calendar.csv／ymyl-review-queue.md（税理士または司法書士のレビュー待ちとして登録）／source-policy.md
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 29, internal links checked: 778）。モバイル幅（390px）・デスクトップ幅のスクリーンショットで表のはみ出しがないことを確認
- YMYLレビュー待ち: article18のNISA・暗号資産・相続の記述（税理士または司法書士。ymyl-review-queue.mdに登録済み）
- 阻害要因: 公的機関・Apple・Google・金融機関の全ドメインへの直接WebFetchがブロックされ、検索結果経由の確認に留まった（source-policy.mdに明記）。運営者ご本人による参考情報URLの原文確認を推奨
- 次回予定: 週次定期実行は従来どおり（次回はarticle05の大幅更新を予定）。本記事は公開2〜4週間後にインデックス状況を確認予定
- 特記事項: 本ブランチはmain基点のため、週次PR #6（article09/14の変更・同名管理ファイルの更新を含む）とは独立。運営者の指示によりPR #6を先にマージし、本ブランチへmainを取り込んで管理ファイルのコンフリクトを解消した（2026-08-04）

## 2026-08-03（週次・定期実行）

- 実行日時: 2026-08-03 09:12 JST
- ブランチ: claude/seo-weekly-2026-07-27（前回PR #6に追加コミット。article09は同PRの「次回予定」に残っていた同一タスクのため、新規ブランチ・新規PRは作らず既存PRを更新）
- 事前確認: git status（クリーン）／origin/main最新化／docs/seo配下の管理ファイル一式／既存ブランチ・オープンPRを確認（PR #6: claude/seo-weekly-2026-07-27＝article09タスク残存、PR #7: claude/lp-top-page-improvements-2026-07-31＝トップページ改善で別件のため対象外）
- 判定: 編集カレンダーの2026-08-03〜07週分（30項目記事）は2026-07-11の初回実行で前倒し完了済みのため対象外。優先順位（本プロンプト3章「4. 公開予定を過ぎている記事」）に従い、PR #6に残っていた期限超過タスクのarticle09（無料EN記事へ独自PDF/Word版追加）を今回実施。前回大幅更新（2026-07-27 article14）から14日未経過のため、隔週の別記事大幅更新は対象外
- 実施した作業:
  - `tools/pdf/free-ending-note.html` を新規作成: 自社オリジナルの記入式エンディングノート（1.基本情報／2.財産・お金／3.医療・介護の希望／4.葬儀・お墓の希望／5.デジタル情報／6.家族へのメッセージ／見直し記録の7セクション。暗証番号・パスワード等は書かない注意書き、専門家相談の目安を明記）。市販品や他社コンテンツは転用せず、article02（書き方ガイド）の項目分類を参考に独自作成
  - ヘッドレスChromium（`/opt/pw-browsers/chromium-1194`）で `downloads/free-ending-note.pdf` を生成（A4・5ページ）。`tools/build-pdf.ps1`はWindows Chrome前提でこの実行環境（Linux）では動作しないため、同等のヘッドレス印刷コマンドを直接実行
  - docxスキル（`docx` npmライブラリ、スクラッチパッドに一時インストールして生成）で `downloads/free-ending-note.docx` を新規作成。PDF版と同一内容をWord形式で用意
  - `articles/article09.html` を更新: 「無料版エンディングノートの入手方法」セクションに、当サイトオリジナルの無料エンディングノート（PDF/Word、会員登録・メールアドレス入力不要）のダウンロード導線を追加。まとめセクションにも1文追加。dateModified/最終更新日を2026-08-03へ更新
  - 管理ファイル更新: content-inventory.csv／keyword-map.csv（article09の最終実質更新日を2026-08-03へ）、internal-link-map.csv（article09→PDF/DOCX、article09→article02の行を追加）、editorial-calendar.csv（2026-07-27〜31週のarticle09行を完了に更新）、sitemap.xml（article09のlastmod更新）
- 変更したURL: https://shukatsu-guide.jp/articles/article09.html（本文にダウンロード導線セクションを追加。検索意図・title・meta descriptionは変更なし）
- 作成ファイル: `tools/pdf/free-ending-note.html`、`downloads/free-ending-note.pdf`、`downloads/free-ending-note.docx`
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 29, internal links checked: 752）
- PDF/DOCX確認:
  - PDF: ヘッドレスChromiumのスクリーンショットで1ページ目のレイアウト・日本語表示（IPAGothicで代替表示）を目視確認。PDF本体は5ページ生成を確認（内部の`/Count 5`）
  - DOCX: python-docxでテキスト構造（86段落・9テーブル、想定どおりの見出し順）を確認し、docx-jsで生成したXML各パーツ（document.xml等）がすべて整形式であることをXMLパーサーで確認。**ただしこの実行環境ではLibreOffice（soffice）headless変換が機能せず**（`.docx`だけでなく単純な`.txt`ファイルの変換すら"source file could not be loaded"で失敗する環境側の制約。トリビアルなdocxでも同様に失敗することを確認済み）、PDF化しての見た目の目視確認はできなかった
- YMYLレビュー待ち: 変更なし（既存のarticle15/article07/article10/article17/30項目記事の項目のまま。article09は低YMYL区分のため今回のレビュー対象外）
- 阻害要因: この実行環境ではWindows向けPDFビルドスクリプト（tools/build-pdf.ps1）とLibreOffice headless変換が動作しないため、代替手段（ヘッドレスChromium直接実行、python-docxでの構造検証）で対応した。次回、Windows環境またはLibreOffice headless変換が正常に動く環境でPDF/DOCXの最終的な見た目を再確認することを推奨
- 次回予定: 2026-08-10週のarticle05（親への切り出し方を拒否・NG例まで拡張）に着手予定
- PR: 既存のPR #6（claude/seo-weekly-2026-07-27）へ追加コミットし、本文を更新

## 2026-07-31（臨時・運営者からのチャット依頼：トップページLP改善）

- 実行日時: 2026-07-31 JST（運営者から「LPの改善点を考えて実行してほしい。Search Console/Analyticsの確認も必ず行って」と依頼。運営者の指す「LP」はトップページ`https://shukatsu-guide.jp/index.html`）
- ブランチ: claude/lp-top-page-improvements-2026-07-31（新規ブランチ、PR #7）
- 重要な制約: このセッションにGoogle Search Console/Google Analyticsへの接続手段が存在しないことを確認（`ListConnectors`実行、接続済みはGoogle Driveのみでこのチャットでは無効）。運営者はご自身のブラウザでSC/Analyticsにログイン済みとのことだったが、それは本セッションのアクセス権とは別物であるため、実データは取得できない旨を運営者に説明した
- 対応（データに依存しない範囲の改善に限定）:
  - トップページの主要CTA・カテゴリカード4種・体験談LPバナー・クロージングCTAに`data-cta`属性とGA4イベント計測（`lp_cta_click`）を追加。`/ihin-kaitori/`・`/ending-note/family-story/`で既に使われている実装パターンを流用し、次回Analyticsを確認できる状態になった際に導線ごとのクリック傾向を把握できるようにした
  - ヒーローのリード文に「親の終活の進め方」を明記し、`docs/seo/seo-strategy.md`が定める最優先クラスタ「親の終活」への副CTA（`/parent-shukatsu/`）をヒーロー内に追加。既存のエンディングノートCTAは変更せず併記
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（作業時点: HTML files 28・内部リンク735件／PR #6マージ後にmainを取り込んで再検証: HTML files 29・内部リンク753件、いずれも全通過）
- 運営者への確認事項（PR本文にも記載）:
  1. Search Console「検索パフォーマンス」・GA4レポートのスクリーンショットまたはCSVをチャットへ貼っていただくか、Google Driveコネクタを有効化してエクスポートを共有いただければ、実データに基づく分析・改善に着手できる
  2. トップページの「よく読まれている記事」ランキング（article08/01/02固定）は実データ未確認のため今回変更していない。実データが得られ次第、見直しを推奨
  3. ヒーロー文言・副CTAの追加は今回の判断によるもので、A/Bテストや実データでの検証は未実施
- PR: ドラフトPR #7を作成
- 次回予定: 運営者から実データ（Search Console/Analytics）が共有され次第、データドリブンなLP改善（CTA文言・導線の見直し、ランキングの実データ反映）に着手
## 2026-07-27（週次・定期実行）

- 実行日時: 2026-07-27 09:15 JST
- ブランチ: claude/seo-weekly-2026-07-27（ドラフトPR運用）
- 事前確認: git status（クリーン）／origin/main最新化（0c6b8fc）／CLAUDE.md（リポジトリに存在せず）／docs/seo配下の管理ファイル一式／既存ブランチ・オープンPRを確認（オープンPRなし、claude/pollet-lp-2026-07-20とclaude/seo-weekly-2026-07-20はマージ済みブランチとして残存のみ、重複作業なし）
- 判定: 編集カレンダーの2026-07-27〜31週分は「article09 PDF/Word版追加（大幅更新）」「article14 秋彼岸向け更新」の2タスク。1回の実行では大幅更新・記事更新をあわせて大量に行わないという原則と、季節需要（6〜10週間後＝2026年9月上旬〜10月上旬に敬老の日9/21・秋のお彼岸9/23が該当）を優先する順序（本プロンプト3章の優先順位5番）にもとづき、季節性の高いarticle14を今回実施。article09は次回に持ち越し
- 実施した作業:
  - article14.html（お墓の終活）を更新:
    - 改葬許可の法的根拠を明記（墓地、埋葬等に関する法律第5条：改葬には市町村長の許可が必要、申請先は焼骨が現に存する地の市区町村）
    - 「秋のお彼岸は、家族で話す好機」セクションを新設。2026年の秋分の日（9月23日・水）と、敬老の日（9/21）に挟まれた9/22が「国民の休日」で休日となり9/19〜23が連休になる旨（国立天文台の暦要項発表・複数報道で確認）を紹介し、状況別（承継者あり/なし/遠方）の考え方・会話例3パターン・「お彼岸に確認しておきたいことシート」（印刷せず本文チェックリストとして掲載）を追加
    - 「費用とトラブルを避けるために知っておきたいこと」セクションを新設。国民生活センターの相談件数推移（2021年度969件→2023年度1,148件、3〜4割が離檀料・改葬関連）、離檀料に法的基準がない点、宗派相違トラブル例、相談先（消費者ホットライン188・国民生活センター、法律問題は弁護士司法書士）を追加。具体的な費用相場（墓石撤去・永代供養等）は信頼できる一次情報が見つからなかったため数値を記載せず、「複数社の書面見積もりで比較する」案内にとどめた（未確認の価格を記載しない方針を遵守）
    - FAQ（4問）とFAQPage JSON-LD、BreadcrumbList JSON-LDを新規追加。冒頭に結論box・できるようになることboxを追加。関連記事に親の終活ガイド・article05を追加
    - dateModified/最終更新日を2026-07-27へ更新（本文を伴う実質更新）
  - parent-shukatsu/index.html（親の終活ハブ）: 記事一覧にarticle14を追加、状況別ケースに「実家のお墓が気になる場合」カードを新設しarticle14へリンク
  - sitemap.xml: article14・parent-shukatsu/のlastmodを2026-07-27へ更新
  - 管理ファイル更新: docs/seo/keyword-map.csv、docs/seo/content-inventory.csv、docs/seo/internal-link-map.csv、docs/seo/editorial-calendar.csv（該当タスクを完了に更新）、docs/seo/source-policy.md（新規一次情報3件を台帳へ追加）
- 変更したURL: https://shukatsu-guide.jp/articles/article14.html（本文追加・構造化データ追加）／https://shukatsu-guide.jp/parent-shukatsu/（内部リンク追加）
- 検索意図: 「墓じまい」「永代供養」「樹木葬」（既存の主意図は維持）に加え、秋のお彼岸を機に家族で話し合う読者の意図をカバー
- 内部リンク: 親の終活ハブ⇄article14を新規に相互整備。article14→article05（切り出し方）を追加
- 技術変更: BreadcrumbList・FAQPage JSON-LDを新規追加（他記事と同じ形式でDOM↔JSON-LD一致を確認）
- 参考情報:
  - 国立天文台「令和8年（2026）暦要項」（秋分の日9/23、9/19〜23の連休。確認日2026-07-27）
  - 墓地、埋葬等に関する法律第5条（厚生労働省法令等データベース。確認日2026-07-27）
  - 国民生活センター「墓・葬儀サービス（各種相談の件数や傾向）」（確認日2026-07-27）
  - いずれも直接WebFetchはブロックされたため、複数の検索クエリで再現性を確認する方法で裏取りした（詳細はsource-policy.md参照）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 28, internal links checked: 748）
- PR: ドラフトPRを作成
- YMYLレビュー待ち: 変更なし（既存キューを継続。article14自体は「中（行政手続・消費者トラブル）」区分で従来どおり「将来推奨」、緊急の専門家レビュー登録は不要と判断）
- 阻害要因: 墓石撤去・永代供養・樹木葬などの具体的な費用相場について、信頼できる一次情報（公的統計等）が見つからなかったため、本文には数値を記載せず「複数社見積もり」の案内にとどめた。編集カレンダーの「費用」項目は手続き面（改葬許可の法的根拠）とトラブル対応面（相談先）のみ充足し、具体的な金額の記載は今後一次情報が得られ次第の課題として残る
- 次回予定: 2026-07-27〜31週の残タスクであるarticle09（無料エンディングノートPDF/Word版追加）に着手予定

## 2026-07-21（臨時・運営者からのチャット依頼：Pollet LPの公開）

- 実行日時: 2026-07-21 JST（PR #5レビュー後、運営者から「公開してください」と依頼）
- ブランチ: claude/pollet-lp-2026-07-20（PR #5に追加コミット）
- 対応:
  - `drafts/ihin-kaitori/index.html` を `/ihin-kaitori/index.html` へ移動し、相対パス（`../../` → `../`）を修正
  - `<meta name="robots" content="noindex">` を削除
  - `datePublished`/`dateModified`/本文の公開日表記を実際の公開日 2026-07-21 に更新
  - `sitemap.xml` へ追加（lastmod 2026-07-21）
  - 内部リンクを追加: トップページ全記事一覧、親の終活ハブの記事一覧、article12（生前整理）の関連記事欄から、それぞれ`/ihin-kaitori/`へ
  - 管理ファイル更新: content-inventory.csv（状態を「下書き」→「公開」に更新）、internal-link-map.csv（新規リンク行を追加）
  - ページ末尾のTODOコメントを、公開後も残る作業（アフィリエイト承認後のリンク差し替え、キャンペーン条件の反映）だけに整理
- **重要**: Polletのアフィリエイトは引き続き審査中のため、CTAボタン3か所は現時点でもPollet公式サイト（`https://pollet.tech/lp`）への直リンクのまま。**このままでは当サイトにアフィリエイト収益は発生しない。** 承認後、正式なトラッキングURLをいただき次第、差し替えが必要
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 28, internal links checked: 734）
- 次回予定: Polletのアフィリエイト審査が承認され次第、トラッキングURLへの差し替えを実施

## 2026-07-20（臨時・運営者からのチャット依頼 その3：新規アフィリエイトLPの下書き）

- 実行日時: 2026-07-20 JST（PR #4マージ後の、別件のチャット依頼）
- ブランチ: claude/pollet-lp-2026-07-20（新規ブランチ。旧PR #4はマージ済みのため新規ブランチで対応）
- 依頼内容: 運営者が申請中の宅配買取サービス「Pollet」（pollet.tech）のアフィリエイトを促すLPを制作してほしい、あわせてrepo内にアップロードされた「日本の遺品整理市場リサーチ報告書」を参考にする指示
- 対応:
  - pollet.tech/lpへの直接WebFetchはブロックされたため、検索結果経由でサービス内容を確認。**Polletは訪問型の遺品整理業者ではなく、箱詰めして送るだけの宅配買取（リユース）サービス**であることを確認し、誤解を招かないようLP本文中に明記
  - アフィリエイトは運営者から「申請中」（未承認）と共有されており、正式なトラッキングリンクが存在しないため、**CTAボタンは暫定的にPollet公式サイト（https://pollet.tech/lp）への直リンクとし、正式リンクへの差し替えをHTMLコメントでTODOとして明記**
  - 査定額アップの具体的な金額・対象エリア・キャンペーン条件は一次情報で確認できなかったため、本文では断定的な数値を記載せず、「公式サイトでご確認ください」と誘導
  - リサーチ報告書内の公的統計（65歳以上人口比率、単身高齢世帯数、死亡数推移、空き家率）は出典が明記された政府統計のため、背景説明セクションでそのまま引用
  - `drafts/ihin-kaitori/index.html`として新規作成。**下書き運用**（`docs/seo/ymyl-review-queue.md`記載の手順どおり、`<meta name="robots" content="noindex">`付与・sitemap.xml未掲載・トップや他記事からの内部リンクなし）とし、まだ公開していない
  - 管理ファイル: content-inventory.csvに下書きとして1行追加（他の管理ファイルは、公開前のため今回は更新せず）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 28, internal links checked: 731。drafts/配下のnoindex必須チェックも通過）
- 公開前に必要な対応（ページ内TODOコメントにも記載）:
  1. Polletアフィリエイト審査の承認後、正式なトラッキングURLへ3か所のCTAリンクを差し替える
  2. 対象エリア・査定額アップ・キャンペーン条件を公式サイトの最新情報で確認し、本文に反映するか判断する
  3. 確認後、`drafts/ihin-kaitori/`から`/ihin-kaitori/`へ移動し、noindexを外し、sitemap.xmlへ追加する
  4. トップページ・article12等からの内部リンクを追加する
- 次回予定: Polletのアフィリエイト審査結果が出次第、運営者からの指示で公開作業を実施予定

## 2026-07-20（臨時・運営者からのチャット依頼 その2）

- 実行日時: 2026-07-20 JST（article16に続く、同日2件目のチャット依頼）
- ブランチ: claude/seo-weekly-2026-07-20（同PRに追加コミット）
- 依頼内容: ニュースURLの提示のみ（[ファイナンシャルフィールド「独身の兄が64歳で亡くなり、年金を一度も受け取れませんでした…」Yahoo!ニュース配信2026-07-16](https://news.yahoo.co.jp/articles/179865ee953109996557b106404ead565340e7d0)）
- 対応:
  - 記事の内容（独身・子どものいない兄が国民年金を40年納付し老齢基礎年金を受けずに64歳で死亡、同居のきょうだいが対象になりうる制度は何か）を検索結果経由で確認
  - 記事が扱う制度が「死亡一時金」（国民年金第1号被保険者が老齢基礎年金等を受けずに死亡した場合の一時金）であり、混同されやすい「未支給年金」（既に年金を受給していた方が死亡した場合の制度）とは別物である点を、日本年金機構の一次情報ページ2件（死亡一時金／未支給年金）で確認したうえで整理
  - `articles/article17.html`を新規作成。死亡一時金・未支給年金それぞれの要件・金額・時効を一次情報つきで解説し、家族が請求を忘れないためのチェックリストとエンディングノートへの記録項目を提案。アフィリエイトはarticle16と同じ実在リンクを再利用（新規リンクは作成せず）
  - 内部リンク: トップ全記事一覧・親の終活ハブ（記事一覧＋「親が亡くなった直後の方」導線）・article15関連記事欄に相互リンク追加
  - ymyl-review-queue.mdに、金額・時効の記述について社会保険労務士のレビュー待ちとして登録（一次情報での事実確認は済み、個別ケースへの当てはめの専門家レビューは未実施）
  - **注意**: news.yahoo.co.jp・nenkin.go.jpいずれも直接WebFetchがブロックされたため、検索結果経由（複数クエリで再現性を確認）での確認に留まる。詳細はsource-policy.mdに記録
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 27, internal links checked: 709）
- 特記事項: 同日3本目相当の新規記事（週次1本＋臨時2本）となり、通常の「新規記事は週1本まで」の原則を運営者の直接指示により超過している。今後さらにニュース記事の追加依頼が続く場合は、ペースについて運営者に一度確認することを推奨
- 次回予定: 週次側は従来どおり2026-07-27週のarticle09・article14に着手予定

## 2026-07-20（臨時・運営者からのチャット依頼）

- 実行日時: 2026-07-20 JST（同日の週次定期実行とは別に、運営者からセッション内で直接依頼）
- ブランチ: claude/seo-weekly-2026-07-20（週次PRに追加コミット）
- 依頼内容: 「ここ1週間の終活に関する記事を引用してレビューするページを書いてください。それに必要な商品を紹介するアフィリエイトも載せてください」+ もしもアフィリエイトの参考URL（`shop_site_id`が空欄で未完成のもの）
- 対応:
  - もしもの`shop_site_id`が空欄だった点、および「この1週間」の終活ニュースを機械的に検索しても信頼できる一次情報が見つからなかった点を運営者に確認。運営者から具体的なニュースURL（NBS長野放送「急な免許返納はリスク『認知症になりやすく』…『運転終活』」、Yahoo!ニュース配信2026-07-15）の提示を受け、これを基に記事化
  - `articles/article16.html`を新規作成。元記事の内容（長野県東御市の講座、真田自動車学校・宮下拓也氏、長野県警調べの事故統計、「運転終活」2ステップ）を紹介し、親への運転免許返納の切り出し方・会話例・エンディングノートへの記録項目につなげる構成。本文中に元記事へのリンクを明記し、報道の要約であって医学的・法的助言ではない旨を冒頭の注意書きで明示
  - アフィリエイト商品: 運営者から`shop_site_id`の正しい値・新規に紹介したい商品の指定がなかったため、新しいアフィリエイトリンクは作成せず、article08.htmlで既に使用されている実在のもしもリンク（一番わかりやすいエンディングノート／もしもに備える情報ノート、いずれも`a_id=5675374`のAmazon・`a_id=5675373`の楽天リンクをそのまま再利用）を文脈に合わせて再掲載
  - 内部リンク: トップページ全記事一覧・親の終活ハブの記事一覧・article05（親への切り出し方）の関連記事欄に相互リンクを追加
  - 管理ファイル更新: content-inventory.csv／keyword-map.csv／internal-link-map.csv／editorial-calendar.csv（臨時追加として記録）／sitemap.xml／automation-state.json／source-policy.md（ニュース引用元と確認日、直接WebFetchがブロックされたため検索結果の再現性で確認した旨を記録）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 26, internal links checked: 677）
- 特記事項: この記事は編集カレンダーに元々計画されていたものではなく、運営者からの当日のチャット依頼による追加。週次自動運用の「新規記事は週1本まで」の原則とは別に、運営者の直接指示によるものとして扱った
- 次回予定: 週次側は従来どおり2026-07-27週のarticle09・article14に着手予定

## 2026-07-20（週次・定期実行）

- 実行日時: 2026-07-20 09:08 JST
- ブランチ: claude/seo-weekly-2026-07-20（ドラフトPR運用）
- 判定:
  - 編集カレンダーの2026-07-20〜24週分（article11チェックリスト大幅改修＋親の終活ハブ新設）は2026-07-11の初回実行で前倒し完了済みのため、新規記事・大幅更新の対象なし
  - 前回大幅更新（2026-07-19 article12）から14日未経過のため、隔週の既存記事大幅更新も対象外
  - 半期YMYL事実確認（本来2026年7月最初の実行=7/11で実施すべきだったが未着手だったもの）が pending_review_tasks に残っていたため、今回これを実施
- 実施した作業:
  - git status／origin/main最新化（f63d804→43fde4b）／CLAUDE.md（リポジトリに存在せず）／docs/seo配下の管理ファイル一式／既存ブランチ・オープンPRを確認（mainのみ、オープンPRなし、重複作業なし）
  - 半期YMYL事実確認（2026年7月分）:
    - 対象14分野のうち、公開済み記事があるのは相続・税務（article15）、遺言（article07）、専門職の業務範囲（article10）、デジタルサービス（article06）、医療の一部（parent-shukatsu/questions/ Q6〜Q10）
    - article15の期限4件（相続放棄・限定承認は原則3か月／準確定申告は原則4か月／相続税申告・納付は原則10か月／相続登記義務化は2024-04-01施行・正当な理由なき申請懈怠で10万円以下の過料）について、裁判所・国税庁（2件）・法務省の公式ページを検索結果の引用内容で照合し、既存の記載と数値の齟齬がないことを確認。各記述に一次情報リンクを追加し、source-policy.mdの台帳に確認日2026-07-20で記録
    - article07（遺言3種比較・法務局保管制度）・article10（士業業務範囲）は、いずれも既に「目安」「詳しくは公証役場・法務局・各専門家にご確認ください」「法律アドバイスではありません」等の限定表現・免責があり、断定的な誤記載は見つからず。追加の一次情報付与は不要と判断（内容自体の専門家レビューは引き続き未実施）
    - article06（デジタル遺品）は特定サービス名・価格・統計の記載がなく、問題なし
    - 医療・人生会議・ACP・延命治療・認知症・介護・身元保証・死後事務・行政の相談窓口は該当する公開記事がないため今回はレビュー対象外（該当記事の公開/下書き作成時に実施）。専門家レビューが必要な箇所は引き続き docs/seo/ymyl-review-queue.md に登録したまま、「監修済み」表示はしていない
    - 直接のWebFetchはcourts.go.jp/nta.go.jp/moj.go.jpへのアクセスがブロックされたため実施できず、検索結果に含まれる当該公式ページの引用内容とタイトルの一致による確認とした。詳細はsource-policy.mdに記録
  - サイト健全性チェック: `node tools/check-site.js` 全通過（HTML 25件・内部リンク645件）
  - 個別確認: canonical（22ページ全て固有URLで重複なし）、robots.txt（Allow all + Sitemap行で正常）、意図しないnoindex（drafts以外になし）、画像alt（img要素はすべてalt属性あり）、PDF/DOCXリンク（downloads/配下3件すべて実在・リンク切れなし）、新たな孤立ページ（なし。tools/pdf/配下のPDFソースHTMLは非公開の生成元でありsitemap対象外のため正常）
  - Search Consoleデータ分析: `docs/seo/sc-data/` が未配置のためデータなし。表示回数・CTR・掲載順位・前月比較は「データ不足」として記録し、数値の推測は行っていない
  - 季節需要（6〜10週間後 = 2026-08-31〜2026-09-24頃）確認: 敬老の日（2026-09-21）・秋のお彼岸（2026-09-23頃）が該当。対応するお墓記事更新（article14）は editorial-calendar.csv で2026-07-27〜31に計画済みのため、今回は追加着手なし
  - 編集カレンダー確認: 次回未着手タスクは2026-07-27〜31（article09 PDF/Word版追加、article14秋彼岸向け更新）。過去未完了タスクの新たな遅延なし
- 変更したファイル:
  - articles/article15.html（期限4件に一次情報リンク追加、dateModified/最終更新日を2026-07-20へ更新）
  - sitemap.xml（article15のlastmod更新）
  - docs/seo/content-inventory.csv、docs/seo/keyword-map.csv（article15の最終実質更新日を2026-07-20へ）
  - docs/seo/source-policy.md（一次情報台帳へ4件追加）
  - docs/seo/ymyl-review-queue.md（article15のステータス更新、半期事実確認の実施記録セクション追加）
  - docs/seo/automation-state.json、docs/seo/run-log.md
- 変更したURL: https://shukatsu-guide.jp/articles/article15.html（本文の一部・参考リンク追加、検索意図・タイトル・見出し構成は変更なし）
- 作成ファイル: なし（新規記事・新規PDFなし）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 25, internal links checked: 645）
- PR: ドラフトPRを作成
- YMYLレビュー待ち: article15の期限記述4件（一次情報URL付与済み・数値の専門家レビューは未）／article07・article10（専門家レビュー未）／30項目記事の延命治療項目（医療職レビュー推奨）／医療・人生会議・ACP・延命治療・認知症・介護・身元保証・死後事務・行政の相談窓口は該当記事なしのため次回該当記事公開時に実施
- 阻害要因: courts.go.jp/nta.go.jp/moj.go.jpへの直接WebFetchがブロックされたため、検索結果経由での確認に留まった（内容の性質上、数値・制度の同一性は高い確度で一致を確認できたと判断）。Search Consoleの実データが引き続き存在しないため、データ起点の分析は一部実施不可
- 次回予定: 2026-07-27週の article09（無料エンディングノートPDF/Word版追加）・article14（お墓記事の秋彼岸向け更新）に着手予定

## 2026-07-11（初回・手動実行）

- ブランチ: claude/seo-initial-2026-07-11（ドラフトPR運用）
- 実施:
  - 現状調査（site-audit.md）
  - 管理ファイル一式作成（docs/seo/ 配下12点＋.claude/prompts/shukatsu-seo-routine.md）
  - /parent-shukatsu/ カテゴリーハブ新設
  - /parent-shukatsu/questions/ 「親が元気なうちに聞いておくこと30項目」新設＋PDF
  - /articles/article11.html を「終活チェックリスト完全版」へ大幅改修＋PDF
  - トップのカテゴリカードに「親の終活」導線追加
  - sitemap.xml へ2URL追加・article11のlastmod更新
  - チェッカーを tools/check-site.js としてリポジトリへ正式移設（FAQ/パンくずJSON-LD照合・title/H1重複検査を含む）
- テスト: tools/check-site.js 全通過（結果はPR本文参照）
- 特記: カレンダー上7/20週・8/3週予定のタスクを初回に前倒し実施（editorial-calendar.csv に記載）

## 2026-07-16（週次・定期実行）

- 実行日時: 2026-07-16 15:27 JST
- ブランチ: claude/seo-weekly-2026-07-16（ドラフトPR運用）
- 判定: 新規記事・大幅更新ともに今回は対象なし（編集カレンダーの次回未着手タスクは2026-07-27〜31開始で未到来。前回大幅更新2026-07-11から14日未経過のため隔週更新も未到来）
- 実施した作業:
  - git status／デフォルトブランチ最新化／CLAUDE.md（リポジトリに存在せず）／docs/seo配下の管理ファイル一式／既存ブランチ・未完了PRを確認（オープンPRなし、重複作業なし）
  - サイト健全性チェック: `node tools/check-site.js` 全通過（HTML 24件・内部リンク629件、リンク切れ・アンカー不整合・タグ不整合・JSON-LD構文エラー・FAQ/パンくずDOM不一致・title重複・H1重複欠落・sitemap不整合・drafts混入いずれもなし）
  - 個別確認: meta description重複（なし）、canonical欠落（なし・全ページ設定済み）、意図しないnoindex（なし）、robots.txt（Allow all + Sitemap行で正常）、画像alt欠落（なし）、PDF/DOCXリンク（downloads/配下2件とも実在・リンク切れなし）
  - 月次レビュー（前回未実施だったため今回実施。last_monthly_review: null → 2026-07-16）:
    - 親の終活クラスタ内部リンク: hub↔questions↔article11の相互リンク、hubからarticle05/06/08/11/12/15への導線、questionsからhubへの戻りリンク（`href="../"`）を確認、いずれも internal-link-map.csv どおりで問題なし
    - 孤立ページ: なし（全24ページがトップまたは記事・ハブから到達可能）
    - コンテンツカニバリゼーション: keyword-map.csv上、主検索意図の重複なし（site-audit.md記載のとおり）
    - 低品質ページの統合候補: なし（全ページ公開10日以内、統合を要する薄いページなし）
  - Search Consoleデータ分析: `docs/seo/sc-data/` に該当月のCSVが未配置のためデータなし。表示回数・CTR・掲載順位・前月比較は「データ不足」として記録し、数値の推測は行っていない
  - 季節需要（6〜10週間後）確認: 敬老の日（2026-09-21）・秋のお彼岸（2026-09-23頃）が該当。対応するお墓記事更新は editorial-calendar.csv で2026-07-27〜31に既に計画済みのため、今回は追加着手なし
  - 編集カレンダー確認: 次回未着手タスクは2026-07-27〜31（article09 PDF/Word版追加、article14秋彼岸向け更新）。過去未完了タスクの遅延なし
- 変更したファイル: docs/seo/automation-state.json、docs/seo/run-log.md（管理ファイルのみ。記事・サイトページの変更なし）
- テスト結果: `node tools/check-site.js` → ALL CHECKS PASSED（HTML files: 24, internal links checked: 629）
- YMYLレビュー待ち: 半期YMYL事実確認（医療/介護/相続/税務等14分野）が2026年7月分未着手（初回実行2026-07-11時点で未実施のまま）。大型タスクのため今回は着手せず、pending_review_tasksに記録し次回以降で優先着手予定
- 阻害要因: なし（Search Consoleの実データが存在しないためデータ起点の分析のみ一部実施不可。記事コンテンツの安全な変更対象が今回は存在しなかった）
- PR: ドラフトPRを作成（管理ファイル更新のみ）
- 次回予定: 2026-07-27週の article09（無料エンディングノートPDF/Word版追加）・article14（お墓記事の秋彼岸向け更新）に着手予定。半期YMYLレビューも状況を見て早期着手を検討

## 2026-07-19（臨時・手動実行：Search Console改善対応）

- 実行日時: 2026-07-19 午前 JST（運営者依頼による臨時実行。週次ルーチンとは別）
- ブランチ: claude/seo-article12-2026-07-19（ドラフトPR運用）
- きっかけ: Search Console「ページのインデックス登録」レポート（最終更新2026-07-10）の確認依頼
- SC調査結果（未登録6件の内訳）:
  - noindex除外×2: /tag/沖縄/ ほか → 前所有者WordPress時代の残骸（最終クロール2025年2月）。現在404。対応不要
  - リダイレクト×1: https://www.shukatsu-guide.jp/ → www→apexの301で正常。対応不要
  - 代替ページ(canonical)×1: /index.html → canonicalで「/」に統合済みで正常。対応不要
  - クロール済み-未登録×2: http://版トップ（https版が登録済みで対応不要）と **/articles/article12.html（要改善と判断）**
- 実施: article12（生前整理）を大幅改修（編集カレンダー2026-10後半の「部屋別リスト+8週間計画」タスクを前倒し）
  - 冒頭結論ボックス・部屋別チェックリスト6エリア・品目別の手放し方表（家電リサイクル4品目注意含む）・8週間モデルプラン表・親の生前整理の会話例・失敗5つ・業者依頼の注意（一般廃棄物処理業の許可確認・国民生活センター出典リンク・見積もり確認項目）・FAQ6問を追加
  - BreadcrumbList/FAQPage構造化データ追加、dateModified 2026-07-19、title/description刷新（URL変更なし）
  - 4レンズ検証（禁止表現/事実/日本語/検索意図）を実施し、断定表現の緩和・係り受け修正・老前整理の定義補足など17件中15件を反映（不採用2件=架空事例の追加提案・資格記載への疑義は運営者確認事項へ）
  - 印刷用PDF新規作成: downloads/seizen-seiri-checklist.pdf（ソース tools/pdf/seizen-seiri-checklist.html、A4・2ページ・生成確認済み）
  - 導線: トップ/体験談LP/親の終活ハブの記事一覧アンカーを新タイトルへ、article12→hub/30項目/article05リンク追加
  - sitemap.xml: article12のlastmodを2026-07-19へ。SCでサイトマップ再送信済み（検出20→22ページに増加）
  - 管理ファイル: content-inventory/keyword-map/internal-link-map/editorial-calendar 更新（PR#1マージ済みに伴うPR中→公開の状態反映含む）
- テスト結果: node tools/check-site.js → 後述PR本文参照
- 次回予定: PRマージ後にSearch ConsoleでサイトマップTB再送信・article12のインデックス登録リクエスト。/parent-shukatsu/ と /parent-shukatsu/questions/ は公開済みのため即日リクエスト
