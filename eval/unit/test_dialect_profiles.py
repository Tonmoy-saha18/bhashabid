# Unit Tests for Regional Dialect Profiles
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.profiles import get_profile, BD_STANDARD, WB_STANDARD
from tools.bn_numbers import number_to_bangla_words, StyleProfile

class TestDialectProfiles(unittest.TestCase):

    def test_profile_resolution(self):
        bd = get_profile("bd_standard")
        self.assertEqual(bd.name, "bd_standard")
        self.assertEqual(bd.hundred_style, "শত")

        wb = get_profile("wb_standard")
        self.assertEqual(wb.name, "wb_standard")
        self.assertEqual(wb.hundred_style, "শো")
        self.assertEqual(wb.twenty_style, "কুড়ি")

    def test_number_formatting_with_profiles(self):
        # BD standard: পাঁচ শত, বিশ
        p_bd = StyleProfile(hundred_style=BD_STANDARD.hundred_style, twenty_style=BD_STANDARD.twenty_style)
        self.assertEqual(number_to_bangla_words(500, p_bd), "পাঁচ শত")
        self.assertEqual(number_to_bangla_words(20, p_bd), "বিশ")

        # WB standard: পাঁচ শো, কুড়ি
        p_wb = StyleProfile(hundred_style=WB_STANDARD.hundred_style, twenty_style=WB_STANDARD.twenty_style)
        self.assertEqual(number_to_bangla_words(500, p_wb), "পাঁচ শো")
        self.assertEqual(number_to_bangla_words(20, p_wb), "কুড়ি")

if __name__ == "__main__":
    unittest.main()
