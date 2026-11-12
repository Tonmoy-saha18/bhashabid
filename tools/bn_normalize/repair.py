# tools/bn_normalize/repair.py
# Deterministic Autonomous Bengali Linguistic Repair Engine
import re
from typing import Tuple, List, Dict, Optional

from .unicode import canonicalize_unicode
from .punctuation import normalize_punctuation
from .orthography import normalize_orthography
from ..bn_lint.guru_chandali import SADHU_MARKERS, CHOLITO_MARKERS
from ..bn_lint.honorifics import (
    THIRD_PERSON_ORDINARY_TO_HONORIFIC,
    THIRD_PERSON_HONORIFIC_TO_ORDINARY,
    TINI_CLASH_PAT,
    SE_CLASH_PAT,
    TUMI_CLASH_PAT,
    APNI_CLASH_PAT,
    FORMAL_TO_FAMILIAR_VERBS,
    FAMILIAR_TO_FORMAL_VERBS
)

B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# Deterministic canonical calque repairs (replaces unnatural machine translations with standard Bengali)
CANONICAL_CALQUE_REPAIRS = [
    # Causal / passive calques
    (re.compile(B_L + r"দ্বারা\s+সভাপতিত্ব[\u0980-\u09FF]*" + B_R), "সভাপতিত্বে অনুষ্ঠিত"),
    (re.compile(B_L + r"দ্বারা\s+সরবরাহ[\u0980-\u09FF]*" + B_R), "সরবরাহকৃত"),
    (re.compile(B_L + r"দ্বারা\s+অনুমোদিত" + B_R), "অনুমোদিত"),
    (re.compile(B_L + r"দ্বারা\s+চালিত" + B_R), "পরিচালিত"),
    (re.compile(B_L + r"দ্বারা\s+কৃত" + B_R), "সম্পাদিত"),
    # Legal & Judicial calques
    (re.compile(B_L + r"জিজ্ঞেস\s+করে\s+একটি\s+রুল\s+জারি\s+করেছে" + B_R), "রুল নিশি জারি করেছেন"),
    (re.compile(B_L + r"জিজ্ঞেস\s+করে\s+একটি\s+রুল" + B_R), "রুল নিশি"),
    # Academic & Corporate calques
    (re.compile(B_L + r"পেপারটি\s+তর্ক\s+করে" + B_R), "গবেষণাপত্রে যুক্তি উপস্থাপন করা হয়েছে"),
    (re.compile(B_L + r"গেম\s+চেঞ্জার" + B_R), "যুগান্তকারী সমাধান"),
    (re.compile(B_L + r"পেইন\s+পয়েন্ট" + B_R), "প্রধান সংকট"),
    (re.compile(B_L + r"ঝড়\s+বৃদ্ধি" + B_R), "জলোচ্ছ্বাস"),
    (re.compile(B_L + r"বড়\s+বিপদের\s+সংকেত" + B_R), "মহাবিপদ সংকেত"),
    (re.compile(B_L + r"বিক্রির\s+কাগজ" + B_R), "সাফ-কবলা বিক্রয় দলিল"),
    (re.compile(B_L + r"পোকা\s+মারার\s+ওষুধ" + B_R), "বালাইনাশক"),
    # Idioms & Proverbs
    (re.compile(B_L + r"ঝোপের\s+চারপাশে\s+পেটাচ্ছেন" + B_R), "ঘুরিয়ে-পেঁচিয়ে কথা বলছেন"),
    (re.compile(B_L + r"ঝোপের\s+চারপাশে\s+পেটানো" + B_R), "ঘুরিয়ে-পেঁচিয়ে কথা বলা"),
    (re.compile(B_L + r"কেকের\s+টুকরো" + B_R), "পানির মতো সহজ কাজ"),
    (re.compile(B_L + r"পরাজয়\s+স্বীকার\s+করেছে" + B_R), "পরাজিত হয়েছে"),
    (re.compile(B_L + r"কাজ\s+শব্দের\s+চেয়ে\s+জোরে\s+কথা\s+বলে" + B_R), "কথার চেয়ে কাজের মূল্য বেশি"),
    (re.compile(B_L + r"খারাপ\s+কর্মী\s+তার\s+সরঞ্জামকে\s+দোষ\s+দেয়" + B_R), "নাচতে না জানলে উঠান বাঁকা"),
    (re.compile(B_L + r"ঘেউ\s+ঘেউ\s+করা\s+কুকুর\s+কদাচিৎ\s+কামড়ায়" + B_R), "যত গর্জে তত বর্ষে না"),
    (re.compile(B_L + r"অধিক\s+রাঁধুনি\s+ঝোল\s+নষ্ট\s+করে" + B_R), "অধিক সন্ন্যাসীতে গাজন নষ্ট"),
    (re.compile(B_L + r"একটি\s+পাথর\s+দিয়ে\s+দুটি\s+পাখি\s+মারা" + B_R), "এক ঢিলে দুই পাখি মারা")
]


