# 実行ログ（run-log）

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
