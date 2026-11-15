#!/usr/bin/env bash
# pipeline.py の結果を受けて、コミット→検証→PR→（条件を満たせば）自動マージ・公開する。
# GitHub Actions（.github/workflows/auto-publish.yml）から呼ばれる。
set -euo pipefail

RESULT="$1"
EVIDENCE="${RUNNER_TEMP:-/tmp}/auto-publish-harness"
status=$(jq -r .status "$RESULT")
slug=$(jq -r '.slug // "none"' "$RESULT")
auto_merge=$(jq -r '.auto_merge // false' "$RESULT")
today=$(TZ=Asia/Tokyo date +%F)
run_url="${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}"

notify() { # $1=title $2=body
  gh issue create --title "$1" --body "$2"$'\n\n'"実行ログ: ${run_url}" --label auto-publish >/dev/null || true
}

case "$status" in
  skipped) echo "nothing to do: $(jq -r .reason "$RESULT")"; exit 0 ;;
  error)   notify "自動記事パイプラインのエラー（${today}）" "$(jq -r .reason "$RESULT")"; exit 1 ;;
esac

if git diff --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "no changes"; exit 0
fi

branch="auto-publish/${today}-${slug}"
git config user.name "auto-publish[bot]"
git config user.email "auto-publish@users.noreply.github.com"
git switch -c "$branch"
git add -A
if [ "$status" = "created" ]; then
  msg="自動記事: $(jq -r .title "$RESULT")"
else
  msg="自動記事パイプライン: ${slug} を保留"
fi
git commit -q -m "$msg" -m "ChatGPT下書き・Claude審査の自動パイプライン（tools/auto-publish）。$(jq -r '.reason // ""' "$RESULT")"

# 既存の検証ハーネス（check-site / check-click-tracking / パイプラインのテスト）
harness_ok=true
python3 tools/agent-harness/run.py --output "$EVIDENCE" || harness_ok=false

git push -q -u origin "$branch"

body=$(mktemp)
{
  echo "## 自動記事パイプライン（ChatGPT × Claude）"
  echo
  echo "- 結果: ${status}"
  [ "$status" = "created" ] && echo "- 記事: $(jq -r .title "$RESULT")（$(jq -r .url "$RESULT")）"
  echo "- YMYL区分: $(jq -r '.ymyl // "-"' "$RESULT")"
  echo "- 自動マージ対象: ${auto_merge}"
  echo "- 検証ハーネス: $([ "$harness_ok" = true ] && echo passed || echo failed)"
  [ "$status" = "blocked" ] && echo "- 保留理由: $(jq -r .reason "$RESULT")"
  echo
  echo "### Claudeの審査指摘"
  jq -r '(.issues // [])[] | "- " + .' "$RESULT"
  echo
  [ -f "$EVIDENCE/summary.md" ] && cat "$EVIDENCE/summary.md"
  echo
  echo "実行ログ: ${run_url}"
  echo
  echo "AIで作成し自動公開する記事です。専門家レビューは未実施です。"
} > "$body"

pr_url=$(gh pr create --base main --head "$branch" --title "$msg" --body-file "$body" --label auto-publish)
echo "PR: $pr_url"

if [ "$harness_ok" = true ] && [ "$auto_merge" = true ]; then
  gh pr merge "$pr_url" --squash --delete-branch
  # GITHUB_TOKEN による push では Pages の再ビルドが走らないことがあるため明示的に依頼する
  gh api -X POST "repos/${GITHUB_REPOSITORY}/pages/builds" >/dev/null 2>&1 || echo "pages build request skipped"
  echo "merged and published"
  if [ "$status" = "blocked" ]; then
    notify "自動記事を保留しました（${today}・${slug}）" "品質基準を満たさなかったため公開していません（キューの状態を「保留」に更新済み）。理由: $(jq -r .reason "$RESULT")"
  fi
elif [ "$harness_ok" != true ]; then
  notify "自動記事の検証に失敗（${today}・${slug}）" "検証ハーネスが通らなかったため自動マージしていません。PR: ${pr_url}"
  exit 1
else
  notify "自動記事の確認依頼（${today}・${slug}）" "高YMYLのため自動マージしていません。内容を確認してマージしてください。PR: ${pr_url}"
fi
