# Unit Tests for Bhashabid MCP Server
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.mcp_server import BhashabidMCPServer

class TestMCPServer(unittest.TestCase):

    def setUp(self):
        self.server = BhashabidMCPServer()

    def test_list_tools(self):
        tools = self.server.list_tools()
        names = [t["name"] for t in tools]
        self.assertIn("convert_number", names)
        self.assertIn("normalize_text", names)
        self.assertIn("lint_text", names)

    def test_call_convert_number(self):
        res = self.server.call_tool("convert_number", {"number": 99, "format": "words"})
        self.assertEqual(res["result"], "নিরানব্বই")

        res_grouped = self.server.call_tool("convert_number", {"number": 1234567, "format": "grouped"})
        self.assertEqual(res_grouped["result"], "১২,৩৪,৫৬৭")

        # Test floating-point and string decimal handling
        res_dec = self.server.call_tool("convert_number", {"number": "89079490.7890", "format": "words"})
        self.assertEqual(
            res_dec["result"],
            "আট কোটি নব্বই লাখ ঊনআশি হাজার চার শত নব্বই দশমিক সাত আট নয় শূন্য"
        )

        res_dec_float = self.server.call_tool("convert_number", {"number": 3.14, "format": "words"})
        self.assertEqual(res_dec_float["result"], "তিন দশমিক এক চার")

        res_dec_grouped = self.server.call_tool("convert_number", {"number": "89079490.7890", "format": "grouped"})
        self.assertEqual(res_dec_grouped["result"], "৮,৯০,৭৯,৪৯০.৭৮৯০")

        res_curr = self.server.call_tool("convert_number", {"number": "50.25", "format": "currency"})
        self.assertEqual(res_curr["result"], "পঞ্চাশ টাকা পঁচিশ পয়সা")

        res_frac = self.server.call_tool("convert_number", {"number": 2.5, "format": "fraction"})
        self.assertEqual(res_frac["result"], "আড়াই")

        res_ord = self.server.call_tool("convert_number", {"number": 35, "format": "ordinal"})
        self.assertEqual(res_ord["result"], "৩৫-তম")

        res_date_ord = self.server.call_tool("convert_number", {"number": 26, "format": "date_ordinal"})
        self.assertEqual(res_date_ord["result"], "২৬শে")

    def test_call_normalize_text(self):
        res = self.server.call_tool("normalize_text", {"text": "তিনি রেলষ্টেশনে গেলেন."})
        self.assertEqual(res["result"], "তিনি রেলস্টেশনে গেলেন।")

    def test_call_lint_text(self):
        res = self.server.call_tool("lint_text", {"text": "আপনি কি কাজটি করো?"})
        self.assertGreater(res["issue_count"], 0)
        self.assertEqual(res["issues"][0]["rule_id"], "RULE-LINT-HONORIFIC-APNI")

if __name__ == "__main__":
    unittest.main()
