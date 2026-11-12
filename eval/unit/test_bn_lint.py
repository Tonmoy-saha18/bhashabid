# Unit Tests for bn_lint
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_lint import lint_text, LintSeverity

class TestBnLint(unittest.TestCase):

    def test_clean_text_no_issues(self):
        text = "তিনি প্রতিদিন সকালে বিদ্যালয়ে যান এবং পাঠদান করেন।"
        issues = lint_text(text)
        self.assertEqual(len(issues), 0)

    def test_guru_chandali_detection(self):
        # Mixing 'আসিয়া' (Sadhu) with 'গেল' (Cholito)
        text = "তিনি বাড়িতে আসিয়া ভাত খেলেন এবং বাজারে গেল।"
        issues = lint_text(text)
        self.assertTrue(any(i.rule_id == "RULE-LINT-GURU-CHANDALI" for i in issues))

        # Mixing 'পড়িয়া' (Sadhu) with 'দাও' (Cholito)
        text2 = "উদ্দীপকটি পড়িয়া নিচের প্রশ্নগুলোর উত্তর দাও।"
        issues2 = lint_text(text2)
        self.assertTrue(any(i.rule_id == "RULE-LINT-GURU-CHANDALI" for i in issues2))

    def test_honorific_clash_detection(self):
        # 'আপনি' with 'করো'
        text = "আপনি কি কাজটি আজ করো?"
        issues = lint_text(text)
        self.assertTrue(any("HONORIFIC" in i.rule_id for i in issues))

    def test_bidirectional_honorific_suggestions(self):
        # 'তুমি সিদ্ধান্ত নেন' must suggest both 'তুমি সিদ্ধান্ত নাও' and 'আপনি সিদ্ধান্ত নেন'
        text = "তুমি সিদ্ধান্ত নেন"
        issues = lint_text(text)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].rule_id, "RULE-LINT-HONORIFIC-TUMI")
        suggestion = issues[0].suggestion
        self.assertIn("তুমি সিদ্ধান্ত নাও", suggestion)
        self.assertIn("আপনি সিদ্ধান্ত নেন", suggestion)

    def test_calque_detection(self):
        text = "এই মেশিনটি বিদ্যুৎ দ্বারা চালিত এবং কাজটি তিনি দ্বারা কৃত।"
        issues = lint_text(text)
        self.assertTrue(any(i.rule_id == "RULE-LINT-CALQUE" for i in issues))

    def test_judicial_calque_detection(self):
        # High Court show-cause Rule Nisi calque 'জিজ্ঞেস করে একটি রুল'
        text = "হাইকোর্ট কেন এটি বেআইনি হবে না জিজ্ঞেস করে একটি রুল জারি করেছে।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        self.assertIn("জানতে চেয়ে রুল জারি করেছেন", calque_issues[0].suggestion)

    def test_sports_calque_detection(self):
        # Sports defeat calque 'পরাজয় স্বীকার করেছে'
        text = "বাংলাদেশ সফরকারীদের বিরুদ্ধে পরাজয় স্বীকার করেছে।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        from tools.bn_normalize import canonicalize_unicode
        self.assertIn(canonicalize_unicode("পরাজিত হয়েছে / হেরেছে"), calque_issues[0].suggestion)

    def test_application_salutation_calque(self):
        text = "প্রিয় মহাশয়, বিনীত নিবেদন এই যে এলাকার রাস্তা মেরামত প্রয়োজন।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        self.assertIn("মহোদয় / জনাব", calque_issues[0].suggestion)

    def test_letter_signoff_calque(self):
        text = "পত্রের সমাপ্তিতে তিনি লিখলেন আপনার বিশ্বস্তভাবে।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        self.assertIn("বিনীত / আপনার বিশ্বস্ত", calque_issues[0].suggestion)

    def test_academic_calque(self):
        text = "এই পেপারটি তর্ক করে যে সামাজিক মাধ্যম শিক্ষার্থীদের মনোযোগ নষ্ট করে।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        self.assertIn("প্রতিপাদ্য উপস্থাপিত হয়েছে", calque_issues[0].suggestion)

    def test_corporate_marketing_calque(self):
        text = "এটি একটি গেম চেঞ্জার পণ্য যা কাস্টমারের পেইন পয়েন্ট দূর করবে।"
        issues = lint_text(text)
        calque_issues = [i for i in issues if i.rule_id == "RULE-LINT-CALQUE"]
        self.assertTrue(len(calque_issues) >= 1)
        self.assertTrue(any("যুগান্তকারী" in i.suggestion for i in calque_issues))

    def test_statutory_calque_disambiguation(self):
        # Legitimate statutory phrases should not be falsely flagged as calques
        statutory_text = "উক্ত ক্ষমতা আইন দ্বারা অনুমোদিত এবং সংশ্লিষ্ট বিধি দ্বারা নির্ধারিত।"
        issues = lint_text(statutory_text)
        self.assertEqual(len(issues), 0, "Legitimate statutory 'দ্বারা' must not trigger false calque warnings")

        # But translation passive calques MUST still be trapped
        calque_text = "প্রকল্পটি সম্পূর্ণভাবে বিদ্যুৎ বিভাগ দ্বারা চালিত।"
        calque_issues = lint_text(calque_text)
        self.assertTrue(any(i.rule_id == "RULE-LINT-CALQUE" for i in calque_issues))

if __name__ == "__main__":
    unittest.main()
