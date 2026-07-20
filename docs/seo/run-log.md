# 実行ログ（run-log）

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
