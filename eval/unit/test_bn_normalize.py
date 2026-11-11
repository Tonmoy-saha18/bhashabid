# Exhaustive Unit Tests for bn_normalize
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize import (
    normalize,
    canonicalize_unicode,
    is_nfc_normalized,
    normalize_punctuation,
    normalize_orthography
)

class TestBnNormalize(unittest.TestCase):

    def test_unicode_canonicalization(self):
        # Decomposed য় (য + ়) -> precomposed য় (U+09DF)
        decomposed_yo = "\u09AF\u09BC"
        canonical_yo = "\u09DF"
        self.assertEqual(canonicalize_unicode(decomposed_yo), canonical_yo)

        # Decomposed ড় (ড + ়) -> U+09DC
        decomposed_rra = "\u09A1\u09BC"
        self.assertEqual(canonicalize_unicode(decomposed_rra), "\u09DC")

        # Decomposed ঢ় (ঢ + ়) -> U+09DD
        decomposed_rhha = "\u09A2\u09BC"
        self.assertEqual(canonicalize_unicode(decomposed_rhha), "\u09DD")

        # Mixed sentence
        text = "বইটি ভালো হ" + decomposed_yo + "েছে"
        result = canonicalize_unicode(text)
        self.assertEqual(result, canonicalize_unicode("বইটি ভালো হয়েছে"))
        self.assertIn("\u09DF", result)
        self.assertNotIn(decomposed_yo, result)
        self.assertTrue(is_nfc_normalized(result))

    def test_dari_punctuation_and_decimals(self):
        # ASCII period at end of sentence to Dari
        self.assertEqual(normalize_punctuation("তিনি বাড়ি গেলেন."), "তিনি বাড়ি গেলেন।")
        
        # Decimal numbers must be preserved without replacing period with Dari
        self.assertEqual(normalize_punctuation("পাই এর মান ৩.১৪ প্রায়."), "পাই এর মান ৩.১৪ প্রায়।")
        self.assertEqual(normalize_punctuation("দাম 50.25 টাকা."), "দাম 50.25 টাকা।")

        # Collapse duplicate Daris
        self.assertEqual(normalize_punctuation("তিনি বললেন।।"), "তিনি বললেন।")

    def test_bangla_academy_loanword_s(self):
        # Foreign loanwords with S
        text = "তিনি রেলষ্টেশনে গিয়ে ডাকঘরে চিঠি পোষ্ট করলেন এবং মাষ্টারমশাইয়ের সাথে দেখা করলেন।"
        expected = "তিনি রেলস্টেশনে গিয়ে ডাকঘরে চিঠি পোস্ট করলেন এবং মাস্টারমশাইয়ের সাথে দেখা করলেন।"
        self.assertEqual(normalize_orthography(text), expected)

    def test_tatbhava_short_vowels(self):
        text = "গাছের ডালে পাখী গান গায় এবং বনে হাতী হাঁটে।"
        expected = "গাছের ডালে পাখি গান গায় এবং বনে হাতি হাঁটে।"
        self.assertEqual(normalize_orthography(text), expected)

    def test_whitespace_compaction(self):
        text = "তিনি    বাড়ি   গেলেন।\n\nনতুন   দিন   শুরু   হলো।"
        expected = canonicalize_unicode("তিনি বাড়ি গেলেন।\n\nনতুন দিন শুরু হলো।")
        self.assertEqual(normalize(text), expected)

if __name__ == "__main__":
    unittest.main()
