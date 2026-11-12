# eval/unit/test_learning_ledger.py
import unittest
import os
import sys
import tempfile
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.learning_benchmark_ledger import LearningBenchmarkLedger, DEFAULT_SECTORS

class TestLearningBenchmarkLedger(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.ledger_file = os.path.join(self.temp_dir.name, "test_ledger.json")
        self.report_file = os.path.join(self.temp_dir.name, "test_report.md")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_ledger_initialization_and_serialization(self):
        ledger = LearningBenchmarkLedger(ledger_path=self.ledger_file)
        self.assertEqual(ledger.data["cumulative_practice_sessions"], 0)
        self.assertEqual(len(ledger.data["sector_sentence_distribution"]), 11)
        ledger.save()
        self.assertTrue(os.path.exists(self.ledger_file))

        # Re-load
        reloaded = LearningBenchmarkLedger(ledger_path=self.ledger_file)
        self.assertEqual(reloaded.data["version"], "1.0.0")
        self.assertEqual(reloaded.data["cumulative_practice_sessions"], 0)

    def test_record_practice_session(self):
        ledger = LearningBenchmarkLedger(ledger_path=self.ledger_file)
        sector_counts = {
            "Constitutional Law & Writs": 15,
            "Macroeconomics & Banking": 20,
            "Healthcare": 10,  # Substring should match Healthcare & Epidemiology
            "Land Registry": 5
        }
        ledger.record_practice_session(
            rounds=2,
            total_checks=50,
            sentences_practiced=50,
            flaws_trapped=2,
            sector_counts=sector_counts
        )

        self.assertEqual(ledger.data["cumulative_practice_sessions"], 1)
        self.assertEqual(ledger.data["cumulative_rounds_completed"], 2)
        self.assertEqual(ledger.data["cumulative_checks_evaluated"], 50)
        self.assertEqual(ledger.data["cumulative_sentences_practiced"], 50)
        self.assertEqual(ledger.data["cumulative_flaws_trapped"], 2)
        self.assertEqual(ledger.data["sector_sentence_distribution"]["Constitutional Law & Writs"], 15)
        self.assertEqual(ledger.data["sector_sentence_distribution"]["Macroeconomics & Banking"], 20)
        self.assertEqual(ledger.data["sector_sentence_distribution"]["Healthcare & Epidemiology"], 10)
        self.assertEqual(ledger.data["sector_sentence_distribution"]["Land Registry & Deeds"], 5)

    def test_record_confidence_milestone(self):
        ledger = LearningBenchmarkLedger(ledger_path=self.ledger_file)
        ledger.record_confidence_milestone(
            round_idx=3,
            saturation_score=0.98,
            clean_precision=0.98,
            batch_size=30,
            new_batch_ingested="eval/corpora/inbox/feed_123.jsonl"
        )

        self.assertEqual(len(ledger.data["confidence_milestones"]), 1)
        self.assertEqual(ledger.data["cumulative_fresh_batches_ingested"], 1)
        m = ledger.data["confidence_milestones"][0]
        self.assertEqual(m["round"], 3)
        self.assertEqual(m["saturation_score"], 0.98)
        self.assertEqual(m["new_batch_ingested"], "feed_123.jsonl")

    def test_export_research_report(self):
        ledger = LearningBenchmarkLedger(ledger_path=self.ledger_file)
        ledger.record_practice_session(
            rounds=5,
            total_checks=100,
            sentences_practiced=100,
            flaws_trapped=3,
            sector_counts={"ICT & Software Engineering": 25}
        )
        ledger.record_confidence_milestone(
            round_idx=5,
            saturation_score=0.97,
            clean_precision=0.97,
            batch_size=25,
            new_batch_ingested="feed_fresh.jsonl"
        )
        out = ledger.export_research_report(report_path=self.report_file)
        self.assertTrue(os.path.exists(out))
        with open(out, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("# Bhashabid Research Learning Ledger & Multi-Sector Benchmark", content)
        self.assertIn("Cumulative Practice Sessions", content)
        for sec in DEFAULT_SECTORS:
            self.assertIn(sec, content)
        self.assertIn("ICT & Software Engineering", content)
        self.assertIn("97.0%", content)
        self.assertIn("feed_fresh.jsonl", content)

if __name__ == "__main__":
    unittest.main()
