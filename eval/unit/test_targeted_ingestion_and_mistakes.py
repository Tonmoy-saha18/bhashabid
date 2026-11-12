# eval/unit/test_targeted_ingestion_and_mistakes.py
# Unit Tests for Sector-Targeted Ingestion and Learning from Mistakes
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.mistake_synthesizer import MistakeLearningSynthesizer, SECTOR_MISTAKE_PATTERNS
from tools.autonomous_scraper import AutonomousScraper

class TestTargetedIngestionAndMistakes(unittest.TestCase):

    def setUp(self):
        self.synth = MistakeLearningSynthesizer()

    def test_mistake_synthesizer_all_sectors(self):
        for sector in SECTOR_MISTAKE_PATTERNS:
            items = self.synth.synthesize_sector_batch(sector, count=2)
            self.assertEqual(len(items), 2, f"Failed to synthesize for sector: {sector}")
            for itm in items:
                self.assertEqual(itm["domain"], sector)
                self.assertIn("Learning from Mistakes", itm["source"])
                self.assertEqual(itm["label"], "MISTAKE_LEARNING_CANDIDATE")
                self.assertGreater(len(itm["text"]), 10)
                self.assertIn("justified by learning from mistakes", itm["notes"].lower())

    def test_fingerprint_deduplication(self):
        fps = set()
        items1 = self.synth.synthesize_sector_batch("Macroeconomics & Banking", count=3, exclude_fingerprints=fps)
        self.assertEqual(len(items1), 3)
        self.assertEqual(len(fps), 3)

        # Generating again with fps populated should not yield duplicates in fps
        items2 = self.synth.synthesize_sector_batch("Macroeconomics & Banking", count=2, exclude_fingerprints=fps)
        self.assertEqual(len(items2), 2)
        self.assertEqual(len(fps), 5)

    def test_scraper_targeted_sector_filtering(self):
        scraper = AutonomousScraper()
        target_sectors = ["Land Registry & Deeds", "Agronomy & Disaster Management"]
        items = scraper.scrape_targeted_sector_data(target_sectors, max_items_per_sector=2)
        
        self.assertGreater(len(items), 0)
        # Ensure only the targeted sectors are returned
        returned_domains = {itm["domain"] for itm in items}
        for d in returned_domains:
            self.assertIn(d, target_sectors, f"Unexpected non-targeted sector returned: {d}")

if __name__ == "__main__":
    unittest.main()