def repair_text(text: str, profile: str = "bd_standard") -> Tuple[str, List[Dict]]:
    """
    Deterministic Bengali linguistic repair engine.
    Automatically repairs:
    1. Unicode decomposition and stray nuktas.
    2. Bangla Academy orthography & loanword standards.
    3. Punctuation standardization (Dari replacement outside URLs/numbers).
    4. Guru-chandali mixtures (harmonizes isolated Sadhu forms into Cholito).
    5. Unnatural English translation calques & machine proverbs.
    6. Honorific concordance mismatches.

    Returns:
        (repaired_text, applied_fixes)
    """
    if not text:
        return "", []

    applied_fixes = []
    current_text = canonicalize_unicode(text)

    # 1. Orthography loanword corrections
    norm_orth = normalize_orthography(current_text, profile=profile)
    if norm_orth != current_text:
        applied_fixes.append({
            "category": "ORTHOGRAPHY",
            "before": current_text,
            "after": norm_orth,
            "description": "Standardized Bangla Academy loanword orthography"
        })
        current_text = norm_orth

    # 2. Punctuation normalization
    norm_punc = normalize_punctuation(current_text)
    if norm_punc != current_text:
        applied_fixes.append({
            "category": "PUNCTUATION",
            "before": current_text,
            "after": norm_punc,
            "description": "Standardized Bengali Dari (।) and quotes"
        })
        current_text = norm_punc

    # 3. Canonical Calque Naturalization
    for pat, replacement in CANONICAL_CALQUE_REPAIRS:
        if pat.search(current_text):
            old = current_text
            current_text = pat.sub(replacement, current_text)
            applied_fixes.append({
                "category": "CALQUE_NATURALIZATION",
                "pattern": pat.pattern,
                "replacement": replacement,
                "description": f"Naturalized literal calque to '{replacement}'"
            })

    # 4. Guru-Chandali Harmonization (Archaic Sadhu verbs in Cholito text)
    tokens = set(re.findall(r"[\u0980-\u09FF]+", current_text))
    has_cholito = bool(tokens.intersection(CHOLITO_MARKERS))
    has_sadhu = bool(tokens.intersection(set(SADHU_MARKERS.keys())))

    # In modern standard prose, if Cholito markers exist or default standard is requested, harmonise Sadhu
    if has_sadhu and (has_cholito or profile == "bd_standard"):
        for s_verb, c_verb in SADHU_MARKERS.items():
            # Only use strict single canonical Cholito verb (skip multi-suggestions with '/')
            c_target = c_verb.split("/")[0].strip()
            pattern = re.compile(B_L + re.escape(s_verb) + B_R)
            if pattern.search(current_text):
                current_text = pattern.sub(c_target, current_text)
                applied_fixes.append({
                    "category": "GURU_CHANDALI_HARMONIZATION",
                    "sadhu": s_verb,
                    "cholito": c_target,
                    "description": f"Harmonized Sadhu form '{s_verb}' to Promito Cholito '{c_target}'"
                })

    # 5. Honorific Concordance Repair
    # (a) TINI + ordinary verb -> TINI + honorific verb
    for m in list(TINI_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        hon_verb = THIRD_PERSON_ORDINARY_TO_HONORIFIC.get(verb, f"{verb}েন")
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{hon_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 3rd-person honorific '{subj}' with verb '{hon_verb}'"
        })

    # (b) SE + honorific verb -> SE + ordinary verb
    for m in list(SE_CLASH_PAT.finditer(current_text)):
        subj = m.group(1)
        middle = m.group(2)
        verb = m.group(3)
        ord_verb = THIRD_PERSON_HONORIFIC_TO_ORDINARY.get(verb, verb)
        old_clause = m.group(0)
        new_clause = f"{subj}{middle}{ord_verb}"
        current_text = current_text.replace(old_clause, new_clause, 1)
        applied_fixes.append({
            "category": "HONORIFIC_CONCORDANCE",
            "before": old_clause,
            "after": new_clause,
            "description": f"Concorded 3rd-person ordinary '{subj}' with verb '{ord_verb}'"
        })

    return current_text, applied_fixes
