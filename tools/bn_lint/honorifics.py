# tools/bn_lint/honorifics.py
# Honorific Concordance Linter (আপনি / তুমি / তুই) with Bidirectional Repair
import re
from .models import LintIssue, LintSeverity

# Boundary helper for Bengali tokens
B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# Verb transformation dictionaries
FORMAL_TO_FAMILIAR_VERBS = {
    "করেন": "করো", "যান": "যাও", "বলেন": "বলো", "খান": "খাও",
    "দেখেন": "দেখো", "নেন": "নাও", "দেন": "দাও", "হোন": "হও",
    "আসেন": "এসো", "করবেন": "করবে", "যাবেন": "যাবে"
}

FAMILIAR_TO_FORMAL_VERBS = {
    "করো": "করেন", "যাও": "যান", "বলো": "বলেন", "খাও": "খান",
    "দেখো": "দেখেন", "নাও": "নেন", "দাও": "দেন", "হও": "হোন",
    "এসো": "আসেন", "করবে": "করবেন", "যাবে": "যাবেন"
}

INTIMATE_TO_FAMILIAR_VERBS = {
    "করিস": "করো", "যাবি": "যাবে", "বলিস": "বলো", "খাস": "খাও",
    "দেখিস": "দেখো", "নিস": "নাও", "দিস": "দাও", "করবি": "করবে"
}

# Third-person verb mappings (তিনি vs সে)
THIRD_PERSON_ORDINARY_TO_HONORIFIC = {
    "বলল": "বললেন", "করল": "করলেন", "গেল": "গেলেন", "খেল": "খেলেন",
    "দেখল": "দেখলেন", "নিল": "নিলেন", "দিল": "দিলেন", "বলে": "বলেন",
    "করে": "করেন", "যায়": "যান", "খায়": "খান", "দেখে": "দেখেন",
    "হলো": "হলেন", "বলবে": "বলবেন", "করবে": "করবেন", "যাবে": "যাবেন"
}

THIRD_PERSON_HONORIFIC_TO_ORDINARY = {
    v: k for k, v in THIRD_PERSON_ORDINARY_TO_HONORIFIC.items()
}

# 1. আপনি + informal verbs
APNI_CLASH_PAT = re.compile(
    B_L + r"(আপনি|আপনারা)" + B_R +
    r"((?:(?!আপনি|আপনারা)[^।?!,;:\n])*?)" +
    B_L + r"(করো|যাও|বলো|খাও|দেখো|নাও|দাও|হও|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R
)

# 2. তুমি + formal or intimate verbs
TUMI_CLASH_PAT = re.compile(
    B_L + r"(তুমি|তোমরা)" + B_R +
    r"((?:(?!তুমি|তোমরা)[^।?!,;:\n])*?)" +
    B_L + r"(আসেন|করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R
)

# 3. তুই + formal verbs
TUI_CLASH_PAT = re.compile(
    B_L + r"(তুই|তোরা)" + B_R +
    r"((?:(?!তুই|তোরা)[^।?!,;:\n])*?)" +
    B_L + r"(আসেন|করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন)" + B_R
)

# 4. তিনি / তাঁরা + ordinary verbs (e.g. তিনি বলল -> তিনি বললেন OR সে বলল)
TINI_CLASH_PAT = re.compile(
    B_L + r"(তিনি|তাঁরা)" + B_R +
    r"((?:(?!তিনি|তাঁরা)[^।?!,;:\n])*?)" +
    B_L + r"(বলল|করল|গেল|খেল|দেখল|নিল|দিল|বলে|করে|যায়|খায়|দেখে|বলবে|করবে|যাবে)" + B_R
)

# 5. সে / তারা + honorific verbs (e.g. সে বললেন -> সে বলল OR তিনি বললেন)
SE_CLASH_PAT = re.compile(
    B_L + r"(সে|তারা)" + B_R +
    r"((?:(?!সে|তারা)[^।?!,;:\n])*?)" +
    B_L + r"(বললেন|করলেন|গেলেন|খেলেন|দেখলেন|নিলেন|দিলেন|বলেন|করেন|খান|দেখেন|বলবেন|করবেন|যাবেন)" + B_R
)

