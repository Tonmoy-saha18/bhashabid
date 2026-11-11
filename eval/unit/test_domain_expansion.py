# eval/unit/test_domain_expansion.py
import unittest
from tools.bn_lint import lint_text

class TestDomainExpansion(unittest.TestCase):
    def test_land_deed_calque_trapped(self):
        text = "আমি আমার জমির বিক্রির কাগজ তৈরি করে জমি ক্রেতাকে হস্তান্তর করলাম।"
        issues = lint_text(text)
        self.assertTrue(any("সাফ-কবলা" in i.suggestion for i in issues))

    def test_storm_surge_calque_trapped(self):
        text = "ঘূর্ণিঝড়ের প্রভাবে উপকূলীয় অঞ্চলে ৫-৭ ফুট উচ্চতার ঝড় বৃদ্ধি দেখা যেতে পারে।"
        issues = lint_text(text)
        self.assertTrue(any("জলোচ্ছ্বাস" in i.suggestion for i in issues))

    def test_cyclone_alert_calque_trapped(self):
        text = "বন্দরগুলোকে ৮ নম্বর বড় বিপদের সংকেত দেখাতে বলা হয়েছে।"
        issues = lint_text(text)
        self.assertTrue(any("মহাবিপদ সংকেত" in i.suggestion for i in issues))

    def test_pesticide_calque_trapped(self):
        text = "ধান ক্ষেতে পোকা মারার ওষুধ সঠিক মাত্রায় প্রয়োগ করুন।"
        issues = lint_text(text)
        self.assertTrue(any("বালাইনাশক" in i.suggestion for i in issues))

if __name__ == "__main__":
    unittest.main()
