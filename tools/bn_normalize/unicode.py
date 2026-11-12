# tools/bn_normalize/unicode.py
import unicodedata
import re

# Canonical Bengali atomic codepoints
CHAR_YO = "\u09df"        # য় (U+09DF)
CHAR_RRA = "\u09dc"       # ড় (U+09DC)
CHAR_RHHA = "\u09dd"      # ঢ় (U+09DD)
CHAR_KHANDA_TA = "\u09ce" # ৎ (U+09CE)
NUKTA = "\u09bc"          # ়
VIRAMA = "\u09cd"         # ্
ZWJ = "\u200d"
ZWNJ = "\u200c"

# Decomposed forms
DECOMPOSED_YO = "\u09af\u09bc"   # য + ়
DECOMPOSED_RRA = "\u09a1\u09bc"  # ড + ়
DECOMPOSED_RHHA = "\u09a2\u09bc" # ঢ + ়
DECOMPOSED_KHANDA_TA_ZWNJ = "\u09a4\u09cd" + ZWNJ # ত + ্ + ZWNJ
DECOMPOSED_KHANDA_TA_ZWJ = "\u09a4\u09cd" + ZWJ   # ত + ্ + ZWJ (Legacy OpenType Bijoy/Avro)
DECOMPOSED_KHANDA_TA = DECOMPOSED_KHANDA_TA_ZWNJ

def is_nfc_normalized(text: str) -> bool:
    """
    Check if string complies with Bengali canonical normalization:
    - Contains no decomposed nukta clusters (য+়, ড+়, ঢ+়)
    - Contains no decomposed Khanda-Ta ligatures (ত্‍)
    - Conforms to canonical form.
    """
    if DECOMPOSED_YO in text or DECOMPOSED_RRA in text or DECOMPOSED_RHHA in text:
        return False
    if DECOMPOSED_KHANDA_TA_ZWJ in text or DECOMPOSED_KHANDA_TA_ZWNJ in text:
        return False
    return text == canonicalize_unicode(text)

def canonicalize_unicode(text: str) -> str:
    """
    Canonicalizes Bengali Unicode text:
    1. Normalizes general text via NFC.
    2. Replaces decomposed nukta sequences with their precomposed atomic Bengali graphemes (য়, ড়, ঢ়).
    3. Replaces decomposed Khanda-Ta (both ZWJ and ZWNJ ligatures) with atomic U+09CE (ৎ).
    4. Cleans orphaned or rogue ZWJ/ZWNJ.
    """
    if not text:
        return ""

    # General NFC pass
    text = unicodedata.normalize("NFC", text)

    # Convert decomposed nukta sequences to canonical atomic codepoints
    text = text.replace(DECOMPOSED_YO, CHAR_YO)
    text = text.replace(DECOMPOSED_RRA, CHAR_RRA)
    text = text.replace(DECOMPOSED_RHHA, CHAR_RHHA)
    text = text.replace(DECOMPOSED_KHANDA_TA_ZWJ, CHAR_KHANDA_TA)
    text = text.replace(DECOMPOSED_KHANDA_TA_ZWNJ, CHAR_KHANDA_TA)

    # Clean stray ZWJ/ZWNJ:
    # Remove isolated ZWJ/ZWNJ not between Bengali characters
    text = re.sub(r"(?<![\u0980-\u09FF])[" + ZWJ + ZWNJ + r"]+", "", text)
    text = re.sub(r"[" + ZWJ + ZWNJ + r"]+(?![\u0980-\u09FF])", "", text)
    # Remove ZWJ if not preceded by virama (্)
    text = re.sub(r"(?<!" + VIRAMA + r")" + ZWJ, "", text)

    return text
