# Bengali Punctuation Normalization
import re

DARI = "\u0964"  # । (Bengali Dari)
DOUBLE_DARI = "\u0965" # ॥ (Bengali Double Dari)

# Regex to safely protect URLs, web domains, and email addresses from Dari conversion
URL_OR_EMAIL_PATTERN = re.compile(
    r"(?:https?://[^\s।]+|ftp://[^\s।]+|www\.[^\s।]+|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)"
)

def normalize_punctuation(text: str, convert_period_to_dari: bool = True) -> str:
    """
    Normalizes punctuation in Bengali text:
    1. Converts ASCII sentence-ending period (.) to Bengali Dari (।) while strictly preserving:
       - Decimals (e.g. 3.14 or ৩.১৪)
       - Web URLs (e.g. https://www.tbsnews.net)
       - Email addresses (e.g. info@bangladesh.gov.bd)
       - Alphanumeric domain names and abbreviations (e.g. e.g., i.e., test.com)
    2. Collapses repeated consecutive Dari characters (।। -> ।).
    3. Standardizes quotation marks to typographical curved quotes.
    4. Cleans spaces before sentence terminators.
    """
    if not text:
        return ""

    # Collapse multiple consecutive Daris
    text = re.sub(r"[\u0964]{2,}", DARI, text)

    # Protect URLs and email addresses using temporary token masking
    masked_items = []
    def _mask_url_or_email(match):
        raw = match.group(0)
        trailing_period = ""
        # If URL ends with a sentence-terminating dot (e.g. 'visit site.com.'), don't swallow the dot
        if raw.endswith("."):
            raw = raw[:-1]
            trailing_period = "."
        idx = len(masked_items)
        masked_items.append(raw)
        return f"__BHASHABID_URL_MASK_{idx}__{trailing_period}"

    text = URL_OR_EMAIL_PATTERN.sub(_mask_url_or_email, text)

    if convert_period_to_dari:
        # 1. Do not convert if followed by ASCII/Bengali digit (decimals like 3.14, ৩.১৪)
        # 2. Do not convert if between ASCII alphanumeric characters (like site.com, node.js, e.g.)
        # 3. Only convert when preceded by Bengali word or at true sentence terminator
        def _replace_period(m):
            span_start = m.start()
            span_end = m.end()
            # Lookahead check for decimal
            after_char = text[span_end:span_end+1]
            if after_char and (after_char.isdigit() or "\u09E6" <= after_char <= "\u09EF"):
                return "."
            # Lookbehind and lookahead for ASCII domain/abbr (e.g. name.ext)
            before_char = text[span_start-1:span_start] if span_start > 0 else ""
            if before_char and after_char and before_char.isalnum() and after_char.isalpha():
                return "."
            return DARI

        text = re.sub(r"\.", _replace_period, text)

    # Restore protected URLs and email addresses
    for idx, original in enumerate(masked_items):
        text = text.replace(f"__BHASHABID_URL_MASK_{idx}__", original)

    # Clean space before sentence ending marks
    text = re.sub(r"\s+([\u0964!?,;:])", r"\1", text)

    # Standardize ASCII quotes to curved Bengali quotes
    # Opening double quote
    text = re.sub(r'(^|\s)"([\u0980-\u09FF])', r'\1“\2', text)
    # Closing double quote
    text = re.sub(r'([\u0980-\u09FF])"($|\s|[\u0964!?,])', r'\1”\2', text)

    return text
