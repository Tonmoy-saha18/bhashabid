# Bengali date formatting and day ordinals
from .digits import to_bangla_digits

# Day suffixes according to traditional Bengali practice
# ১লা, ২রা, ৩রা, ৪ঠা, ৫ই ... ১৮ই, ১৯শে ... ৩১শে
DATE_ORDINALS = {
    1: "১লা", 2: "২রা", 3: "৩রা", 4: "৪ঠা",
    5: "৫ই", 6: "৬ই", 7: "৭ই", 8: "৮ই", 9: "৯ই", 10: "১০ই",
    11: "১১ই", 12: "১২ই", 13: "১৩ই", 14: "১৪ই", 15: "১৫ই",
    16: "১৬ই", 17: "১৭ই", 18: "১৮ই",
    19: "১৯শে", 20: "২০শে", 21: "২১শে", 22: "২২শে", 23: "২৩শে",
    24: "২৪শে", 25: "২৫শে", 26: "২৬শে", 27: "২৭শে", 28: "২৮শে",
    29: "২৯শে", 30: "৩০শে", 31: "৩১শে"
}

GREGORIAN_MONTHS_BN = [
    "", "জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন",
    "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"
]

def format_date_bangla(year: int, month: int, day: int) -> str:
    """
    Format a Gregorian date with Bengali month name, date suffix, and Bengali year digits.
    Example: (2026, 3, 26) -> "২৬শে মার্চ, ২০২৬"
    """
    day_str = DATE_ORDINALS.get(day, f"{to_bangla_digits(day)}ই")
    month_str = GREGORIAN_MONTHS_BN[month] if 1 <= month <= 12 else str(month)
    year_str = to_bangla_digits(year)
    return f"{day_str} {month_str}, {year_str}"
