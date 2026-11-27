# 公開対応レビュー（2026-11-27）

運営者から「公開・コミット・プッシュ・PR操作」の指示を受領。初回の未公開実装の制限を今回の依頼範囲で更新した。公開による既存記事の削除・大幅統合は行わない。

## 変更

- 公開先：`/column/parent-care-family-conversation/`。noindexを解除し、本文・Article・content-inventory・keyword-mapの初回公開日/更新日を2026-11-27に設定（実際の公開予定当日）。出典公表日は流用しない。
- 指定PNGとWebP3サイズ・OGPはそのまま使用。本文・統計の母数区別・編集提案表示・専門事項の注意事項も維持。
- sitemap、新着3本、全記事一覧、親の終活ハブ、30項目記事の関連記事から導線を追加。導線を実質追加したトップ/ハブ/30項目の更新日とsitemap/台帳も整合。
- 初回実装の記録（implementation-review、harness-report/summary、static-verification）は当時の下書き検証の履歴として保持。最新状態は本資料とpublication-browser-verificationを参照。

## 最新の検証

- `node tools/check-site.js`：PASS、HTML66、内部リンク2228。FAQ3件/パンくずDOM↔JSON-LD一致、台帳・sitemap整合を含む。
- `node tools/check-click-tracking.js`：PASS、public HTML62・affiliate38・CTA13・products12。
- `git diff --check`：PASS。
- `node /tmp/verify-family-publication.cjs`：PASS。GoogleのChrome for Testing公式配布からChrome headless 131.0.6778.204を取得して実行（最初の配布URLの403を回避）。デスクトップChromiumによる画面幅検証であり、iOS実機検証ではない。
- 320/375/390/1440pxで画像読込・alt・width/height・srcset選択・日付・index/follow・FAQ表示/開閉・横あふれなし・JS例外なしを確認。画面幅320/375/390は640w、1440は960wのWebPを選択。測定区間のCLS=0（ネットワーク/端末条件が異なる実運用の値を保証しない）。
- ローカルの内部リンク18件はHTTP 200、リンク切れ0。ヒーロー/OGPに人物の切れなし。スマートフォン/デスクトップのスクリーンショットで目視。
- 共通ハーネスはコミット後にクリーンなツリーで実行し、対象SHA/全チェック結果を確認してからpush/PRへ進む。結果は実行ログとPR本文へ記録する。
- 専用build/lint/型チェック設定はなし。既存CIのハーネス/site/計測検査を実行する。

## 残る制限

- 専門家の法務/医療/税務の監修は未実施。個別判断をせず確認先を案内する注意事項を保持。
- 統計（設問929人/全体1,048人・43.5%+26.5%=70.0%）は発表主体の資料と照合済み。7割を会話経験ゼロとしない。企業調査の限界を明記。
- 本番反映の到達性・画像・sitemap・公開メタはマージ後に確認する。検索登録・SNSカードキャッシュ更新は保証しない。
