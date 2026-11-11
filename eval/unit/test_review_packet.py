# Unit Tests for Human Review Packet & Card Confidence
import unittest
import sys
import os
import glob
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.review_packet_generator import generate_review_packet

class TestReviewPacket(unittest.TestCase):

    def test_packet_generation(self):
        packet = generate_review_packet()
        self.assertIn("Expert Linguistic Review Packet", packet)
        self.assertIn("CRD-NUM-001", packet)
        self.assertIn("CRD-ORT-001", packet)
        self.assertIn("CRD-ORT-003", packet)
        self.assertIn("Human Reviewer Decision Box", packet)

    def test_cards_p2_provenance_rule(self):
        cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
        for fpath in glob.glob(os.path.join(cards_dir, "*.yaml")):
            with open(fpath, "r", encoding="utf-8") as f:
                card = yaml.safe_load(f)
            # Principle P2: Agents may NEVER self-promote to 'reviewed'
            self.assertNotEqual(
                card.get("confidence"), "reviewed",
                f"Principle P2 violation: Card {card.get('id')} cannot be 'reviewed' without human native sign-off!"
            )
            self.assertIn(card.get("confidence"), ["llm-hypothesis", "data-supported"])

if __name__ == "__main__":
    unittest.main()
