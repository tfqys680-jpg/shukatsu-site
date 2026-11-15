#!/usr/bin/env python3
"""自動記事パイプラインの通しテスト（APIと出典取得はモック）。

リポジトリを一時ディレクトリへ複製し、pipeline.py を実行してから
tools/check-site.js と tools/check-click-tracking.js が通ることを確認する。
実行: python3 tools/auto-publish/tests/test_pipeline.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SRC1 = "https://www.example.go.jp/nengajo"
SRC2 = "https://www.example.lg.jp/contact"


def sample_article():
    para = ("年賀状のやり取りをやめるかどうかは、親本人の気持ちを確かめてから決めます。"
            "長年続けてきた相手には、感謝の言葉を添えて伝えると受け取る側も安心しやすくなります。")
    sections = []
    for i in range(1, 7):
        sections.append({"heading": f"見出し{i}：年賀状じまいの進め方",
                         "blocks": [{"type": "p", "text": para * 4 + "[1]"},
                                    {"type": "h3", "text": f"小見出し{i}"},
                                    {"type": "ul", "items": ["相手の名前を確認する", "連絡手段を確認する [2]"]},
                                    {"type": "example", "label": "会話例", "lines": ["子：来年の年賀状、どうしたい？", "親：少し減らしたいね。"]},
                                    {"type": "table", "headers": ["相手", "連絡方法"], "rows": [["親戚", "電話"], ["友人", "手紙"]]}]})
    return {
        "title": "年賀状じまいを親と進めるには？伝え方と連絡先の整理手順",
        "breadcrumb": "年賀状じまいを親と進める",
        "description": "年賀状じまいを親と一緒に進めるための手順を紹介。本人の希望の確かめ方、相手ごとの伝え方、連絡先の整理と引き継ぎのポイントをチェックリストで整理します。",
        "conclusion": "年賀状じまいは、親本人の希望を確かめ、相手ごとに伝え方を決めてから進めると無理がありません。",
        "can_do": ["本人の希望を確かめられる", "伝え方を選べる", "連絡先を整理できる"],
        "lead": para,
        "sections": sections,
        "checklist": ["本人の希望を聞いた", "相手を一覧にした", "伝え方を決めた", "連絡先の保管場所を決めた", "家族と共有した"],
        "faq": [{"q": "いつ伝えればよいですか？", "a": "本人の都合のよい時期を選びます。[1]"},
                {"q": "全員にやめると伝えるべきですか？", "a": "相手ごとに決めて構いません。"},
                {"q": "連絡先はどう残しますか？", "a": "保管場所を家族と共有します。"}],
        "next_step": "まずは親と一緒に、年賀状を送っている相手を一覧にしてみましょう。",
        "sources": [{"title": "テスト省「年賀状について」", "url": SRC1, "note": "テスト"},
                    {"title": "テスト市「連絡先の整理」", "url": SRC2, "note": "テスト"}],
        "related": ["/articles/article11.html", "/parent-shukatsu/questions/", "/articles/article05.html"],
    }


def write_fixtures(d, verdict="PASS", ymyl="低"):
    d.mkdir(parents=True, exist_ok=True)
    art = sample_article()
    (d / "openai_1.json").write_text(json.dumps(art, ensure_ascii=False), encoding="utf-8")
    (d / "claude_1.json").write_text(json.dumps({"verdict": verdict, "ymyl": ymyl, "issues": ["テスト指摘"], "article": art},
                                                ensure_ascii=False), encoding="utf-8")
    (d / "sources.json").write_text(json.dumps({SRC1: "出典本文" * 100, SRC2: "出典本文" * 100}, ensure_ascii=False), encoding="utf-8")


class PipelineTest(unittest.TestCase):
    def run_case(self, verdict, ymyl):
        tmp = Path(tempfile.mkdtemp(prefix="auto-publish-test-"))
        site = tmp / "site"
        shutil.copytree(REPO, site, ignore=shutil.ignore_patterns(".git", "node_modules"))
        write_fixtures(tmp / "fx", verdict, ymyl)
        env = dict(os.environ, AUTO_PUBLISH_ROOT=str(site), AUTO_PUBLISH_MOCK=str(tmp / "fx"), AUTO_PUBLISH_DATE="2026-11-18")
        res = tmp / "result.json"
        subprocess.run([sys.executable, str(site / "tools/auto-publish/pipeline.py"), "--result", str(res)], env=env, check=True,
                       capture_output=True)
        return site, json.loads(res.read_text(encoding="utf-8"))

    def checks_pass(self, site):
        for script in ("tools/check-site.js", "tools/check-click-tracking.js"):
            p = subprocess.run(["node", script], cwd=site, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_pass_low_ymyl_is_published(self):
        site, r = self.run_case("PASS", "低")
        self.assertEqual(r["status"], "created", r)
        self.assertTrue(r["auto_merge"])
        page = (site / "column/nengajo-jimai-family-guide/index.html").read_text(encoding="utf-8")
        self.assertIn("生成AI（ChatGPT）で下書き", page)
        self.assertIn('href="#source1"', page)
        self.assertIn("column/nengajo-jimai-family-guide/", (site / "index.html").read_text(encoding="utf-8"))
        self.assertIn("公開(2026-11-18)", (site / "docs/seo/auto-queue.csv").read_text(encoding="utf-8"))
        self.checks_pass(site)

    def test_high_ymyl_waits_for_review(self):
        site, r = self.run_case("PASS", "高")
        self.assertEqual(r["status"], "created")
        self.assertFalse(r["auto_merge"])
        self.checks_pass(site)

    def test_block_creates_no_page(self):
        site, r = self.run_case("BLOCK", "低")
        self.assertEqual(r["status"], "blocked")
        self.assertFalse((site / "column/nengajo-jimai-family-guide").exists())
        self.assertIn("保留(2026-11-18)", (site / "docs/seo/auto-queue.csv").read_text(encoding="utf-8"))
        self.checks_pass(site)


if __name__ == "__main__":
    unittest.main(verbosity=2)
