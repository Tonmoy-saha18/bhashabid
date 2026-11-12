# eval/unit/test_repair_engine.py
# Comprehensive Unit Tests for Deterministic Bengali Linguistic Repair Engine
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.repair import repair_text
from tools.bn_lint import lint_text
from tools.mcp_server.server import BhashabidMCPServer

class TestRepairEngine(unittest.TestCase):

    def test_calque_naturalization(self):
        cases = [
            ("সৌরবিদ্যুৎ দ্বারা চালিত পাম্প", "সৌরবিদ্যুৎ পরিচালিত পাম্প"),
            ("আদালত জিজ্ঞেস করে একটি রুল জারি করেছে", "আদালত রুল নিশি জারি করেছেন"),
            ("পেপারটি তর্ক করে যে উন্নয়ন আবশ্যক।", "গবেষণাপত্রে যুক্তি উপস্থাপন করা হয়েছে যে উন্নয়ন আবশ্যক।"),
            ("উপকূলে ১০ নম্বর বড় বিপদের সংকেত দেখানো হয়েছে।", "উপকূলে ১০ নম্বর মহাবিপদ সংকেত দেখানো হয়েছে।"),
            ("তিনি ঝোপের চারপাশে পেটাচ্ছেন।", "তিনি ঘুরিয়ে-পেঁচিয়ে কথা বলছেন।"),
            ("খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়।", "নাচতে না জানলে উঠান বাঁকা।")
        ]
        for raw, expected in cases:
            repaired, fixes = repair_text(raw)
            self.assertIn(expected, repaired)
            self.assertGreater(len(fixes), 0)
            # Ensure post-repair lint issues are 0
            issues = lint_text(repaired)
            self.assertEqual(len(issues), 0, f"Residual defects found in repaired text: {repaired}")

    def test_guru_chandali_harmonization(self):
        raw = "উদ্দীপকটি পড়িয়া নিচের প্রশ্নগুলোর উত্তর দাও।"
        repaired, fixes = repair_text(raw)
        self.assertIn("উদ্দীপকটি পড়ে নিচের প্রশ্নগুলোর উত্তর দাও", repaired)
        self.assertTrue(any(f["category"] == "GURU_CHANDALI_HARMONIZATION" for f in fixes))
        issues = lint_text(repaired)
        self.assertEqual(len(issues), 0)

    def test_honorific_concordance_repair(self):
        # Tini (honorific) + ordinary verb
        raw_tini = "তিনি কাল ঢাকা গেল।"
        repaired_tini, fixes_tini = repair_text(raw_tini)
        self.assertIn("তিনি কাল ঢাকা গেলেন", repaired_tini)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_tini))
        self.assertEqual(len(lint_text(repaired_tini)), 0)

        # Se (ordinary) + honorific verb
        raw_se = "সে বললেন যে কাল আসবে।"
        repaired_se, fixes_se = repair_text(raw_se)
        self.assertIn("সে বলল যে কাল আসবে", repaired_se)
        self.assertTrue(any(f["category"] == "HONORIFIC_CONCORDANCE" for f in fixes_se))
        self.assertEqual(len(lint_text(repaired_se)), 0)

    def test_idempotence_and_clean_text(self):
        clean_text = "তিনি প্রতিদিন সকালে বিদ্যালয়ে যান এবং পাঠদান করেন।"
        repaired, fixes = repair_text(clean_text)
        self.assertEqual(repaired, clean_text)
        self.assertEqual(len(fixes), 0)

    def test_mcp_server_repair_tool(self):
        server = BhashabidMCPServer()
        res = server.call_tool(
            "repair_text",
            {"text": "তিনি ঝোপের চারপাশে পেটাচ্ছেন."}
        )
        self.assertIn("repaired", res)
        self.assertIn("ঘুরিয়ে-পেঁচিয়ে কথা বলছেন।", res["repaired"])
        self.assertGreater(res["fixes_count"], 0)

if __name__ == "__main__":
    unittest.main()
