# PR #48 統合・公開前レビュー（2026-10-19 JST）

対象: https://github.com/tfqys680-jpg/shukatsu-site/pull/48

## 統合した状態

- 起点: PR #48 `48d8195c87e6142407df956ec8d8705c043f3071`、main `c2cd9e5068d4ca6ed85d62cdb4a9d437c65151f5`。
- 最新mainをPRブランチへマージ。競合は `automation-state.json`、`internal-link-map.csv`、`run-log.md` の3件。両方の記録を残し、実行状態だけを現在の事実に更新。
- `/parent-shukatsu/jikka-katazuke/` の本文・会話例・FAQ・構造化データは初稿のまま保持。トップ・親の終活ハブ・article12からの導線を保持。
- mainの生前墓記事（PR #49）、画像、article14・トップの導線、台帳、sitemap、出典・税務レビュー待ちを保持。他の未マージPRの本文は取り込んでいない。
- internal-link-mapの複数リンク元を3行へ分割し、本文にあるarticle10への相談リンクを追記。「相互リンク」はhub/article12のみに限定。keyword-mapのリンク先にもarticle10を追記。
- inventory・keyword-map・calendarはPR #48が未公開であると明記。last_new_articleは公開済みの生前墓記事を維持。

## 検証

- `node tools/check-site.js`: ALL CHECKS PASSED（HTML 41、内部リンク1,288）。
- `node tools/check-click-tracking.js`: PASSED（公開パスHTML 37、affiliate 34、CTA 13、商品12）。公開パスとはこのブランチ内の配置を指し、本番公開件数ではない。
- `git diff --check`: PASS。
- 追加監査: CSV列数・URL重複、新記事の台帳/FAQ/日付/導線、既存sitemapエントリとlastmodの維持、mainの既存本文・リンクと履歴の保持を確認。
- ブラウザ表示・印刷: 未検証。PlaywrightパッケージはあるがChromium実行ファイルがない。表示合格とは扱わない。
- GitHub CIの成功とは別のローカル検証。チェック実行数はPRの最新コミットで確認する。

## 他PRとの競合と順序

2026-10-19取得のheadに対するローカル3-way統合試行。#43/#44/#47は実際のgit履歴、#45/#50/#51/#52はGitHub取得のmainとの差分から同じ内容のテキストツリーを再構成した。#51の独立した新規WebPはテキスト競合試行の対象外。下表はこのPRの解消後ツリーをmainへ取り込んだ場合の競合であり、GitHubの将来のmergeable値を保証しない。

| PR | #48統合後に衝突するファイル（docs/seo/は省略） | 判断・進め方 |
|---|---|---|
| #47 | keyword-map.csv | 最優先の小修正。最新mainへ追従し、4点表記・既存更新日の整合を確認。 |
| #45 | automation-state.json、editorial-calendar.csv | #48より先に入れる候補。Apple/Google機能の現行仕様確認後に判断。article06の新表題をindex/hub/article12へ残す。 |
| #48 | 現在のmainとの競合は解消 | #47や#45が先にマージされた場合は再追従・再検証。公開前判断は次節。 |
| #44 | automation-state.json、content-inventory.csv、source-policy.md、sitemap.xml | 相続放棄等の期限記述の確認後。古い台帳やlastmodで最新mainを上書きしない。 |
| #43 | automation-state.json、content-inventory.csv、internal-link-map.csv、keyword-map.csv、run-log.md、source-policy.md | 専門家レビュー・実表示確認が残るため保留。noindexでもmainへ入ればアクセス可能。 |
| #51 | content-inventory.csv、internal-link-map.csv、keyword-map.csv、run-log.md | 公式原文・契約/介護記述のレビュー後。drafts/noindex/sitemap非掲載を保持。 |
| #50/#52 | automation-state.json、run-log.md | 状況レポートは最後。10/12・10/19の履歴は残し、現在のlast_new_article等へ古い値を戻さない。 |

推奨は **#47 → #45 → #48 → #44 → レビュー済みの#43/#51 → #50/#52の記録整理**。#44や下書きの未解決レビューを待って他の記事を止める依存関係はない。公開前確認の完了状況に応じて順序を変えてよい。いずれもmainの更新ごとに取り込み・台帳の和集合・両検証をやり直す。順序だけで全競合は消えない。

## 記事内容と公開可否の判断材料

- 原稿には親本人の同意、処分の保留、一般的な会話例であること、専門家へ相談する境界がある。これらを維持し、一般的な片付け手順としてレビュー可能にした。
- 認知症の疑い・溜め込みの相談、不動産・相続・業者の案内には医療/法務等への接点がある。原稿には直接の一次資料リンクがなく、低YMYLという分類だけで「専門家レビュー不要」と断定しない。公開前に運営者が該当箇所の根拠とレビュー要否を確認する。`ymyl-review-queue.md` に登録。
- 表示・Article・inventory・keyword・sitemapの新記事日付は初稿の `2026-10-05` で一致するが、実際の公開日ではない。公開時に初公開日・実質更新日を確定し、表示・構造化データ・両台帳・sitemapを同期する。既存記事のリンク追加のみを理由に更新日は進めない。
- main由来の既存差分: living-aloneのkeyword更新日/3点表記は#47で修正予定。where-to-askのkeyword最終更新日は2026-09-06、本文/inventory/sitemapは2026-10-02。本PRはこの既存の行を変更せず、次の台帳整理時に実質更新内容を照合する。新記事を追加したことによる日付ドリフトとは区別する。
- レビュー可能への切替は公開許可を意味しない。mainへのマージでGitHub Pagesに配信される。本対応ではマージ・公開を行わない。
