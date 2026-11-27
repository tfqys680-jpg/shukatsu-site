> この資料は初回の未公開実装時点の記録です。今回の公開対応・最新状態は publication-review.md を参照してください。

# 親の介護、どう切り出す？ 未公開実装レビュー

作業日：2026-11-27（日本時間）。対象HEAD：`dfdb78cee9aa1cb4ef38d4c9ba75fd099934c929`。
作業開始時はgit statusが空の新規クローン。既存の未コミット変更なし。コミット・プッシュ・PR作成/更新・マージ・公開・デプロイは行っていない。変更はローカルの未コミット状態。

## 判定と重複照合

新規下書き `drafts/parent-care-family-conversation/index.html` を実装。予定URLは `/column/parent-care-family-conversation/`。既存記事の削除・統合・公開ページ本文の変更なし。

| 照合先 | 主な検索意図 | 今回との境界 |
|---|---|---|
| drafts/parent-care-without-burnout/（未公開） | 介護で共倒れしない体制・費用・外部支援・仕事との両立 | 家族の役割/費用整理は重なるが、今回は元気な親への最初の会話、了承・拒否への対応・情報共有の同意に限定。介護サービス選択や費用負担の判断は追加しない |
| parent-shukatsu/questions/ | 終活全般の30項目の聞き取り | 今回は介護について話し始める場面に絞り、全般の質問集へリンク |
| articles/article05.html | エンディングノートへの切り出し | 今回は記入依頼ではなく介護の意向確認が中心 |
| column/obon-family-planning-talk/ | お盆の帰省時に終活全般を聞く | 今回は季節限定にせず、介護の最初の会話に絞る |
| column/work-care-consultation-preparation/ | 介護開始後の職場相談 | 介護前の親子の会話から、必要時に既存記事へリンク |

キーワード台帳と類似本文を確認して上記の境界を記録。GitHubのopen PR検索は0件（読み取りのみ）。リモートブランチにも同スラッグは見当たらない。公開時にはカニバリゼーションを再評価する。

## 既存仕様・実装

- AGENTS.md→CLAUDE.md、README、docs/agent-harness/README.md、SEO戦略・source-policy・定期作業プロンプトを確認。
- 静的HTML＋GitHub Pages。package.json、ロックファイル、専用のbuild/lint/型チェックscriptは存在しない。静的記事の構築にnpm依存追加は不要。
- 共通デザイン：css/style.css、js/main.js。ルート直下のフォルダ/index.htmlでルーティング。既存draftテンプレートに沿う。GA4の既存設定も継承。
- 原稿のSEOタイトル・description・導入・H2/H3・本文・7項目チェックリスト・FAQ3件・CTA・出典を反映。CTAの実装指示と人向け確認事項を読者本文へ混ぜず、本資料へ分離。news-brief.txtの5件は本文に使用していない。
- 会話例・5項目・チェックリストは編集上の提案と明示。専門家による監修済みの表示なし。
- 内部リンクはarticle02、where-to-ask、work-care-consultation-preparation、questionsなど実在ページへ設置。
- title/description/canonical/OGP/Twitter、Article・BreadcrumbList・FAQPageを実装。canonical/og:urlは既存draftと同じ公開予定URL方式。現在その公開ルートは作成していない。
- FAQは既存方針に沿ってFAQPageを維持し、表示3問3答とJSON-LDを一致。Googleの公式更新履歴（2026-05-08/06-15）ではFAQ特別表示の終了・文書削除を確認したため、検索の特別表示を期待/保証するものではない。既存サイト全体のFAQ方式は変更しない。
- 画像は指定PNG（1672×941、2,086,158 bytes）を同一ハッシュで保持、WebP幅640/960/1672を配信（22,840/39,846/90,262 bytes）。静的srcset/sizes、width/height、eager/highでヒーロー領域を予約。1200×630 OGP（60,684 bytes）は全体を収めた余白付きで、顔を切らず目視確認済み。alt・AI生成キャプションは指定どおり。
- 公開日・更新日とも未定。ArticleにdatePublished/dateModifiedを付けず、原稿作成日・出典公表日を流用していない。
- content-inventory/keyword-mapは予定URLを下書き・公開日/更新日未定で追加。ymyl-review-queueも記録。sitemap、公開一覧、カテゴリハブ、公開ページの関連記事からの受けリンクは追加しない。

## 出典の確認（2026-11-27）

| URL | 到達性・確認内容 |
|---|---|
| https://prtimes.jp/main/html/rd/p/000000223.000159136.html | curl HTTP 200。発表主体SOMPOの配信資料本文と調査概要を照合。43.5%は一度も話したことがない、26.5%は話題に出した程度で未決定、合計70.0%。該当設問n=929と全体有効回答1,048人を区別。30〜59歳・親が健在・調査10/9〜16・配信11/12を確認 |
| https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/hukushi_kaigo/kaigo_koureisha/chiiki-houkatsu/index.html | curl HTTP 200。厚労省の地域包括支援センターの総合相談・権利擁護を確認。受付日時/家族のみの相談方法/予約は個別確認とする |
| https://developers.google.com/search/updates | FAQリッチリザルトに関する2026年5/8・6/15の公式更新記録を確認。既存のDOM↔JSON-LD一致方針を維持 |

調査は企業のインターネット意識調査であり、日本全家庭への一般化や会話の効果の証明にしない。出典の画像・図表は転載しない。

## 検証と制限

