# tools/bn_lint/honorifics.py
# Honorific Concordance Linter (আপনি / তুমি / তুই)
import re
from .models import LintIssue, LintSeverity

# Boundary helper for Bengali tokens
B_L = r"(?<![\u0980-\u09FF])"
B_R = r"(?![\u0980-\u09FF])"

# 1. আপনি + informal verbs (করো, করিস, যাও, যাবি, বলো, বলিস, দেখিস)
APNI_CLASH_PATTERNS = [
    (B_L + r"আপনি" + B_R + r"[^।?!,;:]*?" + B_L + r"(করো|যাও|বলো|খাও|দেখো|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R, "আপনি", "-েন (করেন, যান, বলেন)"),
    (B_L + r"আপনারা" + B_R + r"[^।?!,;:]*?" + B_L + r"(করো|যাও|বলো|খাও|দেখো|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R, "আপনারা", "-েন (করেন, যান, বলেন)"),
]

# 2. তুমি + formal or intimate verbs (করেন, করিস, যান, যাবি, নেন, দেন)
TUMI_CLASH_PATTERNS = [
    (B_L + r"তুমি" + B_R + r"[^।?!,;:]*?" + B_L + r"(করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R, "তুমি", "-ো (করো, যাবে, বলো, নাও, দাও)"),
    (B_L + r"তোমরা" + B_R + r"[^।?!,;:]*?" + B_L + r"(করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করিস|যাবি|বলিস|খাস|দেখিস)" + B_R, "তোমরা", "-ো (করো, যাবে, বলো, নাও, দাও)"),
]

# 3. তুই + formal verbs (করেন, যান, বলেন, নেন, দেন)
TUI_CLASH_PATTERNS = [
    (B_L + r"তুই" + B_R + r"[^।?!,;:]*?" + B_L + r"(করেন|যান|বলেন|খান|দেখেন|নেন|দেন|হোন|করবেন|যাবেন)" + B_R, "তুই", "-িস/-বি (করিস, যাবি, বলিস)"),
]

def check_honorific_clash(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    all_patterns = [
        ("RULE-LINT-HONORIFIC-APNI", APNI_CLASH_PATTERNS),
        ("RULE-LINT-HONORIFIC-TUMI", TUMI_CLASH_PATTERNS),
        ("RULE-LINT-HONORIFIC-TUI", TUI_CLASH_PATTERNS)
    ]

    for line_idx, line in enumerate(lines, start=1):
        for rule_id, patterns in all_patterns:
            for pat, subject, expected_suffix in patterns:
                m = re.search(pat, line)
                if m:
                    matched = m.group(0)
                    col = m.start() + 1
                    issues.append(LintIssue(
                        rule_id=rule_id,
                        message=f"সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: '{subject}' এর সাথে বেমানান ক্রিয়াপদ ব্যবহার করা হয়েছে।",
                        line=line_idx,
                        col=col,
                        severity=LintSeverity.ERROR,
                        matched_text=matched,
                        suggestion=f"ক্রিয়াপদে যথাযথ বিভক্তি {expected_suffix} প্রয়োগ করুন।"
                    ))
    return issues
