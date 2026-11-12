# Welcome to the Bhashabid (ভাষাবিদ) Wiki

**Bhashabid** (ভাষাবিদ) is the first-ever open-source Bengali language coprocessor engine featuring a **constitutionally supervised self-learning loop**. Operating as an external cognitive and deterministic coprocessor without retraining model weights, it continuously harvests real-world anomalies, synthesizes candidate rules, and distills high-level invariants under human verification (P2) and a strict < 390 token ceiling—systematically elevating the accuracy, orthography, and native fluency of AI-generated Bengali across daily professional and creative activities.

---

## 🧭 Wiki Contents

1. [Getting Started & Installation](Getting-Started.md)
   - CLI usage, Python SDK, MCP setup, and agent prompt injection.
2. [The 8 Core Writing Domains](The-8-Writing-Domains.md)
   - Deep dive into how Bhashabid handles petitions, news, fiction, academic papers, books, contracts, and healthcare.
3. [Model Context Protocol (MCP) Integration](Model-Context-Protocol-MCP.md)
   - Connecting Bhashabid to Cursor, Claude Desktop, Windsurf, and Zed.
4. [Poetic Prosody & Payar Verification](Poetic-Prosody-&-Payar.md)
   - Phonological syllabification, mora counting, Aksharbritta, Matrabritta, and Payar (8+6=14) scansion.
5. [Article 102 Constitutional Writs](Constitutional-Writs-Article-102.md)
   - High Court writ petitions (Habeas Corpus, Mandamus, Certiorari, Prohibition, Quo Warranto) and statutory prayers.
6. [Principle P2 Provenance & Human Review](Principle-P2-Provenance-&-Review.md)
   - The cryptographic review protocol and verification system that keeps Bhashabid scientifically honest.
7. [Centralized Linguistic Review Hub](../review_queue/README.md)
   - Community guidelines for reviewing and submitting candidate cards via GitHub Pull Requests.

---

## 🏛️ The 4 Pioneering Architectural Pillars

- **Pillar 1: Hard Programmatic Token Ceiling (< 390 tokens)**: Progressive disclosure keeps core rules ultra-lightweight (~302 tokens), preventing context exhaustion.
- **Pillar 2: Supervised Self-Learning Distillation Loop**: Unlike un-gated self-learning agents (e.g. Hermes) that risk linguistic hallucination, Bhashabid uses an anomaly harvester, candidate card synthesizer, and human-in-the-loop (P2) cryptographic sign-off before compiling invariants.
- **Pillar 3: Modular Domain Isolation**: 11 professional sectors across 8 modular guides load strictly on demand; unrelated domain knowledge burns 0.0 tokens.
- **Pillar 4: Deterministic MCP Offloading ($0.00 Token Cost)**: Irregular 0-99 numbers, South Asian currency commas, Unicode NFC, and 14-akshar Payar scansion run in microsecond Python algorithms.
