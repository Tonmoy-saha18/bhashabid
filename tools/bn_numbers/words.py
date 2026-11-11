# Exact Bengali words for 0-99 and large numbers
from dataclasses import dataclass

@dataclass
class StyleProfile:
    hundred_style: str = "শত"  # Options: "শত", "শো", "শ"
    lakh_style: str = "লাখ"     # Options: "লাখ", "লক্ষ"
    twenty_style: str = "বিশ"   # Options: "বিশ", "কুড়ি"
    negative_prefix: str = "মাইনাস" # Options: "মাইনাস", "ঋণাত্মক"

    def __post_init__(self):
        from ..bn_normalize.unicode import canonicalize_unicode
        self.hundred_style = canonicalize_unicode(self.hundred_style)
        self.lakh_style = canonicalize_unicode(self.lakh_style)
        self.twenty_style = canonicalize_unicode(self.twenty_style)
        self.negative_prefix = canonicalize_unicode(self.negative_prefix)

# Canonical 0-99 table as defined by Bangla Academy standard orthography
BASE_0_TO_99 = {
    0: "শূন্য", 1: "এক", 2: "দুই", 3: "তিন", 4: "চার", 5: "পাঁচ",
    6: "ছয়", 7: "সাত", 8: "আট", 9: "নয়", 10: "দশ",
    11: "এগারো", 12: "বারো", 13: "তেরো", 14: "চৌদ্দ", 15: "পনেরো",
    16: "ষোলো", 17: "সতেরো", 18: "আঠারো", 19: "উনিশ", 20: "বিশ",
    21: "একুশ", 22: "বাইশ", 23: "তেইশ", 24: "চব্বিশ", 25: "পঁচিশ",
    26: "ছাব্বিশ", 27: "সাতাশ", 28: "আঠাশ", 29: "ঊনত্রিশ", 30: "ত্রিশ",
    31: "একত্রিশ", 32: "বত্রিশ", 33: "তেত্রিশ", 34: "চৌত্রিশ", 35: "পঁয়ত্রিশ",
    36: "ছত্রিশ", 37: "সাঁইত্রিশ", 38: "আটত্রিশ", 39: "ঊনচল্লিশ", 40: "চল্লিশ",
    41: "একচল্লিশ", 42: "বিয়াল্লিশ", 43: "তেতাল্লিশ", 44: "চুয়াল্লিশ", 45: "পঁয়তাল্লিশ",
    46: "ছেচল্লিশ", 47: "সাতচল্লিশ", 48: "আটচল্লিশ", 49: "ঊনপঞ্চাশ", 50: "পঞ্চাশ",
    51: "একান্ন", 52: "বায়ান্ন", 53: "তিপ্পান্ন", 54: "চুয়ান্ন", 55: "পঞ্চান্ন",
    56: "ছাপ্পান্ন", 57: "সাতান্ন", 58: "আটান্ন", 59: "ঊনষাট", 60: "ষাট",
    61: "একষট্টি", 62: "বাষট্টি", 63: "তেষট্টি", 64: "চৌষট্টি", 65: "পঁয়ষট্টি",
    66: "ছেষট্টি", 67: "সাতষট্টি", 68: "আটষট্টি", 69: "ঊনসত্তর", 70: "সত্তর",
    71: "একাত্তর", 72: "বাহাত্তর", 73: "তিয়াত্তর", 74: "চুয়াত্তর", 75: "পঁচাত্তর",
    76: "ছিয়াত্তর", 77: "সাতাত্তর", 78: "আটাত্তর", 79: "ঊনআশি", 80: "আশি",
    81: "একাশি", 82: "বিরাশি", 83: "তিরাশি", 84: "চুরাশি", 85: "পঁচাশি",
    86: "ছিয়াশি", 87: "সাতাশি", 88: "আটাশি", 89: "ঊননব্বই", 90: "নব্বই",
    91: "একানব্বই", 92: "বিরানব্বই", 93: "তিরানব্বই", 94: "চুরানব্বই", 95: "পঁচানব্বই",
    96: "ছিয়ানব্বই", 97: "সাতানব্বই", 98: "আটানব্বই", 99: "নিরানব্বই"
}

def number_to_bangla_words(n: int, profile: StyleProfile | None = None) -> str:
    """
    Convert an integer to Bengali words with support for arbitrary size,
    recursive crore compounding, and customizable style profiles.
    """
    if profile is None:
        profile = StyleProfile()
        
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
        
    if n < 0:
        return f"{profile.negative_prefix} {number_to_bangla_words(-n, profile)}"
        
    if n == 0:
        return BASE_0_TO_99[0]
        
    if n == 20 and profile.twenty_style == "কুড়ি":
        return "কুড়ি"
        
    if n < 100:
        return BASE_0_TO_99[n]
        
    parts = []
    
    # 1. Crores (কোটি) >= 10,000,000 (10^7)
    crores = n // 10000000
    remainder = n % 10000000
    
    if crores > 0:
        # Recursive conversion for crores
        parts.append(f"{number_to_bangla_words(crores, profile)} কোটি")
        
    # 2. Lakhs (লাখ / লক্ষ) >= 100,000
    lakhs = remainder // 100000
    remainder = remainder % 100000
    if lakhs > 0:
        parts.append(f"{BASE_0_TO_99[lakhs]} {profile.lakh_style}")
        
    # 3. Thousands (হাজার) >= 1,000
    thousands = remainder // 1000
    remainder = remainder % 1000
    if thousands > 0:
        parts.append(f"{BASE_0_TO_99[thousands]} হাজার")
        
    # 4. Hundreds (শত / শো) >= 100
    hundreds = remainder // 100
    remainder = remainder % 100
    if hundreds > 0:
        parts.append(f"{BASE_0_TO_99[hundreds]} {profile.hundred_style}")
        
    # 5. Remaining 1-99
    if remainder > 0:
        if remainder == 20 and profile.twenty_style == "কুড়ি":
            parts.append("কুড়ি")
        else:
            parts.append(BASE_0_TO_99[remainder])
            
    return " ".join(parts)
