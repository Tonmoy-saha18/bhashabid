# tools/bn_prosody/metre.py
# Bengali Metre Analysis & Scansion (ছন্দ ও মাত্রাগণনা)
from dataclasses import dataclass
from typing import List, Tuple
from .syllable import syllabify_line, SyllableType, Syllable
from ..bn_normalize.unicode import canonicalize_unicode

@dataclass
class LineScansionResult:
    line: str
    metre_system: str
    total_morae: int
    total_syllables: int
    open_syllables: int
    closed_syllables: int
    word_mora_breakdown: List[Tuple[str, int]]
    scansion_notation: str  # e.g. "∪ – | ∪ ∪ –"

@dataclass
class PayarValidationResult:
    is_valid_payar: bool
    line: str
    part1_morae: int
    part2_morae: int
    total_morae: int
    explanation: str

def scan_line(line: str, metre_system: str = "aksharbritta") -> LineScansionResult:
    """
    Performs full poetic scansion on a single line of Bengali verse.
    metre_system can be: 'aksharbritta' (default), 'matrabritta', or 'dalabritta'.
    """
    words_syllables = syllabify_line(line)
    total_morae = 0
    total_syllables = 0
    open_count = 0
    closed_count = 0
    breakdown = []
    notation_words = []

    for word_syls in words_syllables:
        if not word_syls:
            continue
        word_text = "".join(s.text for s in word_syls)
        word_morae = sum(s.mora_count(metre_system) for s in word_syls)
        total_morae += word_morae
        total_syllables += len(word_syls)

        word_notation = []
        for s in word_syls:
            if s.syllable_type == SyllableType.OPEN:
                open_count += 1
                word_notation.append("∪")
            else:
                closed_count += 1
                word_notation.append("–")

        breakdown.append((word_text, word_morae))
        notation_words.append(" ".join(word_notation))

    scansion_notation = " | ".join(notation_words)

    return LineScansionResult(
        line=line.strip(),
        metre_system=metre_system,
        total_morae=total_morae,
        total_syllables=total_syllables,
        open_syllables=open_count,
        closed_syllables=closed_count,
        word_mora_breakdown=breakdown,
        scansion_notation=scansion_notation
    )

def verify_payar(line: str) -> PayarValidationResult:
    """
    Validates whether a line conforms to classical Bengali 14-akshar Payar metre (৮ + ৬ = ১৪ মাত্রা/অক্ষর).
    Checks caesura (যতি) positioning and total syllable/mora count.
    """
    line = canonicalize_unicode(line.strip())
    scansion = scan_line(line, metre_system="aksharbritta")

    # In 14-akshar Payar, the caesura (মৌলিক যতি) falls after 8 units, followed by 6 units
    # Calculate running sum across words
    part1_morae = 0
    part2_morae = 0
    caesura_found = False

    running = 0
    for word, m in scansion.word_mora_breakdown:
        running += m
        if running == 8:
            caesura_found = True
            part1_morae = 8
            part2_morae = scansion.total_morae - 8
            break
        elif running > 8:
            break

    total = scansion.total_morae
    is_valid = (total == 14 and caesura_found)

    if is_valid:
        explanation = f"শুদ্ধ পয়ার ছন্দ: ৮+৬=১৪ মাত্রার পর্ব ও মধ্যযতি যথাযথভাবে বিন্যস্ত।"
    elif total == 14 and not caesura_found:
        explanation = f"মোট মাত্রা ১৪ হলেও মধ্যযতি (৮ মাত্রা পর) কোনো শব্দের মাঝে ভঙ্গ হয়েছে।"
    else:
        explanation = f"পয়ারের ১৪ মাত্রার স্থলে মোট {total} মাত্রা পাওয়া গেছে।"

    return PayarValidationResult(
        is_valid_payar=is_valid,
        line=line,
        part1_morae=part1_morae if caesura_found else running,
        part2_morae=part2_morae if caesura_found else (total - running),
        total_morae=total,
        explanation=explanation
    )

def verify_rhyme(line1: str, line2: str) -> bool:
    """
    Verifies end-rhyme (অন্ত্যমিল) between two lines of a couplet.
    """
    words1 = syllabify_line(line1)
    words2 = syllabify_line(line2)
    if not words1 or not words2:
        return False

    last_word1 = words1[-1]
    last_word2 = words2[-1]
    if not last_word1 or not last_word2:
        return False

    final_syl1 = last_word1[-1].text
    final_syl2 = last_word2[-1].text

    # Extract rhyming core (last 1-2 characters or shared matra)
    # Simple phonetic check: matching final sound or matra
    return final_syl1[-1] == final_syl2[-1]
