# Search Consoleデータの取り込み手順（search-console-import）

APIやMCPで直接アクセスできない環境でも定期分析できるよう、CSVエクスポート方式を標準とする。

## 手順（月1回・月初）

1. https://search.google.com/search-console （プロパティ: sc-domain:shukatsu-guide.jp）
2. 「検索パフォーマンス」→ 期間を「過去28日」に設定
3. 右上「エクスポート」→ CSV
4. zip内の以下を `docs/seo/sc-data/YYYY-MM/` に保存
   - ページ.csv（URL別）
   - クエリ.csv（検索語別）
5. Claude Code へ「docs/seo/sc-data/ の最新CSVを分析して」と依頼

## 記録テンプレート（分析結果は run-log.md に追記）

| URL | 主要クエリ | 表示回数 | クリック | CTR | 平均順位 | 前期間差 | 公開日 | 最終更新 | 判定 |
|---|---|---|---|---|---|---|---|---|---|

## 判定基準

- 公開2-4週: インデックス済みか（URL検査）／表示回数が発生しているか
- 公開4-8週: CTR低（表示>100でCTR<1%）→ title/description改善候補
- 公開8-12週: 平均順位11-30位のクエリ → 見出し追加・具体例・内部リンクでリライト
- 3-6ヶ月: クラスタ合計クリックの推移／カニバリ（同一クエリに複数URL）検出

実データがない期間に数値を推測で書かないこと。
