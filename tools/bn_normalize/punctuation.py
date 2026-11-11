# Bengali Punctuation Normalization
import re

DARI = "\u0964"  # । (Bengali Dari)
DOUBLE_DARI = "\u0965" # ॥ (Bengali Double Dari)

def normalize_punctuation(text: str, convert_period_to_dari: bool = True) -> str:
    """
    Normalizes punctuation in Bengali text:
    1. Converts ASCII sentence-ending period (.) to Bengali Dari (।) while preserving decimals (e.g. 3.14 or ৩.১৪).
    2. Collapses repeated consecutive Dari characters (।। -> ।).
    3. Standardizes quotation marks to typographical curved quotes.
    4. Cleans spaces before sentence terminators.
    """
    if not text:
        return ""

    # Collapse multiple consecutive Daris
    text = re.sub(r"[\u0964]{2,}", DARI, text)

    if convert_period_to_dari:
        # Replace period with Dari when NOT immediately followed by a digit (preserving decimals like 3.14, ৩.১৪)
        pattern = r"\.(?![0-9\u09E6-\u09EF])"
        text = re.sub(pattern, DARI, text)

    # Clean space before sentence ending marks
    text = re.sub(r"\s+([\u0964!?,;:])", r"\1", text)

    # Standardize ASCII quotes to curved Bengali quotes
    # Opening double quote
    text = re.sub(r'(^|\s)"([\u0980-\u09FF])', r'\1“\2', text)
    # Closing double quote
    text = re.sub(r'([\u0980-\u09FF])"($|\s|[\u0964!?,])', r'\1”\2', text)

    return text
