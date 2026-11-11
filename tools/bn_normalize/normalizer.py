# Unified Bengali Normalizer Interface
import re
from .unicode import canonicalize_unicode
from .punctuation import normalize_punctuation
from .orthography import normalize_orthography

def clean_whitespace(text: str) -> str:
    """
    Collapses multiple horizontal spaces into a single space,
    trims leading/trailing whitespace per line, while preserving newlines.
    """
    if not text:
        return ""
    lines = text.splitlines()
    cleaned_lines = [re.sub(r"[\t ]+", " ", line).strip() for line in lines]
    return "\n".join(cleaned_lines)

def normalize(
    text: str,
    profile: str = "bd_standard",
    fix_punctuation: bool = True,
    normalize_loanwords: bool = True,
    clean_spaces: bool = True
) -> str:
    """
    Master pipeline for Bengali text normalization.
    Performs:
    1. Unicode NFC & decomposed nukta canonicalization.
    2. Bangla Academy orthography normalization (if requested).
    3. Punctuation standardization (Dari replacement & quote curving).
    4. Whitespace compaction.
    """
    if not text:
        return ""

    # 1. Unicode Canonicalization
    text = canonicalize_unicode(text)

    # 2. Orthography Normalization
    if normalize_loanwords:
        text = normalize_orthography(text, profile=profile)

    # 3. Punctuation
    if fix_punctuation:
        text = normalize_punctuation(text)

    # 4. Whitespace
    if clean_spaces:
        text = clean_whitespace(text)

    return text

# Alias
normalize_text = normalize
