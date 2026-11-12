# Exhaustive Unit Test Suite for bn_numbers
import unittest
import sys
import os

# Add repo root to python path
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_numbers import (
    to_bangla_digits,
    to_ascii_digits,
    format_lakh_crore,
    number_to_bangla_words,
    StyleProfile,
    decimal_to_bangla_words,
    fraction_to_bangla_words,
    format_currency_words,
    format_date_bangla,
    to_classical_ordinal,
    to_date_ordinal
)

class TestBnNumbers(unittest.TestCase):

    def test_ascii_to_bangla_digits(self):
        self.assertEqual(to_bangla_digits("0123456789"), "০১২৩৪৫৬৭৮৯")
        self.assertEqual(to_bangla_digits(1971), "১৯৭১")

    def test_bangla_to_ascii_digits(self):
        self.assertEqual(to_ascii_digits("০১২৩৪৫৬৭৮৯"), "0123456789")
        self.assertEqual(to_ascii_digits("১৯৭১"), "1971")

    def test_lakh_crore_grouping(self):
        self.assertEqual(format_lakh_crore(100), "১০০")
        self.assertEqual(format_lakh_crore(1000), "১,০০০")
        self.assertEqual(format_lakh_crore(1234567), "১২,৩৪,৫৬৭")
        self.assertEqual(format_lakh_crore(12345678), "১,২৩,৪৫,৬৭৮")
        self.assertEqual(format_lakh_crore("1234567", to_bangla=False), "12,34,567")
        self.assertEqual(format_lakh_crore("89079490.7890"), "৮,৯০,৭৯,৪৯০.৭৮৯০")

    def test_zero_to_ninety_nine(self):
        # Verify 0, 1, 99 and sample checks
        self.assertEqual(number_to_bangla_words(0), "শূন্য")
        self.assertEqual(number_to_bangla_words(1), "এক")
        self.assertEqual(number_to_bangla_words(2), "দুই")
        self.assertEqual(number_to_bangla_words(10), "দশ")
        self.assertEqual(number_to_bangla_words(11), "এগারো")
        self.assertEqual(number_to_bangla_words(20), "বিশ")
        self.assertEqual(number_to_bangla_words(25), "পঁচিশ")
        self.assertEqual(number_to_bangla_words(50), "পঞ্চাশ")
        self.assertEqual(number_to_bangla_words(75), "পঁচাত্তর")
        self.assertEqual(number_to_bangla_words(83), "তিরাশি")
        self.assertEqual(number_to_bangla_words(99), "নিরানব্বই")

    def test_exhaustive_0_to_99(self):
        for i in range(100):
            word = number_to_bangla_words(i)
            self.assertIsInstance(word, str)
            self.assertGreater(len(word), 0, f"Number {i} must produce a valid Bengali word")

    def test_large_numbers_words(self):
        self.assertEqual(number_to_bangla_words(100), "এক শত")
        self.assertEqual(number_to_bangla_words(105), "এক শত পাঁচ")
        self.assertEqual(number_to_bangla_words(1234), "এক হাজার দুই শত চৌত্রিশ")
        self.assertEqual(number_to_bangla_words(100000), "এক লাখ")
        self.assertEqual(number_to_bangla_words(10000000), "এক কোটি")
        self.assertEqual(number_to_bangla_words(1000000000), "এক শত কোটি")

    def test_style_profiles(self):
        sho_profile = StyleProfile(hundred_style="শো", lakh_style="লক্ষ")
        self.assertEqual(number_to_bangla_words(500, sho_profile), "পাঁচ শো")
        self.assertEqual(number_to_bangla_words(200000, sho_profile), "দুই লক্ষ")
        
        kuri_profile = StyleProfile(twenty_style="কুড়ি")
        self.assertEqual(number_to_bangla_words(20, kuri_profile), "কুড়ি")

    def test_negative_numbers(self):
        self.assertEqual(number_to_bangla_words(-5), "মাইনাস পাঁচ")
        rin_profile = StyleProfile(negative_prefix="ঋণাত্মক")
        self.assertEqual(number_to_bangla_words(-5, rin_profile), "ঋণাত্মক পাঁচ")

    def test_decimals_digit_by_digit(self):
        self.assertEqual(decimal_to_bangla_words("3.14"), "তিন দশমিক এক চার")
        self.assertEqual(decimal_to_bangla_words(0.05), "শূন্য দশমিক শূন্য পাঁচ")
        self.assertEqual(decimal_to_bangla_words("-0.75"), "মাইনাস শূন্য দশমিক সাত পাঁচ")
        self.assertEqual(decimal_to_bangla_words("-5.25"), "মাইনাস পাঁচ দশমিক দুই পাঁচ")
        self.assertEqual(
            decimal_to_bangla_words("89079490.7890"),
            "আট কোটি নব্বই লাখ ঊনআশি হাজার চার শত নব্বই দশমিক সাত আট নয় শূন্য"
        )

    def test_fractions(self):
        self.assertEqual(fraction_to_bangla_words(0.25), "এক-চতুর্থাংশ")
        self.assertEqual(fraction_to_bangla_words(0.5), "অর্ধেক")
        self.assertEqual(fraction_to_bangla_words(-0.5), "মাইনাস অর্ধেক")
        self.assertEqual(fraction_to_bangla_words(1.5), "দেড়")
        self.assertEqual(fraction_to_bangla_words(-1.5), "মাইনাস দেড়")
        self.assertEqual(fraction_to_bangla_words(2.5), "আড়াই")
        self.assertEqual(fraction_to_bangla_words(-2.5), "মাইনাস আড়াই")
        self.assertEqual(fraction_to_bangla_words(1.25), "সোয়া এক")
        self.assertEqual(fraction_to_bangla_words(3.5), "সাড়ে তিন")
        self.assertEqual(fraction_to_bangla_words(4.75), "পৌনে পাঁচ")
        self.assertEqual(fraction_to_bangla_words(101.5), "সাড়ে এক শত এক")
        self.assertEqual(fraction_to_bangla_words(100.75), "পৌনে এক শত এক")

    def test_currency(self):
        self.assertEqual(format_currency_words(50.25), "পঞ্চাশ টাকা পঁচিশ পয়সা")
        self.assertEqual(format_currency_words(100), "এক শত টাকা")
        self.assertEqual(format_currency_words(0.50), "পঞ্চাশ পয়সা")
        self.assertEqual(format_currency_words(-50.25), "মাইনাস পঞ্চাশ টাকা পঁচিশ পয়সা")
        self.assertEqual(format_currency_words(-0.50), "মাইনাস পঞ্চাশ পয়সা")
        self.assertEqual(format_currency_words(0), "শূন্য টাকা")

    def test_classical_ordinals(self):
        self.assertEqual(to_classical_ordinal(1), "প্রথম")
        self.assertEqual(to_classical_ordinal(2), "দ্বিতীয়")
        self.assertEqual(to_classical_ordinal(3), "তৃতীয়")
        self.assertEqual(to_classical_ordinal(10), "দশম")
        self.assertEqual(to_classical_ordinal(35), "৩৫-তম")

    def test_date_ordinals(self):
        self.assertEqual(to_date_ordinal(1), "১লা")
        self.assertEqual(to_date_ordinal(2), "২রা")
        self.assertEqual(to_date_ordinal(4), "৪ঠা")
        self.assertEqual(to_date_ordinal(5), "৫ই")
        self.assertEqual(to_date_ordinal(21), "২১শে")
        self.assertEqual(to_date_ordinal(31), "৩১শে")
        self.assertEqual(to_date_ordinal(32), "৩২ই")

    def test_date_formatting(self):
        self.assertEqual(format_date_bangla(2026, 3, 26), "২৬শে মার্চ, ২০২৬")
        self.assertEqual(format_date_bangla(1971, 12, 16), "১৬ই ডিসেম্বর, ১৯৭১")

if __name__ == "__main__":
    unittest.main()
