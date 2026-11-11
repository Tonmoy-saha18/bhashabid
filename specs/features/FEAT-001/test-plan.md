# Test Plan: FEAT-001

## 1. Unit Tests (`eval/unit/test_bn_normalize.py`)
- Unicode NFC canonicalization test across all Bengali vowels, consonants, and matras.
- Decomposition resolution: `য + ়` (U+09AF, U+09BC) -> `য়` (U+09DF).
- Decomposition resolution: `ড + ়` -> `ড়` (U+09DC) and `ঢ + ়` -> `ঢ়` (U+09DD).
- Inappropriate ZWJ/ZWNJ removal while ensuring `য-ফলা` and `র-ফলা` remain structurally valid.
- Dari conversion: Replace trailing ASCII `.` with `।` without corrupting decimal numbers (e.g. `৩.১৪`).
- Whitespace compaction without line-break deletion.

## 2. Card Validation Tests (`eval/unit/test_knowledge_cards.py`)
- Validate every card in `knowledge/cards/*.yaml` against `docs/KNOWLEDGE_CARD_SCHEMA.md`.
- Verify no card has empty citations or unverified `reviewed` status.

## 3. Skill Budget Tests (`eval/unit/test_skill.py`)
- Approximate token count check of `skills/bangla-expert/SKILL.md` strictly < 600 tokens.
- Verify referenced files in `references/` exist and are readable.
