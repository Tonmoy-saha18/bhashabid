from dataclasses import dataclass

@dataclass
class DialectProfile:
    name: str
    description: str
    hundred_style: str
    lakh_style: str
    twenty_style: str
    enforce_strict_short_vowels: bool
    permit_traditional_variants: bool

BD_STANDARD = DialectProfile(
    name="bd_standard",
    description="Bangladesh Standard (Bangla Academy, Dhaka) - strict short-vowels in non-tatsama, loanword স/স্ট",
    hundred_style="শত",
    lakh_style="লাখ",
    twenty_style="বিশ",
    enforce_strict_short_vowels=True,
    permit_traditional_variants=False
)

WB_STANDARD = DialectProfile(
    name="wb_standard",
    description="West Bengal Standard (Paschimbanga Bangla Akademi, Kolkata) - traditional variants permitted, শো/লক্ষ/কুড়ি",
    hundred_style="শো",
    lakh_style="লক্ষ",
    twenty_style="কুড়ি",
    enforce_strict_short_vowels=False,
    permit_traditional_variants=True
)

PROFILES = {
    "bd_standard": BD_STANDARD,
    "wb_standard": WB_STANDARD
}

def get_profile(name_or_profile: str | DialectProfile | None) -> DialectProfile:
    if isinstance(name_or_profile, DialectProfile):
        return name_or_profile
    if name_or_profile in PROFILES:
        return PROFILES[name_or_profile]
    return BD_STANDARD
