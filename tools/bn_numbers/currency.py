# Currency formatting in Bengali (টাকা এবং পয়সা)
from .words import number_to_bangla_words, StyleProfile

def format_currency_words(amount: float | int | str, profile: StyleProfile | None = None) -> str:
    """
    Format monetary amounts in Bengali words with support for negative balances.
    Accepts float, int, or string amounts (with Bengali or ASCII digits).
    Example: 50.25  -> "পঞ্চাশ টাকা পঁচিশ পয়সা"
             -50.25 -> "মাইনাস পঞ্চাশ টাকা পঁচিশ পয়সা"
             100    -> "একশত টাকা"
             0.50   -> "পঞ্চাশ পয়সা"
             -0.50  -> "মাইনাস পঞ্চাশ পয়সা"
    """
    if profile is None:
        profile = StyleProfile()

    if isinstance(amount, str):
        from .digits import to_ascii_digits
        clean_str = to_ascii_digits(amount.strip().replace(",", ""))
        try:
            amount = float(clean_str)
        except ValueError:
            raise ValueError(f"Invalid monetary amount string: '{amount}'")

    is_negative = (amount < 0)
    abs_amount = abs(amount)

    taka = int(abs_amount)
    paisa = round((abs_amount - taka) * 100)
    if paisa >= 100:
        taka += 1
        paisa -= 100

    parts = []
    if taka > 0:
        parts.append(f"{number_to_bangla_words(taka, profile)} টাকা")
    if paisa > 0:
        parts.append(f"{number_to_bangla_words(paisa, profile)} পয়সা")

    if not parts:
        return "শূন্য টাকা"

    res = " ".join(parts)
    if is_negative:
        return f"{profile.negative_prefix} {res}"
    return res
