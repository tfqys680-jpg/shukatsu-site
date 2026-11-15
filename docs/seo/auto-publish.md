# 自動記事パイプライン（ChatGPT × Claude）

2026-11-15 運営者の指示（「ChatGPTと協力して全自動できるようにしてください。全権限を委任します」）により導入。公開方法は運営者が「完全自動で公開」を選択した。

## 何をするか

毎週火曜 06:17（JST）に GitHub Actions（`.github/workflows/auto-publish.yml`）が次を行う。

1. `docs/seo/auto-queue.csv` から「待機」のテーマを1件選ぶ。空なら ChatGPT がテーマを提案し、Claude が重複・品質で選別して補充する。
2. ChatGPT が記事原稿（JSON）を作る。
3. 原稿の出典URLを実際に取得し、本文を Claude に渡して照合・推敲する（最大2回）。裏付けのない具体的な記述は削除または「窓口で確認」に書き換える。
4. 機械検証（`tools/auto-publish/pipeline.py` の validate）: 禁止表現、架空の体験・監修、エンディングノートの法的効力の無限定な否定、出典番号、取得できた出典2件以上、構成、文字数、許可した内部リンクのみ。
5. `column/<slug>/` を生成し、トップの新着・全記事一覧、sitemap、content-inventory、keyword-map、editorial-calendar、internal-link-map、run-log、automation-state を更新。
6. ブランチ `auto-publish/<日付>-<slug>` にコミットし、既存の検証ハーネス（check-site・check-click-tracking・本パイプラインのテスト）を実行してPRを作成。
7. 検証が通り、YMYL区分が「低」「中」なら自動でスカッシュマージし、GitHub Pages の再ビルドを依頼する。

## 自動公開しないもの（安全装置）

- Claude の審査が PASS でない、または機械検証に1つでも落ちた記事 → 記事は作らず、キューを「保留」にして Issue で通知。
- YMYL区分が「高」（相続・税・法律・医療の判断を扱う）→ PRを開いたまま Issue で確認依頼。運営者がマージするまで、次の自動実行は止まる。
- 検証ハーネスが失敗 → マージせず Issue で通知。

記事にはAIで作成したこと・専門家レビュー未実施であることを明記し、著者は「はじめての終活ガイド編集部」とする（運営者の体験・相談実績に帰属させない）。アイキャッチは付けず、OGPはサイト共通画像を使う。アフィリエイトリンクは自動では追加しない。

## 初期設定（運営者が行う）

GitHub のリポジトリ設定で次を登録する。

| 種類 | 名前 | 値 |
| --- | --- | --- |
| Secret | `OPENAI_API_KEY` | OpenAI の API キー |
| Secret | `ANTHROPIC_API_KEY` | Anthropic の API キー |
| Variable | `OPENAI_MODEL` | 使う ChatGPT のモデル名 |
| Variable | `ANTHROPIC_MODEL` | 使う Claude のモデル名 |
| Variable | `AUTO_PUBLISH_ENABLED` | `true`（これ以外で停止） |

あわせて Settings → Actions → General → Workflow permissions で「Read and write permissions」と「Allow GitHub Actions to create and approve pull requests」を有効にする。

モデル名は共通ハーネスの方針どおりコードに固定しない。

## 運用

- テーマの追加・並べ替え・除外は `docs/seo/auto-queue.csv` を編集する（状態が「待機」の行だけが対象。YMYL区分は審査結果と比べて重い方を採用）。
- 手動実行: Actions → auto-publish → Run workflow。
- 停止: Variable `AUTO_PUBLISH_ENABLED` を `false` にする。
- 公開後に問題が見つかった記事は、通常の手順（ブランチ＋PR）で修正・非公開化する。
- 保留になった原稿は `tools/auto-publish/last-rejected.json` に残る。

## 既存の週次SEOルーチンとの関係

`.claude/prompts/shukatsu-seo-routine.md` の週次ルーチンは引き続き別に動く。`auto-queue.csv` に載っているテーマと `auto-publish/` ブランチは本パイプラインの担当とし、週次ルーチンは同じテーマの記事を作らない。週次ルーチン側の「レビュー待ちYMYL記事の自動公開」「デフォルトブランチへの直接マージ」の禁止は、週次ルーチン自身の作業に適用される。本パイプラインは運営者の上記指示に基づく例外で、マージは検証済みPR経由で行う。

## テスト

```
python3 tools/auto-publish/tests/test_pipeline.py
```

APIと出典取得をモックにして、公開・高YMYL・保留の3パターンを通しで確認し、生成後のサイトで check-site と check-click-tracking が通ることを確かめる。
