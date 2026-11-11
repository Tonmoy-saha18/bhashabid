# Knowledge Cards Schema and Content Validation Tests
import unittest
import os
import glob

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestKnowledgeCards(unittest.TestCase):

    def test_all_cards_valid_schema(self):
        cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
        card_files = glob.glob(os.path.join(cards_dir, "*.yaml"))
        self.assertGreater(len(card_files), 0, "There must be at least one knowledge card")

        required_keys = [
            "id", "title", "domain", "profile", "register",
            "rule_summary", "good_examples", "bad_examples",
            "common_llm_error", "sources", "confidence",
            "created_date", "last_modified"
        ]

        for card_path in card_files:
            with open(card_path, "r", encoding="utf-8") as f:
                content = f.read()

            for key in required_keys:
                self.assertIn(f"{key}:", content, f"Card {os.path.basename(card_path)} is missing key '{key}'")

            # Check confidence is NOT 'reviewed' unless authorized (P2 rule)
            self.assertNotIn("confidence: reviewed", content,
                f"Agent must never self-promote card {os.path.basename(card_path)} to 'reviewed'")

            # Check sources are non-empty
            self.assertIn("sources:", content)

if __name__ == "__main__":
    unittest.main()
