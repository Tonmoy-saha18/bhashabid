# memory/lessons/LES-001_bengali_unicode_and_regex.md
# Lesson LES-001: Bengali Unicode Invariants & Python Regex Pitfalls

## 1. Context & Mistake References
- Linked Mistakes: `MST-0002`, `MST-0003`
- Linked Requirements: `REQ-016`, `REQ-017`, `REQ-018`
- Relevant Tools: `tools/bn_normalize/unicode.py`, `tools/bn_normalize/orthography.py`

## 2. Key Linguistic & Technical Findings
1. **Python `re` Word Boundary (`\\b`) Failure on Indic Matras**:
   In Python's standard `re` module, word character class `\\w` matches `[\\p{L}\\p{N}_]`, but does NOT match combining vowel diacritics (matras such as `ি`, `ী`, `ু`, `ূ`, `ে`, `ৈ`, `ো`, `ৌ`, which have Unicode category `Mn` or `Mc`). As a result, a word like `পাখী` is treated as two disjoint word tokens (`প` and `খ`) separated by non-word characters (`া` and `ী`). Therefore, `\\bপাখী\\b` fails to match.
   *Invariant Rule*: Never use standard ASCII `\\b` for Bengali text matching without combining mark support. Use explicit stem replacements, lookarounds, or whitespace tokenization.

2. **Decomposed Nukta Persistence**:
   Standard keyboard entry (including Windows Bijoy and Avro) often generates decomposed characters (`য + ়` = `\\u09af\\u09bc`, `ড + ়` = `\\u09a1\\u09bc`). Furthermore, standard Unicode NFC decomposition rules place nukta characters in the Composition Exclusion Table, so standard `unicodedata.normalize('NFC', text)` will not compose them into atomic graphemes.
   *Invariant Rule*: Always run `canonicalize_unicode` to enforce precomposed atomic single characters (`\\u09df`, `\\u09dc`, `\\u09dd`, `\\u09ce`) before equality assertions or dictionary lookups.
