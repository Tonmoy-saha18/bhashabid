# Fractions (সোয়া, দেড়, আড়াই, সাড়ে, পৌনে, আধ)
from .words import BASE_0_TO_99

def fraction_to_bangla_words(val: float) -> str:
    """
    Convert common fractional values to idiomatic Bengali fraction words.
    Examples:
      0.25 -> "এক-চতুর্থাংশ"
      0.5  -> "অর্ধেক"
      0.75 -> "পৌনে এক"
      1.25 -> "সোয়া এক"
      1.5  -> "দেড়"
      1.75 -> "পৌনে দুই"
      2.25 -> "সোয়া দুই"
      2.5  -> "আড়াই"
      2.75 -> "পৌনে তিন"
      3.5  -> "সাড়ে তিন"
      4.75 -> "পৌনে পাঁচ"
    """
    val = round(val, 4)
    whole = int(val)
    frac = round(val - whole, 4)
    
    # Simple proper fractions
    if whole == 0:
        if frac == 0.25:
            return "এক-চতুর্থাংশ"
        elif frac == 0.5:
            return "অর্ধেক"
        elif frac == 0.75:
            return "পৌনে এক"
            
    # Mixed fractions
    if frac == 0.0:
        return BASE_0_TO_99.get(whole, str(whole))
        
    if frac == 0.25:
        # সোয়া + whole
        whole_word = BASE_0_TO_99.get(whole, str(whole))
        return f"সোয়া {whole_word}"
        
    if frac == 0.5:
        if whole == 1:
            return "দেড়"
        elif whole == 2:
            return "আড়াই"
        else:
            whole_word = BASE_0_TO_99.get(whole, str(whole))
            return f"সাড়ে {whole_word}"
            
    if frac == 0.75:
        # পৌনে + (whole + 1)
        next_word = BASE_0_TO_99.get(whole + 1, str(whole + 1))
        return f"পৌনে {next_word}"
        
    # Default fallback to decimal
    from .decimals import decimal_to_bangla_words
    return decimal_to_bangla_words(val)