def check_honorific_clash(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        # 1. Check তুমি clash
        for m_tumi in TUMI_CLASH_PAT.finditer(line):
            subj = m_tumi.group(1)
            middle = m_tumi.group(2)
            verb = m_tumi.group(3)
            matched = m_tumi.group(0)

            if verb in FORMAL_TO_FAMILIAR_VERBS:
                correct_familiar_verb = FORMAL_TO_FAMILIAR_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_familiar_verb}"
                formal_subj = "আপনি" if subj == "তুমি" else "আপনারা"
                opt2 = f"{formal_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১ (ক্রিয়াপদ পরিবর্তন): '{opt1}' অথবা বিকল্প ২ (সর্বনাম পরিবর্তন): '{opt2}'"
            elif verb in INTIMATE_TO_FAMILIAR_VERBS:
                correct_familiar_verb = INTIMATE_TO_FAMILIAR_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_familiar_verb}"
                intimate_subj = "তুই" if subj == "তুমি" else "তোরা"
                opt2 = f"{intimate_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১: '{opt1}' অথবা বিকল্প ২: '{opt2}'"
            else:
                suggestion = f"ক্রিয়াপদে যথাযথ বিভক্তি প্রয়োগ করুন।"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TUMI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সাধারণ) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tumi.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 2. Check আপনি clash
        for m_apni in APNI_CLASH_PAT.finditer(line):
            subj = m_apni.group(1)
            middle = m_apni.group(2)
            verb = m_apni.group(3)
            matched = m_apni.group(0)

            if verb in FAMILIAR_TO_FORMAL_VERBS:
                correct_formal_verb = FAMILIAR_TO_FORMAL_VERBS[verb]
                opt1 = f"{subj}{middle}{correct_formal_verb}"
                familiar_subj = "তুমি" if subj == "আপনি" else "তোমরা"
                opt2 = f"{familiar_subj}{middle}{verb}"
                suggestion = f"বিকল্প ১ (ক্রিয়াপদ পরিবর্তন): '{opt1}' অথবা বিকল্প ২ (সর্বনাম পরিবর্তন): '{opt2}'"
            else:
                suggestion = f"ক্রিয়াপদে যথাযথ সম্ভ্রমাত্মক বিভক্তি (-েন) প্রয়োগ করুন।"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-APNI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সম্ভ্রমাত্মক) এর সাথে বেমানান ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_apni.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 3. Check তুই clash
        for m_tui in TUI_CLASH_PAT.finditer(line):
            subj = m_tui.group(1)
            matched = m_tui.group(0)
            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TUI",
                message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (ঘনিষ্ঠ/তুচ্ছার্থ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tui.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion="ঘনিষ্ঠ রূপে -িস/-বি (যেমন: করিস, যাবি) ব্যবহার করুন।"
            ))

        # 4. Check তিনি / তাঁরা clash (3rd person honorific pronoun + non-honorific verb)
        for m_tini in TINI_CLASH_PAT.finditer(line):
            subj = m_tini.group(1)
            middle = m_tini.group(2)
            verb = m_tini.group(3)
            matched = m_tini.group(0)
            hon_verb = THIRD_PERSON_ORDINARY_TO_HONORIFIC.get(verb, f"{verb}েন")
            ord_subj = "সে" if subj == "তিনি" else "তারা"
            suggestion = f"বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): '{subj}{middle}{hon_verb}' অথবা বিকল্প ২ (সাধারণ সর্বনাম): '{ord_subj}{middle}{verb}'"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-TINI",
                message=f"তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_tini.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

        # 5. Check সে / তারা clash (3rd person ordinary pronoun + honorific verb)
        for m_se in SE_CLASH_PAT.finditer(line):
            subj = m_se.group(1)
            middle = m_se.group(2)
            verb = m_se.group(3)
            matched = m_se.group(0)
            ord_verb = THIRD_PERSON_HONORIFIC_TO_ORDINARY.get(verb, verb)
            hon_subj = "তিনি" if subj == "সে" else "তাঁরা"
            suggestion = f"বিকল্প ১ (সাধারণ ক্রিয়াপদ): '{subj}{middle}{ord_verb}' অথবা বিকল্প ২ (সম্ভ্রমাত্মক সর্বনাম): '{hon_subj}{middle}{verb}'"

            issues.append(LintIssue(
                rule_id="RULE-LINT-HONORIFIC-SE",
                message=f"তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subj}' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ '{verb}' ব্যবহার করা হয়েছে।",
                line=line_idx,
                col=m_se.start() + 1,
                severity=LintSeverity.ERROR,
                matched_text=matched,
                suggestion=suggestion
            ))

    return issues
