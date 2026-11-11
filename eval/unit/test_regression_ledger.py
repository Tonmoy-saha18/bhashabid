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

if __name__ == "__main__":
    unittest.main()
