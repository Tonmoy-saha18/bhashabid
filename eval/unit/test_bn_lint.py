# Unit Tests for bn_lint
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_lint import lint_text, LintSeverity

class TestBnLint(unittest.TestCase):

    def test_clean_text_no_issues(self):
        text = "তিনি প্রতিদিন সকালে বিদ্যালয়ে যান এবং পাঠদান করেন।"
        issues = lint_text(text)
        self.assertEqual(len(issues), 0)

    def test_guru_chandali_detection(self):
        # Mixing 'আসিয়া' (Sadhu) with 'গেল' (Cholito)
        text = "তিনি বাড়িতে আসিয়া ভাত খেলেন এবং বাজারে গেল।"
        issues = lint_text(text)
        self.assertTrue(any(i.rule_id == "RULE-LINT-GURU-CHANDALI" for i in issues))

    def test_honorific_clash_detection(self):
        # 'আপনি' with 'করো'
        text = "আপনি কি কাজটি আজ করো?"
        issues = lint_text(text)
        self.assertTrue(any("HONORIFIC" in i.rule_id for i in issues))

    def test_calque_detection(self):
        text = "এই মেশিনটি বিদ্যুৎ দ্বারা চালিত এবং কাজটি তিনি দ্বারা কৃত।"
        issues = lint_text(text)
        self.assertTrue(any(i.rule_id == "RULE-LINT-CALQUE" for i in issues))

if __name__ == "__main__":
    unittest.main()
