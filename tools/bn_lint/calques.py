# tools/bn_lint/calques.py
# English Calque and Unnatural Passive Linter
import re
from .models import LintIssue, LintSeverity
from ..bn_normalize.unicode import canonicalize_unicode

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

RAW_UNNATURAL_CALQUES = [
    (B_L + r"দ্বারা\s+সভাপতিত্ব\w*" + B_R, "দ্বারা সভাপতিত্ব", "সভাপতিত্বে অনুষ্ঠিত"),
    (B_L + r"দ্বারা\s+সরবরাহ\w*" + B_R, "দ্বারা সরবরাহ", "সরবরাহ করবে / যোগান দেবে"),
    (B_L + r"দ্বারা\s+অনুমোদিত" + B_R, "দ্বারা অনুমোদিত", "অনুমোদন করেছে / কর্তৃক অনুমোদিত"),
    (B_L + r"দ্বারা\s+চালিত" + B_R, "দ্বারা চালিত", "চালিত / পরিচালিত"),
    (B_L + r"দ্বারা\s+কৃত" + B_R, "দ্বারা কৃত", "সম্পাদিত / করা"),
    (B_L + r"জিজ্ঞেস\s+করে\s+একটি\s+রুল" + B_R, "জিজ্ঞেস করে একটি রুল", "কেন ... হবে না, তা জানতে চেয়ে রুল জারি করেছেন"),
    (B_L + r"পরাজয়\s+স্বীকার\s+করেছে" + B_R, "পরাজয় স্বীকার করেছে", "পরাজিত হয়েছে / হেরেছে"),
    (B_L + r"কাজ\s+শব্দের\s+চেয়ে\s+জোরে\s+কথা\s+বলে" + B_R, "কাজ শব্দের চেয়ে জোরে কথা বলে", "কথার চেয়ে কাজের মূল্য বেশি"),
    (B_L + r"প্রিয়\s+মহাশয়" + B_R, "প্রিয় মহাশয়", "মহোদয় / জনাব"),
    (B_L + r"আপনার\s+বিশ্বস্তভাবে" + B_R, "আপনার বিশ্বস্তভাবে", "বিনীত / আপনার বিশ্বস্ত"),
    (B_L + r"পেপারটি\s+তর্ক\s+করে" + B_R, "পেপারটি তর্ক করে", "প্রবন্ধে প্রতিপাদ্য উপস্থাপিত হয়েছে / গবেষণায় প্রতীয়মান হয়"),
    (B_L + r"গেম\s+চেঞ্জার" + B_R, "গেম চেঞ্জার", "যুগান্তকারী সমাধান / উদ্যোগ"),
    (B_L + r"পেইন\s+পয়েন্ট" + B_R, "পেইন পয়েন্ট", "কষ্টসাধ্য সমস্যা / প্রধান সংকট"),
    (B_L + r"ঝড়\s+বৃদ্ধি" + B_R, "ঝড় বৃদ্ধি", "জলোচ্ছ্বাস"),
    (B_L + r"বড়\s+বিপদের\s+সংকেত" + B_R, "বড় বিপদের সংকেত", "মহাবিপদ সংকেত"),
    (B_L + r"বিক্রির\s+কাগজ" + B_R, "বিক্রির কাগজ", "সাফ-কবলা বিক্রয় দলিল"),
    (B_L + r"পোকা\s+মারার\s+ওষুধ" + B_R, "পোকা মারার ওষুধ", "বালাইনাশক / কীটনাশক"),
]

# Canonicalize all patterns at module load time to guarantee zero nukta mismatch
UNNATURAL_CALQUES = [
    (canonicalize_unicode(pat), canonicalize_unicode(label), canonicalize_unicode(sugg))
    for pat, label, sugg in RAW_UNNATURAL_CALQUES
]

def check_calques(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        for pat, matched_label, suggestion in UNNATURAL_CALQUES:
            m = re.search(pat, line)
            if m:
                col = m.start() + 1
                issues.append(LintIssue(
                    rule_id="RULE-LINT-CALQUE",
                    message=f"অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: '{matched_label}' প্রমিত বাংলায় কৃত্রিম শোনায়।",
                    line=line_idx,
                    col=col,
                    severity=LintSeverity.WARNING,
                    matched_text=m.group(0),
                    suggestion=f"স্বাভাবিক বাংলা প্রকাশভঙ্গি '{suggestion}' ব্যবহার করুন।"
                ))

    return issues
