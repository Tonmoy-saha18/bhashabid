# Bhashabid Constitution (00-constitution.md)

## Non-Negotiable Core Principles

### P1: Spec First
The `specs/` directory is the single source of truth. No code, knowledge card, tool, or skill rule may be written or modified without a corresponding Spec or Requirement ID. Any changes to specifications must strictly follow the Spec Change Protocol: propose diff + rationale -> Reviewer (A14) verification -> record in `specs/CHANGELOG.md` -> update `traceability.csv` -> execute implementation.

### P2: Provenance & Attribution
Every knowledge card must specify documented sources, verified positive/negative examples, a "common LLM error" analysis, and a confidence tier:
`llm-hypothesis` -> `data-supported` -> `reviewed`.
Only human native-speaker reviewers may assign or promote a card to `reviewed`. Autonomous agents may never self-promote or claim unverified human endorsement.

### P3: License-Gated Data
Only public-domain, openly licensed, or explicitly approved sources from `memory/sources/` and `DATA_LICENSES.md` are permitted. Autonomous scrapers must respect `robots.txt` and terms of service. Raw copyrighted works (books, news archives) must never be stored in bulk; only derived statistics, structural patterns, and minimal illustrative phrases are stored.

### P4: Tools for Rules, Knowledge for Judgment
Deterministic linguistic operations must be implemented as deterministic software with 100% test coverage:
- Digit to Bengali word conversion (0-99 irregular patterns)
- South Asian number grouping (১২,৩৪,৫৬৭)
- Digit-by-digit decimal readout
- Ordinals and fractions (সোয়া, দেড়, আড়াই, সাড়ে, পৌনে)
- Currency formatting (টাকা/পয়সা)
- Bengali / Gregorian calendar calculations
- Unicode NFC normalization, ZWJ/ZWNJ sanitization, and Dari (।) punctuation.
Accept valid regional variants via explicit profile configuration (e.g. পাঁচশ vs পাঁচশো vs পাঁচশত), never via random guesswork.

### P5: Parameterized Profiles and Registers
Linguistic registers and geographic standards are explicit parameters:
- **Standards**: Bangladesh Standard (Bangla Academy) vs West Bengal (Paschimbanga Bangla Akademi).
- **Styles**: Cholito (চলিত) vs Sadhu (সাধু).
- **Honorific Registers**: তুই (intimate/inferior), তুমি (familiar/equal), আপনি (formal/polite).
- **Functional Domains**: News prose, academic writing, legal/formal, creative fiction, colloquial speech, poetry.

### P6: Token Efficiency via Progressive Disclosure
The agent skill layer must maintain an ultra-compact `SKILL.md` entry point (< 500 tokens). Detailed grammar rules, idiomatic mappings, and dictionary lookups must reside in modular reference guides loaded strictly on demand.

### P7: Evidence Over Confidence
No feature, card, or tool is deemed "ready" without empirical benchmark results comparing performance with-skill versus without-skill across at least three distinct model architectures.

### P8: Anti-Self-Deception
No model may act as the sole evaluator of its own output. Evaluations must utilize held-out test splits, cross-model jury judges, deterministic unit checks, and human native-speaker audits. A pristine hidden holdout split is permanently maintained and never exposed for training or prompt engineering.

---

## Autonomy Policy

| Scope | Permitted Actions |
|---|---|
| **AUTONOMOUS** (No approval needed) | Write/edit code and tests; run unit/benchmark suites; ingest pre-approved sources; draft cards (`llm-hypothesis`, `data-supported`); log mistakes in ledger; update memory; commit on feature branches. |
| **USER APPROVAL REQUIRED** (Pause and prompt) | Registering unverified sources; incurring external paid API expenses; modifying repository licenses; merging feature branches to `main`; tagging releases; deleting data; altering the core constitution. |
| **STRICTLY FORBIDDEN** | Promoting cards to `reviewed` autonomously; bypassing `robots.txt`; scraping paywalled material; fabricating benchmark numbers; ignoring `state/STOP`. |

## Operational Guardrails & Kill Switch
1. **Kill Switch**: If `state/STOP` exists, all processing loops terminate immediately.
2. **Cycle Cap**: Max 25 iterations per continuous run.
3. **Budget Cap**: Local sandbox default $0.00.
