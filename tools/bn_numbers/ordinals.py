# Classical and calendar ordinals
from .dates import DATE_ORDINALS
from .digits import to_bangla_digits

CLASSICAL_ORDINALS = {
    1: "প্রথম", 2: "দ্বিতীয়", 3: "তৃতীয়", 4: "চতুর্থ", 5: "পঞ্চম",
    6: "ষষ্ঠ", 7: "সপ্তম", 8: "অষ্টম", 9: "নবম", 10: "দশম",
    11: "একাদশ", 12: "দ্বাদশ", 13: "ত্রয়োদশ", 14: "চতুর্দশ", 15: "পঞ্চদশ",
    16: "ষোড়শ", 17: "সপ্তদশ", 18: "অষ্টাদশ", 19: "ঊনবিংশ", 20: "বিংশ",
    21: "একবিংশ", 22: "দ্বাবিংশ", 23: "ত্রয়োবিংশ", 24: "চতুর্বিংশ", 25: "পঞ্চবিংশ",
    30: "ত্রিংশ", 40: "চত্বারিংশ", 50: "পঞ্চাশত্তম", 100: "শততম"
}

def to_classical_ordinal(n: int) -> str:
    """Return classical Sanskrit-derived ordinal in Bengali (e.g. 1 -> প্রথম, 35 -> ৩৫-তম)."""
    if n in CLASSICAL_ORDINALS:
        return CLASSICAL_ORDINALS[n]
    return f"{to_bangla_digits(n)}-তম"

def to_date_ordinal(day: int) -> str:
    """Return calendar date ordinal (e.g. 1 -> ১লা, 21 -> ২১শে, 32 -> ৩২ই)."""
    if day in DATE_ORDINALS:
        return DATE_ORDINALS[day]
    return f"{to_bangla_digits(day)}ই"