| コマンド/確認 | 結果 |
|---|---|
| git status --short（着手前） | 空。既存変更なし |
| node tools/check-site.js（着手前） | PASS：HTML65、内部リンク2194。既存のサイト検査エラーなし |
| node tools/check-site.js（実装後） | PASS：HTML66、内部リンク2225。FAQ/パンくず一致、構文、内部リンク、台帳、sitemap/draft制御を含む |
| python3 tools/agent-harness/run.py --output /workspace/scratch/9c3df2c2cb63/family-conversation-harness-final | 総合blocked、終了1。未コミット変更あり（今回の依頼どおり）。harness-regression/site/click-trackingは全てpassed（各終了0）。release_ready=false |
| python3 tools/agent-harness/test_runner.py（ハーネス内） | PASS：4 tests |
| node tools/check-click-tracking.js（ハーネス内） | PASS。初回に今回追加ページのgtag定義欠落を検出したが、既存テンプレートの定義を継承して修正済み |
| git diff --check | PASS |
| python3 /tmp/family-static-check.py | PASS。noindex・日付未設定・sitemap/公開一覧非掲載・PNG同一ハッシュ・統計・FAQ数・画像予約/srcset/eager属性。下書きと画像5件のローカルHTTP 200 |
| curl -L -sS -o /tmp/family-source1.html -w '%{http_code}\n' --max-time 30 <出典1URL>（出典2も同様） | 両方HTTP 200。本文の数値/母数/相談業務も確認 |
| node /tmp/verify-family-conversation.cjs | 実行不可：PlaywrightのChromium本体なし。/usr/bin/chromiumもリンク先実体なし |
| npx --yes playwright install chromium / 同梱playwright/cli.js install chromium | 失敗：配布サーバーHTTP 403。リポジトリにpackage/lockは作成していない |
| build/lint/型チェック | 独立script・設定がないため該当なし。既存のsite/計測/ハーネス検査で代替 |
| モバイル320/375/390px・デスクトップ1440px | 未検証：ブラウザ不足。画像ファイルの表示は確認したが、ページの実表示・メニュー・FAQ操作・CLS/LCP実測・実際のsrcset選択を合格としない |

ハーネスのreport/summaryは同ディレクトリへ保存。対象SHAは元HEADであり未コミット差分を含むため、コミット検証済みとは扱わない。静的検査詳細はstatic-verification.json。環境不足と実装エラー（修正済み）を区別する。

## 公開前に人が確認する事項

- 法務：希望のメモと代理権の区別、個人情報の同意/共有範囲、金融機関ごとの手続への誘導。個別契約の成立・権限を断定しない。
- 医療：話を嫌がることから認知症・判断能力低下を推定しない。診断・治療効果を説明せず医療機関へつなぐ。
- 税務：資産共有を贈与や名義変更の推奨にしない。税額・控除・申告の個別判断を追加しない。
- 統計：設問n=929と全体1,048人、43.5%＋26.5%=70.0%、企業調査の限界を保持する。合計を会話経験ゼロと読み替えない。
- 相談先：親の居住地の自治体公式案内を各自確認する導線。営業時間を一律に断定しない。架空のサービス・料金・実績なし。
- 画像：AI生成の架空人物である表示、人物・手指・ロゴ/個人情報の最終目視。実在の調査参加者と扱わない。
- UI：320/375/390/1440pxで横あふれ、画像読込、顔・主被写体、alt、領域予約、FAQ/メニュー操作、CLSを実測する。SNS側の実カード表示は未公開のため未検証。
- 公開作業の承認後にのみcolumnへ移動、noindex解除、実際の初回公開日を本文/構造化データ/台帳に設定。sitemap・一覧・カテゴリ・関連記事の受けリンクを同時更新し、検証を再実行する。今回はここで確認待ち。

## 変更ファイル一覧と目的

| ファイル | 目的 |
|---|---|
| `docs/seo/content-inventory.csv` | 新記事の下書き状態を追加 |
| `docs/seo/keyword-map.csv` | 検索意図と既存記事との境界を記録 |
| `docs/seo/ymyl-review-queue.md` | 専門事項・公開前確認点を記録 |
| `drafts/parent-care-family-conversation/index.html` | 原稿・画像・SEOの未公開実装 |
| `public/images/shukatsu/parent-care-family-conversation-hero-1672.webp` | 指定元画像と配信用の最適化画像 |
| `public/images/shukatsu/parent-care-family-conversation-hero-640.webp` | 指定元画像と配信用の最適化画像 |
| `public/images/shukatsu/parent-care-family-conversation-hero-960.webp` | 指定元画像と配信用の最適化画像 |
| `public/images/shukatsu/parent-care-family-conversation-hero.png` | 指定元画像と配信用の最適化画像 |
| `public/images/shukatsu/parent-care-family-conversation-ogp.webp` | 指定元画像と配信用の最適化画像 |
| `docs/seo/parent-care-family-conversation/article-draft.txt` | 原稿/画像由来と検証証拠を保存 |
| `docs/seo/parent-care-family-conversation/harness-report.json` | 原稿/画像由来と検証証拠を保存 |
| `docs/seo/parent-care-family-conversation/harness-summary.md` | 原稿/画像由来と検証証拠を保存 |
| `docs/seo/parent-care-family-conversation/image-details.txt` | 原稿/画像由来と検証証拠を保存 |
| `docs/seo/parent-care-family-conversation/static-verification.json` | 原稿/画像由来と検証証拠を保存 |
| `docs/seo/parent-care-family-conversation/implementation-review.md` | 重複判断・検証結果・未実施事項・人向けレビュー |
