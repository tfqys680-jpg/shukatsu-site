> 現在の状態（2026-11-13）：運営者がコミット・プッシュ・PR・マージ・公開・デプロイを明示承認。下記は下書き段階の記録。末尾の公開準備記録を参照。

# 親の家のトイレ修理：実装・確認記録

2026-11-13（日本時間）。未公開・未コミットで確認待ち。

## 対象と判断

対象 tfqys680-jpg/shukatsu-site。取得した origin/main の基準SHA：4aacf46e20561e99ff04272a71986139d062295e。
既存作業場所の未コミット変更を保護するため独立cloneへ実装。既存作業場所は変更していない。
keyword-mapと記事群を照合。古い家電の記事は製品安全、実家の将来計画は所有・住まい方、本稿は緊急水回り修理の契約前準備であり新規追加が妥当。「トイレ 修理」の未完了PR検索は0件。

- 下書きパス：/drafts/parents-home-repair-cost-checklist/
- 公開予定URL：https://shukatsu-guide.jp/column/parents-home-repair-cost-checklist/ （未公開）
- 静的HTML、css/style.css、js/main.js、既存header/footer/FAQ detailsを使用。package.jsonなし。専用ビルド・lint・型チェック未定義。
- noindex、公開一覧とsitemapへの追加なし。新たな公開フラグの仕組みは増設していない。
- title/description/canonical/OGP/Article/BreadcrumbListを実装。canonical等は既存下書き方式どおり公開予定URL。未公開のためdatePublished/dateModifiedは未設定。公開時に実日付で追加が必要。
- FAQ3件は可視HTMLで維持。FAQPageは追加しない。Google公式更新履歴で2026-05-07 FAQリッチリザルト終了、06-15ドキュメント削除を確認：https://developers.google.com/search/updates 。既存記事の構造化データは変更していない。
- 原稿の全本文・出典4件・チェック7項目・人手確認事項を維持。原稿の制作指示のみHTMLコメント、CTA見出しのみ読者向け表記。原稿本文の欠落0件を文字列照合。原稿全文を別途バイト一致で保全。news-brief.txtは記事に混ぜていない。

## 画像

ZIP同梱PNGを指定の public/images/shukatsu/parents-home-repair-cost-hero.png へ配置。
PNG：1672×941、2,116,536 bytes。Pillow Lanczos縮小、WebP quality82/method6。

| 幅×高さ | bytes | PNG比削減 |
|---|---:|---:|
|640×360|29,628|98.6%|
|960×540|52,210|97.5%|
|1536×864|98,872|95.3%|

トリミングなし（縮小時の整数丸めのみ）。width/height、同率aspect-ratio、srcset3種、sizes指定。eager/high/async。既存724pxコンテンツ幅を維持。PCでは960w画像が読み込まれた。指定alt、架空AIイメージの注記あり。OGPとArticle画像は同じ元PNGの絶対URL、実寸指定。約16:9、人物の切り抜きなし。SNS側の自動切り抜き・実際の共有カード表示は未確認。本番画像URLは未公開なので本番疎通対象外。

## 検証

- node tools/check-site.js：成功。HTML59件、内部リンク2000件（最終実行参照）。JSON-LD/パンくず/タグ/アンカー/noindex/sitemap等。
- node tools/check-click-tracking.js：成功。初回gtag定義欠落を既存方式へ修正。
- python3 tools/agent-harness/test_runner.py：4テスト成功。
- python3 tools/agent-harness/run.py --output /workspace/scratch/2e7acbce5934/harness-final：各チェック成功、全体blocked。未コミット変更があるため。ユーザーのコミット禁止を優先し解消目的のコミットは作成しない。
- git diff --check：成功（CSV追加行の改行修正後）。
- 原稿本文の欠落0、FAQ3件・チェックリスト7項目、PNG原本と保存原稿のZIP一致確認。
- PC 1363px、iframe viewport320/375/390pxで目視。画像欠落・横はみ出しなし。スマホ幅では縦スクロールバー15pxを除いたclient幅305/360/375pxでscrollWidth一致。320pxのFAQ3開閉・回答表示を確認。
- CLS：画像領域予約とリサイズ比率を確認。PerformanceObserver/Lighthouse等の数値測定・実端末測定は未実施。CLS=0とは断定しない。
- build/lint/typecheck：専用コマンドなし、未実施。新規設定は増設しない。

## 残課題と人手確認

出典[1]は公式検索結果本文で照合、[2]はPDF本文照合済み。[3][4]は転送され元本文未照合。原稿側の11/13確認という表記を保持し、実装時の不足を冒頭注意書きとsource-policyに記録。公開前に移転後の正確な個別記事URLと原文を再照合する。
法務：支払義務・クーリング・オフ・賃貸修繕負担の一律断定がないか。個別の返金・法的効果は保証しない。
医療介護：年齢や認知症による判断能力の決めつけがないか。本人の意思・同意・情報共有範囲を尊重。
税務：控除・経費・相続評価は扱わない。追加時のみ税理士等による要件確認。
上記専門家レビューは未実施。監修者・サービス・被害者は創作していない。
公開直前に出典・188・内部リンク・最新mainとの整合、公開日、OGP実表示を確認する。

## 変更ファイル一覧

- drafts/parents-home-repair-cost-checklist/index.html
- public/images/shukatsu/parents-home-repair-cost-hero.png
- public/images/shukatsu/parents-home-repair-cost-hero-640.webp
- public/images/shukatsu/parents-home-repair-cost-hero-960.webp
- public/images/shukatsu/parents-home-repair-cost-hero-1536.webp
- docs/seo/content-inventory.csv
- docs/seo/keyword-map.csv
- docs/seo/ymyl-review-queue.md
- docs/seo/source-policy.md
- docs/seo/parents-home-repair-cost/article-draft.txt
- docs/seo/parents-home-repair-cost/image-details.txt
- docs/seo/parents-home-repair-cost/implementation-review.md

コミット・プッシュ・PR作成・マージ・公開・デプロイは一切実施していない。


## 2026-11-13 公開準備記録

運営者の追加指示で公開へ移行。column/へ移動しnoindexを解除、公開日・実質更新日を11月13日に設定。トップ新着・全記事一覧、親の終活ハブ、sitemap、content-inventory、keyword-map、internal-link-map、editorial-calendarを同期した。共通部のリンク追加は実質的な本文更新ではないため既存ページのdateModifiedは変更しない。
出典[3][4]の内容は公式検索結果全文で照合済み。転送の注意と現存する公式PDF・消費者庁の補足資料を案内。専門家レビュー未実施表示を保持し、監修済みとは表示しない。記事本文と指定画像は維持。変更ファイルは下書き一覧に加えindex.html、parent-shukatsu/index.html、sitemap.xml、internal-link-map.csv、editorial-calendar.csv。記事HTMLの配置先はcolumn/parents-home-repair-cost-checklist/index.html。
検証はコミット後に共通ハーネスを実行し、PRのCI結果と対象SHAを確認する。GitHub Pagesはmainマージにより配信される。デプロイ成功と本番疎通は外部の実行結果で別途確認し、準備段階では完了と扱わない。
