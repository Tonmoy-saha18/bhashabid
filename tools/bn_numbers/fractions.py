# Fractions (সোয়া, দেড়, আড়াই, সাড়ে, পৌনে, আধ)
from .words import number_to_bangla_words, StyleProfile

def fraction_to_bangla_words(val: float, profile: StyleProfile | None = None) -> str:
    """
    Convert common fractional values to idiomatic Bengali fraction words,
    supporting negative values and numbers >= 100 without ASCII leaks.
    Examples:
      0.25   -> "এক-চতুর্থাংশ"
      0.5    -> "অর্ধেক"
      -0.5   -> "মাইনাস অর্ধেক"
      0.75   -> "পৌনে এক"
      1.25   -> "সোয়া এক"
      1.5    -> "দেড়"
      -1.5   -> "মাইনাস দেড়"
      2.5    -> "আড়াই"
      -2.5   -> "মাইনাস আড়াই"
      3.5    -> "সাড়ে তিন"
      101.5  -> "সাড়ে এক শত এক"
      100.75 -> "পৌনে এক শত এক"
    """
    if profile is None:
        profile = StyleProfile()

    val = round(val, 4)
    is_neg = (val < 0)
    abs_val = abs(val)
    whole = int(abs_val)
    frac = round(abs_val - whole, 4)

    def _get_word(n: int) -> str:
        return number_to_bangla_words(n, profile)

    # Simple proper fractions (whole == 0)
    if whole == 0:
        if frac == 0.25:
            res = "এক-চতুর্থাংশ"
        elif frac == 0.5:
            res = "অর্ধেক"
        elif frac == 0.75:
            res = "পৌনে এক"
        else:
            from .decimals import decimal_to_bangla_words
            return decimal_to_bangla_words(val, profile)
        return f"{profile.negative_prefix} {res}" if is_neg else res

    # Mixed fractions
    if frac == 0.0:
        res = _get_word(whole)
    elif frac == 0.25:
        res = f"সোয়া {_get_word(whole)}"
    elif frac == 0.5:
        if whole == 1:
            res = "দেড়"
        elif whole == 2:
            res = "আড়াই"
        else:
            res = f"সাড়ে {_get_word(whole)}"
    elif frac == 0.75:
        res = f"পৌনে {_get_word(whole + 1)}"
    else:
        from .decimals import decimal_to_bangla_words
        return decimal_to_bangla_words(val, profile)

    return f"{profile.negative_prefix} {res}" if is_neg else res
