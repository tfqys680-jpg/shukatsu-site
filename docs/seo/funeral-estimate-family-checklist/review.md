# 葬儀の見積もり補足：公開反映記録

2026年11月21日（日本時間）。運営者が「補足の文章として使用出来るなら追記、蛇足なら掲載しない」と指示し、改訂下書きを確認後、公開・デプロイ・コミット・プッシュ・PR作成・マージを明示承認。

## 変更

反映先は既存 `/articles/article13.html`。同じ検索意図の新規URLは作らず、費用節に「含む・別途・未定」、質問例、増減条件、記録保存を統合。原稿のチェックリスト6項目、FAQ3件、CTA、公式出典、契約上の注意事項を維持。元の希望整理は既存sec4を活用して重複を避けた。news-brief.txtは本文に混ぜていない。

未確認の既存相談者の発言は一般的な説明へ整理。「比較できるのは生前だけ」「相談は無料」といった断定を避け、事前の比較と依頼前の料金確認を提案。価格固定・返金・取消し等を保証せず、消費生活センター・必要に応じ弁護士への案内、追加箇所の法律専門家レビュー未実施を明記。

公開日2026-07-07は保持し、実質更新日・Article dateModified・sitemap lastmod・content-inventory・keyword-mapを2026-11-21に同期。canonical、Article mainEntityOfPage、og:urlは既存URLを保持。本文とFAQPageの一致を検証。公開版のindex,followと本番GA設定を確認。

## 画像

ZIP内のPNG原本1672×941を `public/images/shukatsu/funeral-estimate-family-hero.png` へ配置。WebPは640×360（25,316 bytes）、960×540（45,156 bytes）、1600×900（95,614 bytes）。OGPは全画面を使う1200×675（81,450 bytes）。人物の追加トリミングなし。指定alt、width/height、srcset/sizes、レスポンシブ指定を設定。主要画像にfetchpriority=high、lazy指定なし。生成AIによる架空の家族のイメージと明記。

## 出典

国民生活センター「もしもの時に慌てないように！葬儀の料金トラブル」
https://www.kokusen.go.jp/mimamori/mj_mailmag/mj-shinsen558.html
2026-11-19公表、2026-11-21原文照合。公的助言と編集提案を区別し、相談事例の文章・画像は転載しない。

## 検証と制約

コミット前のnode tools/check-site.js、node tools/check-click-tracking.jsを実施し、コミット後に共通ハーネスの3チェックを実行する。実際の結果はPRとチェックアウト外の証跡に記録する。

package.json・独立したbuild/lint/型チェック設定は存在せず、README指定の既存チェックが検証入口。ローカルブラウザーはChromiumのsocket操作制限で起動できず、代替ブラウザーもローカルページへ接続できないため、PC/スマホ320/375/390px表示と実測LCP/CLSは未確認。画像寸法・参照・CSSは静的確認済み。実機確認や専門家レビューを実施済みとは扱わない。

公開後の反映状況はPR・デプロイと本番確認の結果で判断する。下書きの複製は公開せず、今回反映する記事だけを既存URLで更新する。
