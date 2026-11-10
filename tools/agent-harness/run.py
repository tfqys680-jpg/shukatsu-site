"""Run repository-owned checks without AI credentials or production mutations."""
import argparse
import datetime
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def run_check(check, root):
    start = time.monotonic()
    try:
        proc = subprocess.Popen(check['command'], cwd=root, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True,
                                start_new_session=os.name != 'nt')
        try:
            output, _ = proc.communicate(timeout=check.get('timeout_seconds', 180))
            status = 'passed' if proc.returncode == 0 else 'failed'
        except subprocess.TimeoutExpired:
            if os.name != 'nt':
                os.killpg(proc.pid, signal.SIGKILL)
            else:
                proc.kill()
            output, _ = proc.communicate()
            status = 'timeout'
        code = proc.returncode
    except OSError as exc:
        status, code, output = 'blocked', None, str(exc)
    return dict(id=check['id'], command=check['command'], status=status,
                exit_code=code, seconds=round(time.monotonic() - start, 3),
                output=output[-30000:])


def evaluate(checks, root):
    if not checks or len({c['id'] for c in checks}) != len(checks):
        raise ValueError('Checks must be nonempty with unique IDs')
    for c in checks:
        if (not isinstance(c.get('command'), list) or not c['command']
                or not all(isinstance(x, str) and x for x in c['command'])
                or not isinstance(c.get('timeout_seconds', 180), (int, float))
                or not 0 < c.get('timeout_seconds', 180) <= 900):
            raise ValueError('Invalid command or timeout')
    return [run_check(c, root) for c in checks]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='Directory outside the checkout')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = Path(args.output).resolve()
    if out == root or root in out.parents:
        parser.error('Evidence must be outside the checkout')
    out.mkdir(parents=True, exist_ok=True)
    # Overwrite old evidence before execution so a failed run cannot reuse a pass.
    report = dict(schema_version=1, status='blocked', release_ready=False,
                  started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), checks=[])
    target = out / 'report.json'
    target.write_text(json.dumps(report), encoding='utf-8')
    try:
        git = lambda *a: subprocess.check_output(['git', *a], cwd=root, text=True).strip()
        report['commit'] = git('rev-parse', 'HEAD')
        report['dirty_before'] = bool(git('status', '--porcelain'))
        config = json.loads((root / 'tools/agent-harness/config.json').read_text())
        report['manual_review'] = config['manual_review']
        report['checks'] = evaluate(config['checks'], root)
        report['dirty_after'] = bool(git('status', '--porcelain'))
        report['status'] = ('passed' if all(c['status'] == 'passed' for c in report['checks'])
                            and not report['dirty_before'] and not report['dirty_after'] else 'blocked')
    except Exception as exc:
        report['error'] = str(exc)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# Agent verification', '', 'Status: ' + report['status'],
             'Commit: ' + report.get('commit', 'unknown'), '',
             'This is automated verification only; release approval is not granted.', '']
    lines += [f"- {c['id']}: {c['status']} ({c['seconds']}s)" for c in report['checks']]
    lines += ['', '## Required review'] + ['- ' + s for s in report.get('manual_review', [])]
    (out / 'summary.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    return 0 if report['status'] == 'passed' else 1


if __name__ == '__main__':
    sys.exit(main())
