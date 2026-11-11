# Decimal number conversion (digit-by-digit)
from .words import number_to_bangla_words, BASE_0_TO_99, StyleProfile
from .digits import to_ascii_digits

def decimal_to_bangla_words(val: float | str, profile: StyleProfile | None = None) -> str:
    """
    Converts a floating point number or decimal string into Bengali words.
    Example: 3.14 -> "তিন দশমিক এক চার"
    """
    if profile is None:
        profile = StyleProfile()
        
    s = to_ascii_digits(str(val).strip())
    if "." not in s:
        return number_to_bangla_words(int(s), profile)
        
    integer_part_str, fractional_part_str = s.split(".", 1)
    
    integer_part = int(integer_part_str) if integer_part_str else 0
    integer_words = number_to_bangla_words(integer_part, profile)
    
    # Read decimal portion digit by digit
    frac_words = [BASE_0_TO_99[int(d)] for d in fractional_part_str if d.isdigit()]
    
    if not frac_words:
        return integer_words
        
    return f"{integer_words} দশমিক {' '.join(frac_words)}"
