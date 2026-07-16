# サイト現状調査（site-audit）

- 調査日: 2026-07-11（Asia/Tokyo）
- 調査方法: リポジトリ全ファイル精査＋本番URL（https://shukatsu-guide.jp/）のcurl確認＋自作リンクチェッカー実行
- 本番とリポジトリの差分: なし（main=e5ce09a 時点で一致確認。GitHub Pagesがmainを自動配信）

## 技術構成

| 項目 | 内容 |
|---|---|
| フレームワーク/CMS | なし（手書き静的HTML。SSG・ビルド工程なし） |
| ホスティング | GitHub Pages（リポジトリ tfqys680-jpg/shukatsu-site、mainブランチ/ルート） |
| ドメイン | shukatsu-guide.jp（CNAMEファイル＋Xserver DNS A×4/www CNAME、HTTPS強制） |
| デプロイ | main への push で自動反映（約30〜60秒） |
| ビルド/テスト | 専用ツールなし。品質検証は自作チェッカー（tools/check-site.js に本PRで正式移設） |
| 計測 | GA4 gtag直書き（G-M7NS8ZH6WL、全ページ）。体験談LPのみ lp_cta_click イベントあり |
| Search Console | sc-domain:shukatsu-guide.jp（DNS TXT認証済み・sitemap送信済み） |

## ディレクトリ構成（2026-07-11時点）

```
/ … index.html, about.html, privacy.html, disclaimer.html, robots.txt, sitemap.xml, CNAME, favicon.ico
/articles/ … article01〜15.html（記事データ=HTML直書き。frontmatter等なし）
/ending-note/family-story/ … 体験談LP（サブディレクトリ+index.html型）
/css/style.css … 共通CSS（CSS変数・コンポーネント・印刷CSSなし→本PRで追加）
/js/main.js … ナビ/スムーススクロール/to-top/スクロール演出
/images/ … favicon群・ogp.jpg・profile.webp・hero.webp
```

## URL・記事一覧（20ページ）

詳細は content-inventory.csv を参照。要点:
- title/meta description/canonical/OGP/Twitter Card: 全ページ固有・設定済み
- H1: 全ページ1つ
- 構造化データ: 記事=Article、トップ=WebSite+FAQPage、体験談LP=Article+FAQPage+BreadcrumbList
- パンくず: 全下層ページに表示あり。**BreadcrumbList JSON-LDは体験談LPのみ**（他ページは未実装→改修時に順次追加方針）
- 著者表示: 「執筆・監修：終活カウンセラー1級」（筆名なし。実名はリポジトリに存在しない→捏造禁止、運営者確認事項）
- 公開日/更新日: 記事は「最終更新日」表示+JSON-LDのdatePublished/dateModified。体験談LPのみ公開日と更新日を併記

## テクニカルSEO状況

| 項目 | 状態 |
|---|---|
| robots.txt | Allow all + Sitemap行。noindexなし（全ページ公開意図どおり） |
| sitemap.xml | 20URL（手動管理）。lastmod付き |
| 404ページ | **なし（GitHub Pagesデフォルト404）** → 改善候補（404.html） |
| リダイレクト | GitHub Pages機能なし。github.io→独自ドメインはPages側で301 |
| 重複title/description | なし（チェッカーは未検査→本PRでチェック追加） |
| 孤立ページ | なし（全ページがトップまたは記事から到達可能） |
| リンク切れ | なし（チェッカー530リンク通過） |
| 画像alt | コンテンツ画像はあり。計測ピクセルはalt="" |
| モバイル | 320/360/375/390pxで横スクロールなし検証済み |
| 速度 | 画像最適化済み（WebP/圧縮）。外部JSはgtagのみ。フォントはシステムフォント |
| 印刷CSS | **なし** → 本PRで追加 |

## カテゴリ構造・内部リンク

- 現状カテゴリは「トップの3カード（エンディングノート/遺言/デジタル遺品）」のみで、**ハブページが存在しない**
- 体験談LPが実質的なハブとして9記事へリンク済み
- 記事間リンクは相互に整備済み（internal-link-map.csv 参照）

## 検索意図の重複リスク（カニバリ）

| テーマ | 該当 | 判定 |
|---|---|---|
| エンディングノート必要性 | 体験談LP | 代表=LP。article01は「とは/違い」で棲み分けOK |
| 終活とは/やること/チェックリスト | article11 | 代表=article11（本PRでチェックリスト完全版へ拡張） |
| 親への切り出し方 | article05 | 代表=article05。30項目記事とは意図が異なる（聞く内容 vs 切り出し方）→アンカーで相互連結 |

## 既存の未コミット変更

なし（main=e5ce09a でクリーン。本作業は claude/seo-initial-2026-07-11 ブランチ上）

## アフィリエイト状況

- article08: Amazon/楽天 全10商品実リンク（もしも経由）。article09: 1位商品リンク。article10/12/13: 案件未確定（プレースホルダまたは未設置）
- 全ページに広告表記+Amazonアソシエイト文言あり

## 確認できなかった項目

- Search Consoleの検索クエリ実データ（サイト公開4日目でデータ蓄積中）
- 運営者の実名・相談実績の詳細（operator-interview-questions.md に確認事項として記録）
