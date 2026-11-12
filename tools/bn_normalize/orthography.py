# tools/bn_normalize/orthography.py
import re

# Direct stem/root replacements for foreign loanwords with S (Bangla Academy rule)
# Foreign words with /s/ or /st/ should use 'স্ট' or 'স', never 'ষ্ট' or 'ষ'
LOANWORD_S_ROOTS = [
    ("রেজিষ্ট্রেশন", "রেজিস্ট্রেশন"),
    ("রেজিষ্ট্রি", "রেজিস্ট্রি"),
    ("ষ্টেশন", "স্টেশন"),
    ("মাষ্টার", "মাস্টার"),
    ("পোষ্টার", "পোস্টার"),
    ("পোষ্ট", "পোস্ট"),
    ("ষ্টুডিও", "স্টুডিও"),
    ("ষ্ট্যান্ড", "স্ট্যান্ড"),
    ("ষ্টোর", "স্টোর"),
    ("কাষ্টমার", "কাস্টমার"),
    ("ট্যাক্সী", "ট্যাক্সি"),
    ("ক্লাষ", "ক্লাস"),
]

# Tatbhava / Desi words that must take short-vowel 'ি' (হ্রস্ব-ইকার) under modern orthography
TATBHAVA_SHORT_VOWEL_ROOTS = [
    ("পাখী", "পাখি"),
    ("হাতী", "হাতি"),
    ("দাদী", "দাদি"),
    ("নানী", "নানি"),
    ("চাচী", "চাচি"),
    ("মামী", "মামি"),
    ("শাড়ী", "শাড়ি"),
    ("বাড়ী", "বাড়ি"),
    ("গাড়ী", "গাড়ি"),
    ("তরকারী", "তরকারি"),
    ("সরকারী", "সরকারি"),
    ("ফার্সী", "ফারসি"),
    ("আরবী", "আরবি"),
    ("ইংরেজী", "ইংরেজি"),
    ("বাঙালী", "বাঙালি"),
    ("কেরানী", "কেরানি")
]

def normalize_orthography(text: str, profile: str = "bd_standard") -> str:
    """
    Enforces standardized orthographic rules based on the selected profile.
    Default profile 'bd_standard' enforces modern Bangla Academy rules:
    - Foreign loanwords use 'স'/'স্ট', not 'ষ'/'ষ্ট'.
    - Tatbhava/desi/foreign words use short-vowel 'ি', not 'ী'.
    """
    if not text:
        return ""

    if profile == "bd_standard":
        # 1. Loanword S replacements (stem-aware)
        for bad_stem, good_stem in LOANWORD_S_ROOTS:
            text = text.replace(bad_stem, good_stem)

        # Handle 'বাষ' (bus) strictly at word boundaries to avoid altering 'বাষট্টি' (62), 'সুভাষ', or 'বাষ্প' (vapor)
        text = re.sub(r"(?<![\u0980-\u09FF])বাষ(?=(?:ে|ের|টা|টি|গুলো|গুলা)?(?![\u0980-\u09FF]))", "বাস", text)

        # 2. Tatbhava short-vowel replacements
        for bad_stem, good_stem in TATBHAVA_SHORT_VOWEL_ROOTS:
            text = text.replace(bad_stem, good_stem)

    return text
