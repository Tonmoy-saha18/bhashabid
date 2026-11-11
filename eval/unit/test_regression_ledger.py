# Ledger Regression Harness
import unittest
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_numbers import number_to_bangla_words

class TestLedgerRegressions(unittest.TestCase):

    def test_all_resolved_mistakes_in_ledger(self):
        ledger_path = os.path.join(REPO_ROOT, "memory", "mistakes", "ledger.jsonl")
        self.assertTrue(os.path.exists(ledger_path), "Ledger file must exist")
        
        with open(ledger_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            
        self.assertGreater(len(lines), 0, "Mistake ledger should not be empty")
        
        for line in lines:
            entry = json.loads(line)
            mistake_id = entry.get("id")
            status = entry.get("status")
            
            if status == "RESOLVED":
                task = entry.get("task")
                inp = entry.get("input")
                expected = entry.get("expected")
                
                if task == "Number to Word Conversion":
                    actual = number_to_bangla_words(int(inp))
                    self.assertEqual(
                        actual, expected,
                        f"Regression failure for {mistake_id}: input={inp}, expected='{expected}', got='{actual}'"
                    )
                elif task == "Orthography Regex Matching":
                    from tools.bn_normalize import normalize_orthography
                    actual = normalize_orthography(inp)
                    self.assertEqual(actual, expected)
                elif task == "Nukta Canonicalization in String Literals":
                    from tools.bn_normalize import canonicalize_unicode
                    decomposed_sample = "\u0986\u09a1\u09bc\u09be\u0987" # আ + ড + ় + া + ই
                    actual = canonicalize_unicode(decomposed_sample)
                    expected_canonical = "\u0986\u09dc\u09be\u0987" # আ + ড় + া + ই
                    self.assertEqual(actual, expected_canonical)
                elif task == "Honorific Concordance Detection":
                    from tools.bn_lint import lint_text
                    issues = lint_text(inp)
                    rule_ids = [i.rule_id for i in issues]
                    self.assertIn(expected, rule_ids)
                elif task == "Honorific Concordance Repair":
                    from tools.bn_lint import lint_text
                    issues = lint_text(inp)
                    self.assertGreater(len(issues), 0)
                    suggestion = issues[0].suggestion
                    self.assertIn("তুমি সিদ্ধান্ত নাও", suggestion)
                    self.assertIn("আপনি সিদ্ধান্ত নেন", suggestion)
                elif task == "Judicial Show-Cause Translation":
                    from tools.bn_lint import lint_text
                    issues = lint_text(entry.get("output"))
                    self.assertTrue(any(i.rule_id == "RULE-LINT-CALQUE" for i in issues))
                    calque = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"][0]
                    self.assertIn("জানতে চেয়ে রুল জারি করেছেন", calque.suggestion)
                elif task == "Sports Defeat Reporting Translation":
                    from tools.bn_lint import lint_text
                    from tools.bn_normalize import canonicalize_unicode
                    issues = lint_text(entry.get("output"))
                    self.assertTrue(any(i.rule_id == "RULE-LINT-CALQUE" for i in issues))
                    calque = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"][0]
                    self.assertIn(canonicalize_unicode("পরাজিত হয়েছে / হেরেছে"), calque.suggestion)

if __name__ == "__main__":
    unittest.main()
