# English Calque and Unnatural Passive Linter
import re
from .models import LintIssue, LintSeverity

UNNATURAL_CALQUES = [
    (r"\bদ্বারা\s+কৃত\b", "দ্বারা কৃত", "কর্তৃক সম্পাদিত / করা"),
    (r"\bদ্বারা\s+চালিত\b", "দ্বারা চালিত", "চালিত / পরিচালিত"),
    (r"কাজ\s+শব্দের\s+চেয়ে\s+জোরে\s+কথা\s+বলে", "কাজ শব্দের চেয়ে জোরে কথা বলে", "কথার চেয়ে কাজের মূল্য বেশি"),
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
                    message=f"অস্বাভাবিক ইংরেজি ক্যাল্ক (আক্ষরিক অনুবাদ): '{matched_label}' প্রমিত বাংলায় কৃত্রিম শোনায়।",
                    line=line_idx,
                    col=col,
                    severity=LintSeverity.WARNING,
                    matched_text=m.group(0),
                    suggestion=f"স্বাভাবিক বাংলা প্রকাশভঙ্গি '{suggestion}' ব্যবহার করুন।"
                ))

    return issues
