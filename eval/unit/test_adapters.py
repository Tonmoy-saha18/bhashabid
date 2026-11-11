# Adapter Integrity Tests
import unittest
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestAdapters(unittest.TestCase):

    def test_cursorrules_exists(self):
        p = os.path.join(REPO_ROOT, "adapters", "cursor", ".cursorrules")
        self.assertTrue(os.path.exists(p))
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Bangla Academy Orthography", content)

    def test_claude_prompt_token_budget(self):
        p = os.path.join(REPO_ROOT, "adapters", "claude", "claude_system_prompt.txt")
        self.assertTrue(os.path.exists(p))
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        tokens = int(len(content.split()) * 1.3)
        self.assertLess(tokens, 500, f"Claude prompt exceeds token budget: approx {tokens}")

    def test_adrs_exist(self):
        adr1 = os.path.join(REPO_ROOT, "docs", "adr", "001-progressive-skill-disclosure.md")
        adr2 = os.path.join(REPO_ROOT, "docs", "adr", "002-deterministic-bengali-grapheme-regex.md")
        self.assertTrue(os.path.exists(adr1))
        self.assertTrue(os.path.exists(adr2))

if __name__ == "__main__":
    unittest.main()
