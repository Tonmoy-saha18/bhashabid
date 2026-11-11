# tools/bn_prosody/syllable.py
# Bengali Phonetic Syllabifier (দল বিভাজন ও বর্ণক্রম)
from dataclasses import dataclass
from enum import Enum
import re
from ..bn_normalize.unicode import canonicalize_unicode

class SyllableType(Enum):
    OPEN = "মুক্তদল"    # Vowel-ending (Mukto-dol)
    CLOSED = "রুদ্ধদল"  # Consonant-ending or closed diphthong (Ruddho-dol)

@dataclass
class Syllable:
    text: str
    syllable_type: SyllableType
    is_word_final: bool = False
    is_word_initial: bool = False
    is_monosyllabic: bool = False

    def mora_count(self, metre_system: str) -> int:
        """
        Calculates mora/akshar count based on the Bengali classical metre system:
        - dalabritta (দলবৃত্ত / স্বরবৃত্ত): মুক্তদল = 1, রুদ্ধদল = 1
        - matrabritta (মাত্রাবৃত্ত / কলাবৃত্ত): মুক্তদল = 1, রুদ্ধদল = 2
        - aksharbritta (অক্ষরবৃত্ত / পয়ার): প্রতিটি অক্ষর = ১ একক (৮ + ৬ = ১৪ অক্ষরের পর্ব)
        """
        if metre_system == "dalabritta":
            return 1  # In Dalabritta, all syllables have mora weight 1
        elif metre_system == "matrabritta":
            return 2 if self.syllable_type == SyllableType.CLOSED else 1
        elif metre_system == "aksharbritta":
            return 1  # Standard Payar counts individual akshars (8+6=14)
        return 1

VOWELS = set("অআইঈউঊঋএঐওঔ")
MATRAS = set("ািীুূৃেৈোৌ")
SIGNS = set("ংঃঁৎ")
HASANT = "্"

def syllabify_word(word: str) -> list[Syllable]:
    """
    Decomposes a single Bengali word into its constituent phonological syllables (দল).
    """
    word = canonicalize_unicode(word.strip())
    if not word:
        return []

    # Clean non-Bengali characters
    word = re.sub(r"[^\u0980-\u09FF]", "", word)
    if not word:
        return []

    # Split into phonetic units using clusters and matras
    # A standard Bengali phonetic syllable comprises:
    # (Consonant + Hasanta)* + Consonant + (Matra | implicit vowel) + (Hasanta + Consonant | Sign)?
    units = []
    i = 0
    n = len(word)

    while i < n:
        unit = word[i]
        i += 1
        # Include hasant conjuncts
        while i < n and word[i] == HASANT:
            unit += word[i]
            i += 1
            if i < n:
                unit += word[i]
                i += 1
        # Include vowel matras and signs
        while i < n and (word[i] in MATRAS or word[i] in SIGNS):
            unit += word[i]
            i += 1
        units.append(unit)

    # Now group units into syllables (onset + nucleus + coda)
    # In Bengali:
    # 1. If a unit ends with a vowel matra (া, ি, ী, ু, ূ, ৃ, ে, ৈ, ো, ৌ), it's OPEN unless followed by a coda hasant/sign.
    # 2. If a unit ends with ৎ, ং, ঃ, it's CLOSED.
    # 3. For the word-final consonant without a matra, standard Bengali pronunciation usually closes it
    #    (e.g. জল্ [jol], রাত্ [raat], মন [mon]) unless it has an inherent 'o' (যেমন: প্রিয়, শুভ).
    
    syllables = []
    num_units = len(units)

    for idx, u in enumerate(units):
        is_final = (idx == num_units - 1)
        is_initial = (idx == 0)
        is_mono = (num_units == 1)

        has_matra = any(c in MATRAS for c in u)
        has_sign = any(c in SIGNS for c in u)
        has_terminal_hasant = u.endswith(HASANT)

        # Determine if closed or open
        if has_sign or has_terminal_hasant:
            stype = SyllableType.CLOSED
        elif has_matra:
            stype = SyllableType.OPEN
        else:
            # Consonant with inherent vowel
            # In final position of multisyllabic words or monosyllabic words:
            # Word like 'জল' (1 unit) -> CLOSED [jol]
            # Word like 'নয়ন' -> 'ন' (OPEN) + 'য়ন' (CLOSED)
            if is_final:
                stype = SyllableType.CLOSED
            else:
                stype = SyllableType.OPEN

        syllables.append(Syllable(
            text=u,
            syllable_type=stype,
            is_word_final=is_final,
            is_word_initial=is_initial,
            is_monosyllabic=is_mono
        ))

    return syllables

def syllabify_line(line: str) -> list[list[Syllable]]:
    """
    Syllabifies a full line of Bengali verse into a list of words, each containing syllables.
    """
    words = re.findall(r"[\u0980-\u09FF]+", canonicalize_unicode(line))
    return [syllabify_word(w) for w in words]
