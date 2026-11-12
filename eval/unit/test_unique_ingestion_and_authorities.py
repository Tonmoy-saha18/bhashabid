# eval/unit/test_unique_ingestion_and_authorities.py
# Verification of Guaranteed Unique Ingestion, Fingerprinting, and Authoritative Citations
import unittest
import os
import json
import tempfile
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

from tools.autonomous_scraper import AutonomousScraper, DEFAULT_FEEDS
from tools.card_synthesizer import CardSynthesizer, AUTHORITATIVE_DOMAIN_STANDARDS
from tools.corpus_harvester import CorpusHarvester, HarvestedSentence


class TestUniqueIngestionAndAuthorities(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tmp_path = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_scraper_fingerprint_deduplication(self):
        """Ensure identical or punctuation-variant sentences are caught and rejected as duplicates."""
        fp_file = os.path.join(self.tmp_path, "test_fp.json")
        scraper = AutonomousScraper(inbox_dir=self.tmp_path, fingerprints_path=fp_file)

        text_a = "বাংলাদেশ সুপ্রিম কোর্ট সংবিধানের ১০২ অনুচ্ছেদ অনুসারে রিট এখতিয়ার প্রয়োগ করেন।"
        text_a_variant = "  বাংলাদেশ সুপ্রিম কোর্ট সংবিধানের ১০২ অনুচ্ছেদ অনুসারে রিট এখতিয়ার প্রয়োগ করেন!  "
        text_b = "বাংলাদেশ ব্যাংক বৈদেশিক মুদ্রার রিজার্ভ সুরক্ষায় নতুন মুদ্রানীতি ঘোষণা করেছে।"

        # text_a should not be seen initially
        self.assertFalse(scraper.is_seen(text_a))
        scraper.mark_seen(text_a)
        self.assertTrue(scraper.is_seen(text_a))

        # Variant with different whitespace and punctuation should hash to the exact same invariant fingerprint
        self.assertTrue(scraper.is_seen(text_a_variant), "Punctuation/whitespace variation must be recognized as duplicate")

        # Distinct sentence text_b should not be marked seen yet
        self.assertFalse(scraper.is_seen(text_b))
        scraper.mark_seen(text_b)
        self.assertTrue(scraper.is_seen(text_b))

        # Save fingerprints and reload in new scraper instance to test persistence
        scraper.save_fingerprints()
        self.assertTrue(os.path.exists(fp_file))

        reloaded_scraper = AutonomousScraper(inbox_dir=self.tmp_path, fingerprints_path=fp_file)
        self.assertTrue(reloaded_scraper.is_seen(text_a))
        self.assertTrue(reloaded_scraper.is_seen(text_a_variant))
        self.assertTrue(reloaded_scraper.is_seen(text_b))

    def test_11_sectors_covered_in_scraper_feeds(self):
        """Verify all 11 professional sectors have dedicated authoritative feeds."""
        covered_sectors = {feed["sector"] for feed in DEFAULT_FEEDS}
        for sector_id in range(1, 12):
            self.assertIn(sector_id, covered_sectors, f"Sector {sector_id} missing from autonomous scraper feeds")

        for feed in DEFAULT_FEEDS:
            self.assertTrue(feed.get("name"), "Feed must have a descriptive name")
            self.assertTrue(feed.get("url"), "Feed must have a valid URL")
            self.assertTrue(feed.get("domain"), "Feed must have an assigned domain")
            self.assertIn("sector", feed, "Feed must specify sector index")

    def test_11_sectors_have_authoritative_standards(self):
        """Verify all 11 professional sectors map to verified statutory authorities."""
        required_domains = [
            "Constitutional Law & Writs",
            "Macroeconomics & Banking",
            "Healthcare & Epidemiology",
            "Administrative Governance & Memos",
            "Creative Fiction & Dialogue",
            "Classical Poetry & Prosody",
            "Academic Research & Methodology",
            "Land Registry & Deeds",
            "Agronomy & Disaster Management",
            "ICT & Software Engineering",
            "Education & NCTB Pedagogy"
        ]
        for dom in required_domains:
            self.assertIn(dom, AUTHORITATIVE_DOMAIN_STANDARDS, f"Domain {dom} missing authoritative citations")
            standards = AUTHORITATIVE_DOMAIN_STANDARDS[dom]
            self.assertGreaterEqual(len(standards), 2, f"Domain {dom} must have at least 2 verified sources")

    def test_synthesizer_attaches_verified_authoritative_sources(self):
        """Verify candidate knowledge cards carry statutory standards and provenance."""
        synth = CardSynthesizer(drafts_dir=self.tmp_path)
        test_anomalies = [
            {
                "rule_id": "TEST-LEGAL-001",
                "matched": "রিট আবেদনপত্র দাখিল",
                "raw_text": "আইনজীবী হাইকোর্টে রিট আবেদনপত্র দাখিল করিলেন।",
                "suggestion": "রিট আবেদনপত্র দাখিল করলেন",
                "domain": "Constitutional Law & Writs",
                "source": "Bangla Wikipedia Bangladesh Case Law & Jurisprudence"
            }
        ]

        created = synth.cluster_and_synthesize_anomalies(test_anomalies)
        self.assertEqual(len(created), 1)
        draft_card_path = created[0]

        import yaml
        with open(draft_card_path, "r", encoding="utf-8") as f:
            card = yaml.safe_load(f)

        sources = card.get("sources", [])
        self.assertTrue(any("Constitution of the People's Republic of Bangladesh" in s for s in sources))
        self.assertTrue(any("Corpus Harvest Provenance" in s for s in sources))
        self.assertTrue(any("Principle P2 Human Provenance Audit Gate" in s for s in sources))

    def test_corpus_harvester_resets_harvested_buffer(self):
        """Verify harvest_all_sources clears old harvested data before each cycle."""
        harvester = CorpusHarvester()
        # Seed dummy item
        dummy = HarvestedSentence(
            id="SENT-DUMMY",
            source="Old Batch",
            domain="general",
            raw_text="পুরনো ডেটা",
            normalized_text="পুরনো ডেটা",
            is_clean=True,
            flaws_count=0,
            flaws=[],
            category="clean"
        )
        harvester.harvested = [dummy]
        self.assertEqual(len(harvester.harvested), 1)

        # Call harvest_all_sources
        harvester.harvest_all_sources(archive_inbox=False)
        # Check that the dummy item was wiped and only actual corpora were harvested
        for item in harvester.harvested:
            self.assertNotEqual(item.raw_text, "পুরনো ডেটা", "Old harvested items must not persist across harvest calls")


if __name__ == "__main__":
    unittest.main()
