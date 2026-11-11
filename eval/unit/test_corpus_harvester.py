# eval/unit/test_corpus_harvester.py
# Unit tests for Corpus Harvester, Sentence Splitting & Multi-Domain Ingestion
import unittest
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.corpus_harvester import CorpusHarvester

class TestCorpusHarvester(unittest.TestCase):

    def setUp(self):
        self.harvester = CorpusHarvester()

    def test_sentence_splitting_with_dari_and_abbreviations(self):
        sample = "ড. ইউনূস প্রধান উপদেষ্টা হিসেবে দায়িত্ব নিলেন। তিনি সভায় বলিলেন, 'কাজ দ্রুত করুন।' পাইয়ের মান ৩.১৪।"
        sents = CorpusHarvester.split_sentences(sample)
        self.assertEqual(len(sents), 3)
        self.assertIn("ড. ইউনূস", sents[0])
        self.assertIn("৩.১৪", sents[2])

    def test_harvest_all_real_world_sources(self):
        stats = self.harvester.harvest_all_sources()
        self.assertGreaterEqual(stats["sources_scanned"], 3)
        self.assertGreaterEqual(stats["total_sentences"], 15)
        self.assertGreater(stats["benchmark_clean"], 10)
        self.assertGreater(stats["canary_trapped"], 0)

    def test_parallel_newsroom_distinction(self):
        raw_calque = "মূল্যস্ফীতি খাদ্যমূল্য বৃদ্ধির দ্বারা চালিত হয়েছে।"
        gold_standard = "খাদ্যমূল্যের কারণে মূল্যস্ফীতি বৃদ্ধি পেয়েছে।"
        
        raw_res = self.harvester.audit_sentence(raw_calque, source="TBS (Raw LLM)")
        gold_res = self.harvester.audit_sentence(gold_standard, source="TBS (Human Gold)")
        
        self.assertEqual(raw_res.category, "CANARY_TRAPPED")
        self.assertEqual(gold_res.category, "BENCHMARK_CLEAN")

    def test_export_harvest_report(self):
        self.harvester.harvest_all_sources()
        out = self.harvester.export_summary_report()
        self.assertTrue(os.path.exists(out))
        self.assertGreater(os.path.getsize(out), 100)

if __name__ == "__main__":
    unittest.main()
