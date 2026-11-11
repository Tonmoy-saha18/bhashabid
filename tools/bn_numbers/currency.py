# Currency formatting in Bengali (টাকা এবং পয়সা)
from .words import number_to_bangla_words, StyleProfile

def format_currency_words(amount: float | int, profile: StyleProfile | None = None) -> str:
    """
    Format monetary amounts in Bengali words.
    Example: 50.25 -> "পঞ্চাশ টাকা পঁচিশ পয়সা"
             100   -> "একশত টাকা"
             0.50  -> "পঞ্চাশ পয়সা"
    """
    if profile is None:
        profile = StyleProfile()
        
    taka = int(amount)
    paisa = round((amount - taka) * 100)
    
    parts = []
    if taka > 0:
        parts.append(f"{number_to_bangla_words(taka, profile)} টাকা")
    if paisa > 0:
        parts.append(f"{number_to_bangla_words(paisa, profile)} পয়সা")
        
    if not parts:
        return "শূন্য টাকা"
        
    return " ".join(parts)
