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

    def test_installer_and_uninstaller_lifecycle(self):
        import tempfile
        import json
        from pathlib import Path
        from tools.skill_installer import install_skill, uninstall_skill, install_mcp, uninstall_mcp

        with tempfile.TemporaryDirectory() as tmpdir:
            # 1. Install to cursor in tempdir
            msg_in = install_skill(target="cursor", workspace_dir=tmpdir, with_mcp=True)
            self.assertIn("successfully installed", msg_in)

            cur_rules = Path(tmpdir) / ".cursorrules"
            cur_mdc = Path(tmpdir) / ".cursor" / "rules" / "bangla-expert.mdc"
            cur_refs = Path(tmpdir) / ".cursor" / "bangla-references"
            mcp_file = Path(tmpdir) / ".cursor" / "mcp.json"

            self.assertTrue(cur_rules.exists())
            self.assertTrue(cur_mdc.exists())
            self.assertTrue(cur_refs.exists())
            self.assertTrue(mcp_file.exists())

            with open(mcp_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIn("bhashabid", data.get("mcpServers", {}))

            # 2. Uninstall from cursor
            msg_un = uninstall_skill(target="cursor", workspace_dir=tmpdir, with_mcp=True)
            self.assertIn("successfully removed", msg_un)

            self.assertFalse(cur_rules.exists())
            self.assertFalse(cur_mdc.exists())
            self.assertFalse(cur_refs.exists())

            # Verify MCP server entry was cleanly removed
            with open(mcp_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertNotIn("bhashabid", data.get("mcpServers", {}))

if __name__ == "__main__":
    unittest.main()
