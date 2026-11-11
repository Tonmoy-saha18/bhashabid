# Feature Specification: FEAT-001 (Unicode Normalization, Orthography & Core Skill Layer)

## 1. Overview
FEAT-001 implements the core deterministic normalizer `bn_normalize` (REQ-016 through REQ-025), foundational linguistic knowledge cards (REQ-026 through REQ-030), and the progressive skill router `skills/bangla-expert/SKILL.md` (REQ-036).

## 2. Requirements Addressed
- **REQ-016**: Unicode NFC Normalization.
- **REQ-017**: Canonicalization of composite য় (U+09AF + U+09BC -> U+09DF).
- **REQ-018**: Canonicalization of composite ড় (U+09DC) and ঢ় (U+09DD).
- **REQ-019**: ZWJ / ZWNJ sanitization preserving standard conjuncts (য-ফলা, র-ফলা).
- **REQ-020**: Dari (`।`, U+0964) punctuation normalization replacing sentence-ending ASCII periods.
- **REQ-021**: Bangla Academy foreign loanword /s/ orthography (স vs ষ).
- **REQ-022**: Tatbhava / Desi short vowel normalization (হ্রস্ব-ই, হ্রস্ব-উ).
- **REQ-023**: Preservation of Khanda-ta (`ৎ`, U+09CE).
- **REQ-024**: Whitespace compaction without newline distortion.
- **REQ-025**: Bengali quotation mark canonicalization.
- **REQ-026 - REQ-030**: Sadhu/Cholito separation and honorific agreement rules.
- **REQ-036**: Skill file token budget (< 600 tokens).

## 3. Interfaces & Contracts
`bn_normalize.normalize(text: str, profile: str = "bd_standard", fix_punctuation: bool = True) -> str`
`bn_normalize.clean_unicode(text: str) -> str`
`bn_normalize.is_nfc_normalized(text: str) -> bool`
