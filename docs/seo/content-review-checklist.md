# 記事公開前チェックリスト（content-review-checklist）

## 内容

- [ ] 冒頭に結論がある
- [ ] チェックリスト/手順/会話例など「そのまま使える」要素がある
- [ ] 体験談と一般解説が区別されている
- [ ] 存在しない体験・実績・数値・価格を書いていない
- [ ] 金額・期限・制度は一次情報＋確認日つき（source-policy.md に台帳記録）
- [ ] 断定的な法務・税務・医療助言がない／専門家への境界線を明示
- [ ] 不安を煽る表現・「必ず」「絶対」がない
- [ ] パスワードの平文一覧化を促していない

## SEO・構造

- [ ] title固有／description固有／H1は1つ／見出し階層が正しい
- [ ] canonical（サブディレクトリ型は末尾スラッシュ）
- [ ] OGP・og:image
- [ ] Article(+FAQPage/BreadcrumbList) JSON-LDが表示内容と一致
- [ ] パンくず表示
- [ ] keyword-map.csv に登録し、既存ページと検索意図が重複していない
- [ ] 内部リンク（柱⇄個別の双方向）／自然なアンカーテキスト
- [ ] sitemap.xml へ追加（下書きは追加しない）

## 品質ゲート

- [ ] `node tools/check-site.js` 全通過
- [ ] 320px/375pxで横スクロールなし
- [ ] PDF等の添付はリンク切れなし・A4印刷確認・版番号あり

## 運用

- [ ] dateModifiedは実質更新時のみ
- [ ] YMYL該当箇所は ymyl-review-queue.md へ登録
- [ ] run-log.md / automation-state.json を更新
