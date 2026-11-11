# Bhashabid Architecture Specification (ARCHITECTURE.md)

## 1. System Philosophy & Layering
Bhashabid operates as a modular, external capability layer designed for any LLM or AI agent runtime. It consists of four distinct tiers:

```
+-------------------------------------------------------------------+
|                        Agent Runtime                              |
|           (Claude, Gemini, GPT-4, Cursor, Open-Source)            |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| 1. Progressive Skill Layer (skills/bangla-expert/SKILL.md)        |
|    - Compact Router (<600 tokens)                                 |
|    - Dynamic References (grammar, idioms, orthography, registers) |
+-------------------------------------------------------------------+
          |                                                 |
          v                                                 v
+-------------------------------+       +---------------------------+
| 2. Deterministic Tools Engine |       | 3. Linguistic Knowledge   |
|    (tools/bn_numbers,         |       |    Base (knowledge/cards/)|
|     tools/bn_normalize,       |       |    - Atomic YAML cards    |
|     tools/bn_lint)            |       |    - Dialect & Register   |
|    - High performance Python  |       |    - Anti-Pattern guides  |
+-------------------------------+       +---------------------------+
          \                                                 /
           +----------------------+------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| 4. Self-Correcting Feedback Loop & Memory Engine                  |
|    - Mistake Ledger (memory/mistakes/ledger.jsonl)                |
|    - Automated Regression Test Generator (eval/unit/)             |
|    - Multi-Model Evaluation Matrix & Holdouts (eval/benchmarks/)   |
+-------------------------------------------------------------------+
```

## 2. Core Components

### 2.1 Deterministic Toolset (`tools/`)
Rules that can be computed algorithmically are never offloaded to probabilistic model generation:
- `bn_numbers`: Converts between digits and words (0-99 irregular forms, lakh/crore grouping, decimals, ordinals, currency, fractions, dates).
- `bn_normalize`: NFC Unicode canonicalization, punctuation standardization (Dari), sanitizing ZWJ/ZWNJ, and Bengali Academy loanword orthography.
- `bn_lint`: Static analysis linter checking for Sadhu-Cholito mixing (গুরুচণ্ডালী দোষ), honorific clashes, and common calques.
- `mcp_server`: Standard Model Context Protocol (MCP) server exposing tools to compatible agents.

### 2.2 Knowledge Base (`knowledge/`)
Atomic, schema-validated YAML cards (`knowledge/cards/*.yaml`) capturing linguistic subtleties:
- Grammatical rules and exceptions
- Collocations, proverbs, and cultural metaphors
- False friends and English-Bengali translation pitfalls
- Dialectal profiles: Bangladesh Standard (Bangla Academy) vs West Bengal.

### 2.3 Progressive Skill Architecture (`skills/bangla-expert/`)
To preserve prompt context windows, `SKILL.md` is strictly minimized (<600 tokens). It acts as a routing controller pointing to specialized markdown files in `skills/bangla-expert/references/`:
- `numerals.md`
- `honorifics.md`
- `sadhu_cholito.md`
- `orthography.md`
- `translation_idioms.md`

### 2.4 Mistake-Driven Memory & Regression Loop
When an evaluation failure or real-task defect occurs:
1. `A13 Mistake Analyst` logs the failure in `memory/mistakes/ledger.jsonl`.
2. A reproducing test case is added to `eval/unit/test_regression_ledger.py`.
3. `A6 Developer` or `A9 Knowledge Distiller` implements the fix.
4. The regression suite verifies resolution prior to closing the ledger item.
