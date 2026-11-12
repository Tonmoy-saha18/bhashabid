# eval/unit/test_self_improving_pipeline.py
# Unit Tests for Closed-Loop Knowledge Card Synthesizer & Skill Distiller
import unittest
import os
import tempfile
import yaml
from pathlib import Path

from tools.card_synthesizer import CardSynthesizer
from tools.skill_distiller import SkillDistiller, MAX_CORE_TOKEN_BUDGET

class TestSelfImprovingPipeline(unittest.TestCase):

    def test_card_synthesizer_draft_creation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            synth = CardSynthesizer(drafts_dir=tmpdir)
            out_path = synth.synthesize_draft_from_anomaly(
                title="Test Proverb Rule",
                domain="translation",
                register="formal",
                rule_summary="Map English proverb to Bengali idiom.",
                bad_examples=["ঘেউ ঘেউ করা কুকুর"],
                good_examples=["যত গর্জে তত বর্ষে না"],
                common_llm_error="Literal machine calque.",
                sources=["Test Source"],
                draft_id="CRD-DFT-999"
            )

            self.assertTrue(os.path.exists(out_path))
            with open(out_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            self.assertEqual(data["id"], "CRD-DFT-999")
            self.assertEqual(data["confidence"], "candidate")
            self.assertEqual(data["review"]["status"], "PENDING_HUMAN_REVIEW")
            self.assertIn("যত গর্জে তত বর্ষে না", data["good_examples"])

    def test_skill_distiller_token_budget_verification(self):
        distiller = SkillDistiller()
        self.assertGreater(len(distiller.approved_cards), 0)

        # Test valid text under budget
        valid_text = "This is a short rule prompt with few tokens."
        is_valid, tok = distiller.verify_token_budget(valid_text, max_tokens=100)
        self.assertTrue(is_valid)
        self.assertLess(tok, 100)

        # Test oversize text
        huge_text = "শব্দ " * 500
        is_valid_huge, tok_huge = distiller.verify_token_budget(huge_text, max_tokens=MAX_CORE_TOKEN_BUDGET)
        self.assertFalse(is_valid_huge)
        self.assertGreater(tok_huge, MAX_CORE_TOKEN_BUDGET)

    def test_skill_distiller_live_distillation(self):
        distiller = SkillDistiller()
        stats = distiller.distill_all(auto_install=False)
        self.assertGreaterEqual(stats["approved_cards_loaded"], 28)
        self.assertTrue(stats["token_budget_compliant"])
        self.assertLessEqual(stats["core_rules_token_count"], MAX_CORE_TOKEN_BUDGET)

if __name__ == "__main__":
    unittest.main()
