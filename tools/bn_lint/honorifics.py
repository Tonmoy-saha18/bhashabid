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

# 1. আপনি + informal verbs
APNI_CLASH_PAT = (
    B_L + r"(আপনি|আপনারা)" + B_R +
    r"([^।?!,;:]*?)" +
    B_L + r"(করো|যাও|বলো|খাও|দেখো|নাও|দাও|হও|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R
)

# 2. তুমি + formal or intimate verbs
TUMI_CLASH_PAT = (
    B_L + r"(তুমি|তোমরা)" + B_R +
    r"([^।?!,;:]*?)" +
    B_L + r"(করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R
)

# 3. তুই + formal verbs
TUI_CLASH_PAT = (
    B_L + r"(তুই|তোরা)" + B_R +
    r"([^।?!,;:]*?)" +
    B_L + r"(করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন)" + B_R
)

def check_honorific_clash(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        # 1. Check তুমি clash (e.g. তুমি সিদ্ধান্ত নেন -> তুমি সিদ্ধান্ত নাও OR আপনি সিদ্ধান্ত নেন)
        m_tumi = re.search(TUMI_CLASH_PAT, line)
        if m_tumi:
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

        # 2. Check আপনি clash (e.g. আপনি কাজটি করো -> আপনি কাজটি করেন OR তুমি কাজটি করো)
        m_apni = re.search(APNI_CLASH_PAT, line)
        if m_apni:
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
        m_tui = re.search(TUI_CLASH_PAT, line)
        if m_tui:
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

    return issues
