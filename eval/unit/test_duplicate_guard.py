# eval/unit/test_duplicate_guard.py
# Automated Regression Test Suite for Duplicate Guard and Consistency
import unittest
import os
import glob
import yaml
from pathlib import Path
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

from tools.card_synthesizer import CardSynthesizer

class TestDuplicateGuard(unittest.TestCase):

    def test_no_duplicate_titles_across_all_cards(self):
        cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
        drafts_dir = os.path.join(cards_dir, "drafts")

        all_cards = []
        for p in glob.glob(os.path.join(cards_dir, "*.yaml")):
            with open(p, encoding="utf-8") as f:
                d = yaml.safe_load(f)
                all_cards.append((p, d))

        for p in glob.glob(os.path.join(drafts_dir, "*.yaml")):
            with open(p, encoding="utf-8") as f:
                d = yaml.safe_load(f)
                all_cards.append((p, d))

        titles = defaultdict(list)
        for path, c in all_cards:
            t = (c.get("title") or "").strip().lower()
            titles[t].append(path)

        dup_titles = {t: paths for t, paths in titles.items() if len(paths) > 1}
        self.assertEqual(len(dup_titles), 0, f"Found duplicate card titles: {dup_titles}")

    def test_no_duplicate_examples_within_any_card(self):
        cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
        drafts_dir = os.path.join(cards_dir, "drafts")

        for fpath in glob.glob(os.path.join(cards_dir, "*.yaml")) + glob.glob(os.path.join(drafts_dir, "*.yaml")):
            with open(fpath, encoding="utf-8") as f:
                card = yaml.safe_load(f)
            bads = card.get("bad_examples") or []
            goods = card.get("good_examples") or []
            self.assertEqual(len(bads), len(set(bads)), f"Duplicate bad_examples in {fpath}: {bads}")
            self.assertEqual(len(goods), len(set(goods)), f"Duplicate good_examples in {fpath}: {goods}")

    def test_duplicate_guard_prevents_redundant_synthesis(self):
        synth = CardSynthesizer()
        # Simulated novel anomaly pattern not in production
        pattern = "পরীক্ষামূলক অমিল প্যাটার্ন"
        test_anomalies = [
            {
                "rule_id": "TEST-NOVEL-PATTERN-001",
                "matched": pattern,
                "raw_text": f"এটি একটি {pattern}",
                "suggestion": "সংশোধিত রূপ",
                "domain": "translation"
            }
        ]
        # First synthesis creates a draft
        created_1 = synth.cluster_and_synthesize_anomalies(test_anomalies)
        self.assertEqual(len(created_1), 1)
        draft_path = created_1[0]
        self.assertTrue(os.path.exists(draft_path))

        try:
            # Second synthesis with the same pattern must NOT create a new file
            created_2 = synth.cluster_and_synthesize_anomalies(test_anomalies)
            self.assertEqual(len(created_2), 1)
            self.assertEqual(created_2[0], draft_path, "Duplicate guard should return existing draft, not create another")
        finally:
            # Clean up test draft
            if os.path.exists(draft_path):
                os.remove(draft_path)

if __name__ == "__main__":
    unittest.main()
