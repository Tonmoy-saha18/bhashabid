# CLI Integration Unit Tests
import unittest
import subprocess
import sys
import os
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestCLI(unittest.TestCase):

    def run_cli(self, args: list[str]) -> tuple[int, str, str]:
        cmd = [sys.executable, "-m", "tools.cli"] + args
        p = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()

    def test_cli_number_words(self):
        code, out, _ = self.run_cli(["number", "99"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "নিরানব্বই")

    def test_cli_number_grouped(self):
        code, out, _ = self.run_cli(["number", "1234567", "--format", "grouped"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "১২,৩৪,৫৬৭")

    def test_cli_normalize(self):
        code, out, _ = self.run_cli(["normalize", "তিনি রেলষ্টেশনে গেলেন."])
        self.assertEqual(code, 0)
        self.assertEqual(out, "তিনি রেলস্টেশনে গেলেন।")

    def test_cli_lint_json(self):
        code, out, _ = self.run_cli(["lint", "তুমি সিদ্ধান্ত নেন", "--json"])
        self.assertEqual(code, 1) # Has error
        data = json.loads(out)
        self.assertGreater(len(data), 0)
        self.assertEqual(data[0]["rule_id"], "RULE-LINT-HONORIFIC-TUMI")
        self.assertIn("তুমি সিদ্ধান্ত নাও", data[0]["suggestion"])

    def test_cli_lint_clean(self):
        code, out, _ = self.run_cli(["lint", "আপনি কাল সকালে আসুন।"])
        self.assertEqual(code, 0)
        self.assertIn("কোনো ব্যাকরণগত বা বানানজনিত ত্রুটি পাওয়া যায়নি", out)

    def test_cli_install_and_uninstall(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdir:
            # Test CLI install-skill
            code, out, _ = self.run_cli(["install-skill", "--target", "cursor", "--workspace", tmpdir])
            self.assertEqual(code, 0)
            self.assertIn("successfully installed", out)

            # Test CLI uninstall-skill
            code, out, _ = self.run_cli(["uninstall-skill", "--target", "cursor", "--workspace", tmpdir])
            self.assertEqual(code, 0)
            self.assertIn("successfully removed", out)

if __name__ == "__main__":
    unittest.main()
