# tools/bn_lint/calques.py
# English Calque and Unnatural Passive Linter
import re
from .models import LintIssue, LintSeverity
from ..bn_normalize.unicode import canonicalize_unicode

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

RAW_UNNATURAL_CALQUES = [
    (B_L + r"দ্বারা\s+সভাপতিত্ব[\u0980-\u09FF]*" + B_R, "দ্বারা সভাপতিত্ব", "সভাপতিত্বে অনুষ্ঠিত"),
    (B_L + r"দ্বারা\s+সরবরাহ[\u0980-\u09FF]*" + B_R, "দ্বারা সরবরাহ", "সরবরাহ করবে / যোগান দেবে"),
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
    # Proverbs & Idiom Calques (Machine Translation Traps)
    (B_L + r"ঝোপের\s+চারপাশে\s+পেটা[\u0980-\u09FF]*" + B_R, "ঝোপের চারপাশে পেটানো", "ঘুরিয়ে-পেঁচিয়ে কথা বলা / মূল প্রসঙ্গ এড়িয়ে যাওয়া"),
    (B_L + r"কেকের\s+টুকরো" + B_R, "কেকের টুকরো", "পানির মতো সহজ / অতি সহজ কাজ / দুধভাত"),
    (B_L + r"পা\s+ভেঙে\s+ফে[\u0980-\u09FF]*" + B_R, "পা ভেঙে ফেলা", "শুভকামনা / শুভ সূচনা হোক"),
    (B_L + r"শিম\s+ছড়িয়ে\s+দে[\u0980-\u09FF]*" + B_R, "শিম ছড়িয়ে দেওয়া", "হাঁড়ি ভেঙে দেওয়া / গোপন তথ্য ফাঁস করা"),
    (B_L + r"মধ্যরাতের\s+তেল\s+পোড়া[\u0980-\u09FF]*" + B_R, "মধ্যরাতের তেল পোড়ানো", "রাত জেগে পড়ালেখা / কঠোর পরিশ্রম করা"),
    (B_L + r"খারাপ\s+কর্মী\s+তার\s+সরঞ্জাম[\u0980-\u09FF]*\s+দোষ[\u0980-\u09FF]*" + B_R, "খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়", "নাচতে না জানলে উঠান বাঁকা"),
    (B_L + r"ঘেউ\s+ঘেউ\s+করা\s+কুকুর\s+কদাচিৎ\s+কামড়া[\u0980-\u09FF]*" + B_R, "ঘেউ ঘেউ করা কুকুর কদাচিৎ কামড়ায়", "যত গর্জে তত বর্ষে না"),
    (B_L + r"হৃৎপিণ্ড\s+পাথরে\s+পরিণত[\u0980-\u09FF]*" + B_R, "হৃৎপিণ্ড পাথরে পরিণত", "হৃদয় পাষাণ হয়ে যাওয়া / মন শক্ত হওয়া"),
    (B_L + r"অধিক\s+রাঁধুনি\s+ঝোল\s+নষ্ট\s+ক[\u0980-\u09FF]*" + B_R, "অধিক রাঁধুনি ঝোল নষ্ট করে", "অধিক সন্ন্যাসীতে গাজন নষ্ট"),
    (B_L + r"একটি\s+পাথর\s+দিয়ে\s+দুটি\s+পাখি\s+মা[\u0980-\u09FF]*" + B_R, "একটি পাথর দিয়ে দুটি পাখি মারা", "এক ঢিলে দুই পাখি মারা / রথ দেখা ও কলা বেচা"),
]

# Canonicalize all patterns at module load time to guarantee zero nukta mismatch
UNNATURAL_CALQUES = [
    (canonicalize_unicode(pat), canonicalize_unicode(label), canonicalize_unicode(sugg))
    for pat, label, sugg in RAW_UNNATURAL_CALQUES
]

# Statutory legal and constitutional patterns where 'দ্বারা' is legally legitimate
PROTECTED_STATUTORY_PATTERNS = [
    re.compile(canonicalize_unicode(r"(?:আইন|সংবিধান|বিধি|আদালত|আদেশ)\s+দ্বারা\s+(?:অনুমোদিত|নির্ধারিত|অর্পিত|স্বীকৃত|প্রণীত|নির্দেশিত)"))
]

def check_calques(text: str, profile: str = "bd_standard") -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        for pat, matched_label, suggestion in UNNATURAL_CALQUES:
            for m in re.finditer(pat, line):
                matched_span = (m.start(), m.end())
                
                # Check if this match falls within a protected statutory context
                is_protected = False
                for stat_pat in PROTECTED_STATUTORY_PATTERNS:
                    for sm in stat_pat.finditer(line):
                        if sm.start() <= matched_span[0] and matched_span[1] <= sm.end():
                            is_protected = True
                            break
                    if is_protected:
                        break

                if not is_protected:
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
