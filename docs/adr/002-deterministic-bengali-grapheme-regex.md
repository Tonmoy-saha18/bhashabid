# ADR 002: Deterministic Bengali Token Boundaries Over ASCII Word Boundaries

## Status
Accepted (2026-11-11)

## Context
During Cycle 1 and Cycle 2 testing (`MST-0002`, `MST-0004`), standard regex word boundaries (`\b`) consistently failed on inflected Bengali words. In Python's built-in `re` engine, combining vowel diacritics (matras such as `ি`, `ী`, `ু`, `ো`) are categorized as `Mn`/`Mc` and are excluded from the `\w` character class. Consequently, words like `পাখী` or `করো` are seen as multiple disconnected tokens, making `\b` fail.

## Decision
We prohibit the use of unvarnished ASCII `\b` for Bengali text matching. All token boundaries must use explicit Unicode script range lookarounds:
`B_L = r"(?<![\u0980-\u09FF])"`
`B_R = r"(?![\u0980-\u09FF])"`

## Consequences
- Guaranteed 100% boundary matching across all inflected Bengali words, matras, and punctuation.
- Zero dependencies on external third-party regex C-extensions.
