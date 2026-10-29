import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True

spec = importlib.util.spec_from_file_location('runner', Path(__file__).with_name('run.py'))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class HarnessTests(unittest.TestCase):
    def test_failure_does_not_hide_later_checks(self):
        with tempfile.TemporaryDirectory() as root:
            result = runner.evaluate([
                {'id': 'fail', 'command': [sys.executable, '-c', 'raise SystemExit(7)']},
                {'id': 'pass', 'command': [sys.executable, '-c', 'print("evidence")']},
            ], root)
        self.assertEqual([r['status'] for r in result], ['failed', 'passed'])
        self.assertEqual(result[0]['exit_code'], 7)
        self.assertIn('evidence', result[1]['output'])

    def test_unavailable_command_blocks(self):
        result = runner.run_check({'id': 'missing', 'command': ['nonexistent-harness-command']}, '.')
        self.assertEqual(result['status'], 'blocked')

    def test_timeout_is_not_pass(self):
        result = runner.run_check({'id': 'timeout', 'command': [sys.executable, '-c',
                                  'import time; time.sleep(10)'], 'timeout_seconds': 0.05}, '.')
        self.assertEqual(result['status'], 'timeout')

    def test_empty_duplicate_or_shell_commands_rejected(self):
        for checks in [[], [{'id': 'x', 'command': 'echo ok'}],
                       [{'id': 'x', 'command': ['echo']}] * 2]:
            with self.assertRaises(ValueError):
                runner.evaluate(checks, '.')


if __name__ == '__main__':
    unittest.main()
