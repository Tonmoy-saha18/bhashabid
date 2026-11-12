# Decimal number conversion (digit-by-digit)
from .words import number_to_bangla_words, BASE_0_TO_99, StyleProfile
from .digits import to_ascii_digits

def decimal_to_bangla_words(val: float | str, profile: StyleProfile | None = None) -> str:
    """
    Converts a floating point number or decimal string into Bengali words,
    with strict preservation of negative signs for values like -0.75.
    Example: 3.14  -> "তিন দশমিক এক চার"
             -0.75 -> "মাইনাস শূন্য দশমিক সাত পাঁচ"
    """
    if profile is None:
        profile = StyleProfile()

    s = to_ascii_digits(str(val).strip())
    is_negative = s.startswith("-")
    if is_negative:
        s = s[1:].strip()

    if "." not in s:
        res = number_to_bangla_words(int(s) if s else 0, profile)
        return f"{profile.negative_prefix} {res}" if is_negative and res != "শূন্য" else res

    integer_part_str, fractional_part_str = s.split(".", 1)

    integer_part = int(integer_part_str) if integer_part_str else 0
    integer_words = number_to_bangla_words(integer_part, profile)

    # Read decimal portion digit by digit
    frac_words = [BASE_0_TO_99[int(d)] for d in fractional_part_str if d.isdigit()]

    if not frac_words:
        res = integer_words
    else:
        res = f"{integer_words} দশমিক {' '.join(frac_words)}"

    if is_negative:
        return f"{profile.negative_prefix} {res}"
    return res
