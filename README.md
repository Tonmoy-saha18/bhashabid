# Bhashabid (ভাষাবিদ) — Open-Source Bengali Linguistic Coprocessor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: >=3.10](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://python.org)
[![Version: v1.0.0](https://img.shields.io/badge/Version-v1.0.0-blue.svg)](https://github.com/ashik1291/bhashabid)
[![Tests: 59 Passing](https://img.shields.io/badge/Tests-59%20Passing-brightgreen.svg)](eval/unit)
[![Proven Knowledge: 23 Reviewed Cards](https://img.shields.io/badge/P2%20Provenance-23%2F23%20Cards%20Reviewed-blueviolet.svg)](knowledge/cards)

> **Bhashabid** (ভাষাবিদ - *"The Bengali Linguist"*) is a spec-driven, deterministic linguistic coprocessor, evaluation matrix, and progressive AI skill layer that enables **ANY** AI agent, LLM, or software pipeline to write, translate, correct, and evaluate authentic Bengali (বাংলা) like a skilled native writer.

---

## 🎯 The Core Problem It Solves

Frontier LLMs (ChatGPT, Claude, Gemini, DeepSeek) consistently deteriorate when generating or translating Bengali:
- **Catastrophic Calques**: English passives (*"দ্বারা চালিত"*, *"দ্বারা অনুষ্ঠিত"*), judicial errors (*"জিজ্ঞেস করে রুল"*), and greeting mistranslations (*"প্রিয় মহাশয়"*).
- **Broken Epistolary Hierarchy**: Treating revered teachers, bosses, friends, and juniors with generic pronoun/verb mismatches (*তুমি সিদ্ধান্ত নেন*).
- **Numeral Disasters**: Fabricating 2-digit numbers (*নব্বই নয়* instead of *নিরানব্বই*), wrong currency words, and Western 3-digit comma grouping.
- **Unscanned Poetry**: Line breaks masquerading as verse without syllabic metre (*মাত্রা/অক্ষরবৃত্ত/পয়ার*) or caesura (*যতি*).
- **Unicode Fragmentation**: Non-canonical nuktas (`য+়` vs `য়`, `ড+়` vs `ড়`), missing Daris (`।`), and broken ZWJ/ZWNJ forms.

**Bhashabid fixes all of this** through an external, deterministic, token-efficient architecture without retraining model weights.

---

## 🚀 6 Ways to Use Bhashabid Today

### 1. As an Antigravity, Claude, or Cursor Skill (1-Command Install with ALL References)
To install the skill along with **all 8 specialized reference guides** into your AI environment, run the built-in installer:
```bash
# Install to all detected environments (Antigravity, Claude, and Cursor)
bhashabid install-skill --target all

# Or install specifically:
bhashabid install-skill --target antigravity
bhashabid install-skill --target claude
bhashabid install-skill --target cursor
```
* **Token Footprint**: Strictly **< 390 tokens** (progressive disclosure routes to modular guides on demand).
* **Autonomous Lookup**: When handling legal writs, business news, petitions, or fiction, the agent automatically reads the appropriate reference guide without human intervention.

### 2. Universal All-In-One Prompt (ChatGPT, Claude Web, Gemini Web, DeepSeek)
For users who only have a web browser chat box and cannot install files, copy the single consolidated bundle:
👉 **[`skills/bangla-expert/STANDALONE_ALL_IN_ONE.md`](skills/bangla-expert/STANDALONE_ALL_IN_ONE.md)**

This file packages the core invariants plus the distilled rules for all 8 sectors into a single ready-to-paste prompt.

### 3. As an MCP Server (Cursor, Claude Desktop, Windsurf, Zed)
Exposes Bhashabid's deterministic tools via the **Model Context Protocol (MCP)**:
```bash
python -m tools.mcp_server
```
**Exposed Tools**:
* `convert_number`: Exact 0-99 cardinal lookup, currency in words, South Asian grouping (`১২,৩৪,৫৬৭`).
* `normalize_text`: Unicode NFC, Dari enforcement, Bangla Academy short vowels, loanword S-rules.
* `lint_text`: Real-time trapping of Guru-chandali, honorific clashes, and 20+ English calques.
* `prosody_scan`: Scans classical metres (Dalabritta, Matrabritta, Aksharbritta) and verifies 14-akshar Payar couplets.
* `generate_writ_prayer`: Drafts Article 102 High Court constitutional writ prayers in statutory Bengali.

### 4. As a Command-Line Tool (CLI)
Install locally:
```bash
pip install -e .
```
Run any linguistic task instantly:
```bash
# Convert numbers to authentic Bengali words
bhashabid number 99 --format words
# Output: নিরানব্বই

# Format currency in South Asian lakh/crore
bhashabid number 1234567.50 --format currency
# Output: বারো লাখ চৌত্রিশ হাজার পাঁচশত সাতষট্টি টাকা পঞ্চাশ পয়সা

# Lint text for grammatical and calque errors
bhashabid lint "তুমি সিদ্ধান্ত নেন এবং কাজটি বিদ্যুৎ দ্বারা চালিত."

# Verify 14-akshar Payar poetry metre (8+6)
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar

# Draft High Court constitutional writ prayers
bhashabid writ --remedy "detention" --subject "জনাব করিম" --authority "স্বরাষ্ট্র সচিব"
```

### 5. In Python Code / Backend Pipelines
```python
from tools.bn_numbers import number_to_bangla_words, format_lakh_crore
from tools.bn_normalize import normalize
from tools.bn_lint import lint_text
from tools.bn_prosody import verify_payar

# Deterministic numerals
print(number_to_bangla_words(99))  # "নিরানব্বই"

# Orthography & Punctuation
print(normalize("ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন."))
# "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।"

# Linter checks
issues = lint_text("তুমি সিদ্ধান্ত নেন")
for issue in issues:
    print(issue.suggestion)  # Synthesizes bidirectional fixes: তুমি সিদ্ধান্ত নাও / আপনি সিদ্ধান্ত নেন
```

### 6. Cursor Rules (`.cursor/rules`)
Copy [`adapters/cursor/bangla-expert.mdc`](adapters/cursor/bangla-expert.mdc) to `.cursor/rules/` in any project to automatically guide Cursor AI during Bengali coding or copywriting.

---

## 📚 The 8 Supported Professional Sectors

| Sector | Coverage & Capabilities | Reference Guide |
| :--- | :--- | :--- |
| **1. High Court & Legal** | Article 102 writs (Habeas Corpus, Mandamus, Certiorari), Rule Nisi show-cause formulas, statutory deed drafting. | [`constitutional_writs.md`](skills/bangla-expert/references/constitutional_writs.md) |
| **2. Administrative Petitions** | Secretariat instructions (*সচিবালয় নির্দেশমালা*), DC petitions, formal openings (*বিনীত নিবেদন*), closing prayers. | [`official_letters.md`](skills/bangla-expert/references/official_letters.md) |
| **3. Epistolary Hierarchy** | Precise salutations & sign-offs for seniors (*শ্রদ্ধেয়/প্রণামান্তে*), friends (*সুপ্রিয়/ইতি*), and juniors. | [`official_letters.md`](skills/bangla-expert/references/official_letters.md) |
| **4. Macroeconomic Reporting** | TBS financial style, Bangladesh Bank MPS terminology (*নীতি সুদহার*, *বেসিস পয়েন্ট*), active causal clauses. | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) |
| **5. Literary Fiction & Story** | Living spoken dialogue (*কথ্য চলিত রীতি*), character action attribution, pacing, atmospheric sensory cadence. | [`creative_writing.md`](skills/bangla-expert/references/creative_writing.md) |
| **6. Classical Prosody** | Syllabic scansion for Dalabritta, Matrabritta, Aksharbritta (14-akshar Payar 8+6), caesura and rhyme matching. | [`creative_writing.md`](skills/bangla-expert/references/creative_writing.md) |
| **7. Corporate & Advertising** | Natural, punchy marketing copy without raw English buzzwords (*যুগান্তকারী সমাধান* instead of *গেম চেঞ্জার*). | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) |
| **8. Healthcare & Medical** | Precise clinical advice (*উপসর্গ*, *সেবনবিধি*), unambiguous dosage intervals, emergency referral instructions. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |

---

## 🛡️ Rigorous Scientific Governance & Autonomy

Bhashabid operates under strict constitutional rules:
1. **Principle P2 (Provenance)**: Every card requires verified sources, good/bad examples, and common LLM traps. **23/23 cards (100%)** have been authenticated and digitally signed by lead human native speaker `Ashikur Rahman Bhuiyan`.
2. **Principle P4 (Deterministic Tools for Rules)**: Rules that can be computed with math or grammar algorithms are code, not prompt guesses.
3. **Principle P8 (Anti-Self-Deception & Memory)**: Every trapped flaw is logged in [`memory/mistakes/ledger.jsonl`](memory/mistakes/ledger.jsonl) and automatically sealed as an active test in [`eval/unit/test_regression_ledger.py`](eval/unit/test_regression_ledger.py).

---

## 🚦 Release Status: v1.0.0 (Production Stable)

### ✅ Production Deliverables:
- [x] Full deterministic engine (`bn_numbers`, `bn_normalize`, `bn_lint`, `bn_prosody`, `bn_legal`).
- [x] Progressive Agent Skill (`skills/bangla-expert/SKILL.md`) < 390 tokens with 7 modular route guides.
- [x] Model Context Protocol (MCP) Server with 5 tools for Cursor, Claude Desktop, Windsurf, and Zed.
- [x] Developer CLI with 7 subcommands (`number`, `normalize`, `lint`, `prosody`, `writ`, `review`, `practice`).
- [x] 23 Knowledge Cards (100%) reviewed and signed off by lead human native speaker with SHA-256 signatures.
- [x] 59/59 passing unit and regression tests (100% green).
- [x] Automated Daily Practice Engine (`tools/daily_practice_runner.py`).
- [x] Complete GitHub Wiki Documentation (`docs/wiki/`).

---

## 📖 Wiki & Detailed Documentation

Comprehensive documentation is available in the [`docs/wiki/`](docs/wiki/) directory and on the GitHub Wiki:
- [Home & Architecture](docs/wiki/Home.md)
- [Getting Started & Installation](docs/wiki/Getting-Started.md)
- [The 8 Core Writing Domains](docs/wiki/The-8-Writing-Domains.md)
- [Model Context Protocol (MCP) Integration](docs/wiki/Model-Context-Protocol-(MCP).md)
- [Poetic Prosody & Payar Verification](docs/wiki/Poetic-Prosody-&-Payar.md)
- [Article 102 Constitutional Writs](docs/wiki/Constitutional-Writs-(Article-102).md)
- [Principle P2 Provenance & Human Review](docs/wiki/Principle-P2-Provenance-&-Review.md)

---

## 📄 License

* **Code & Deterministic Engines**: Apache 2.0 (Open-source, commercial-friendly).
* **Knowledge Cards & Documentation**: CC BY-SA 4.0.
