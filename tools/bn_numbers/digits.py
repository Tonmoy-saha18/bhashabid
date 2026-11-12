# Digit mapping and South Asian lakh/crore comma grouping
ASCII_DIGITS = "0123456789"
BANGLA_DIGITS = "০১২৩৪৫৬৭৮৯"

ASCII_TO_BN_MAP = str.maketrans(ASCII_DIGITS, BANGLA_DIGITS)
BN_TO_ASCII_MAP = str.maketrans(BANGLA_DIGITS, ASCII_DIGITS)

def to_bangla_digits(val: str | int) -> str:
    """Convert ASCII digits to Bengali digits."""
    return str(val).translate(ASCII_TO_BN_MAP)

def to_ascii_digits(val: str) -> str:
    """Convert Bengali digits to ASCII digits."""
    return str(val).translate(BN_TO_ASCII_MAP)

def format_lakh_crore(val: int | str, to_bangla: bool = True) -> str:
    """
    Format an integer according to the South Asian numbering system (3, 2, 2 grouping).
    Example: 1234567 -> 12,34,567 or ১২,৩৪,৫৬৭
    """
    s = str(val).strip()
    if not s:
        return ""
    
    # Handle negative
    prefix = ""
    if s.startswith("-"):
        prefix = "-"
        s = s[1:]
    
    # Normalize to ascii digits first
    s = to_ascii_digits(s)
    
    # Handle decimal if present
    decimal_part = ""
    if "." in s:
        s, decimal_digits = s.split(".", 1)
        if decimal_digits and not decimal_digits.isdigit():
            raise ValueError(f"Invalid number string for grouping: {val}")
        decimal_part = "." + decimal_digits
        
    if not s.isdigit():
        raise ValueError(f"Invalid number string for grouping: {val}")
        
    if len(s) <= 3:
        formatted = s
    else:
        last_three = s[-3:]
        remaining = s[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted = ",".join(groups) + "," + last_three
        
    res = prefix + formatted + decimal_part
    return to_bangla_digits(res) if to_bangla else res
