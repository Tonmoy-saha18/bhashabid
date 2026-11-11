# tools/bn_lint/guru_chandali.py
# Sadhu-Cholito mixing detection (গুরুচণ্ডালী দোষ)
import re
from .models import LintIssue, LintSeverity
from ..bn_normalize.unicode import canonicalize_unicode

SADHU_MARKERS = {
    "আসিয়া": "এসে",
    "করিয়াছিল": "করেছিল",
    "করিয়া": "করে",
    "যাইয়া": "গিয়ে",
    "বলিয়া": "বলে",
    "দেখিয়া": "দেখে",
    "খাইয়া": "খেয়ে",
    "লইয়া": "নিয়ে",
    "যাইবে": "যাবে",
    "হইবে": "হবে",
    "তাহারা": "তারা",
    "উহারা": "ওরা",
    "সহিত": "সাথে / সঙ্গে",
    "বসিয়া": "বসে",
    "গিয়াছিল": "গিয়েছিল"
}

CHOLITO_MARKERS = {
    "করেছিল", "এসে", "করে", "গিয়ে", "বলে", "দেখে",
    "খেয়ে", "নিয়ে", "যাবে", "হবে", "তারা", "ওরা",
    "সাথে", "সঙ্গে", "বসে", "গিয়েছিল", "গেল", "গেলেন",
    "করল", "করলেন", "বলল", "বললেন", "খেল", "খেলেন",
    "এলো", "এলেন", "ছিল", "ছিলেন", "হলো", "হলেন"
}

def is_word_in_text(word: str, text: str) -> bool:
    pattern = r"(?<![\u0980-\u09FF])" + re.escape(word) + r"(?![\u0980-\u09FF])"
    return bool(re.search(pattern, text))

def check_guru_chandali(text: str) -> list[LintIssue]:
    issues = []
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, start=1):
        found_sadhu = [s for s in SADHU_MARKERS if is_word_in_text(s, line)]
        found_cholito = [c for c in CHOLITO_MARKERS if is_word_in_text(c, line)]

        # If both Sadhu and Cholito markers co-occur in the same line/sentence
        if found_sadhu and found_cholito:
            for s in found_sadhu:
                col = line.find(s) + 1
                suggestion = SADHU_MARKERS[s]
                issues.append(LintIssue(
                    rule_id="RULE-LINT-GURU-CHANDALI",
                    message=f"গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('{s}') ও চলিত রীতির মিশ্রণ ঘটেছে।",
                    line=line_idx,
                    col=col,
                    severity=LintSeverity.ERROR,
                    matched_text=s,
                    suggestion=f"চলিত রূপে '{suggestion}' ব্যবহার করুন।"
                ))

    return issues
