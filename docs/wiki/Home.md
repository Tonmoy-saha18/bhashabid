# Welcome to the Bhashabid (ভাষাবিদ) Wiki

**Bhashabid** is an open-source, spec-driven Bengali linguistic coprocessor, evaluation matrix, and progressive AI skill layer. It empowers any AI assistant, LLM, or software backend to write, translate, correct, and evaluate authentic Bengali prose like a skilled native writer.

---

## 🧭 Wiki Contents

1. [Getting Started & Installation](Getting-Started.md)
   - CLI usage, Python SDK, MCP setup, and agent prompt injection.
2. [The 8 Core Writing Domains](The-8-Writing-Domains.md)
   - Deep dive into how Bhashabid handles petitions, news, fiction, academic papers, books, contracts, and healthcare.
3. [Model Context Protocol (MCP) Integration](Model-Context-Protocol-(MCP).md)
   - Connecting Bhashabid to Cursor, Claude Desktop, Windsurf, and Zed.
4. [Poetic Prosody & Payar Verification](Poetic-Prosody-&-Payar.md)
   - Phonological syllabification, mora counting, Aksharbritta, Matrabritta, and Payar (8+6=14) scansion.
5. [Article 102 Constitutional Writs](Constitutional-Writs-(Article-102).md)
   - High Court writ petitions (Habeas Corpus, Mandamus, Certiorari, Prohibition, Quo Warranto) and statutory prayers.
6. [Principle P2 Provenance & Human Review](Principle-P2-Provenance-&-Review.md)
   - The cryptographic review protocol and verification system that keeps Bhashabid scientifically honest.

---

## 🏛️ Architectural Pillars

- **Deterministic Tools for Rules**: Grammatical, numerical, and phonological tasks are solved with deterministic algorithms with 100% test coverage.
- **Knowledge for Judgment**: Stylistic, literary, and domain-specific conventions are codified into atomic knowledge cards.
- **Progressive Skill Routing**: Agents load modular reference files only on demand, maintaining a core prompt size of < 390 tokens.
- **Permanent Mistake Memory**: Every trapped flaw is permanently sealed in `memory/mistakes/ledger.jsonl` and tested in `test_regression_ledger.py`.
