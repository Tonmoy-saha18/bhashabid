# Bhashabid (ভাষাবিদ) — The First Bengali Language Coprocessor Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: >=3.10](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://python.org)
[![Version: v1.0.0](https://img.shields.io/badge/Version-v1.0.0-blue.svg)](https://github.com/ashik1291/bhashabid)
[![Tests: 64 Passing](https://img.shields.io/badge/Tests-64%20Passing-brightgreen.svg)](eval/unit)
[![Proven Knowledge: 26 Reviewed Cards](https://img.shields.io/badge/P2%20Provenance-26%2F26%20Cards%20Reviewed-blueviolet.svg)](knowledge/cards)

> **Bhashabid** (ভাষাবিদ) is the **first-ever open-source Bengali language coprocessor engine** designed to work alongside AI agents, foundation models (LLMs), and developer workflows. Operating as an external cognitive and deterministic coprocessor without retraining model weights, it systematically elevates the accuracy, orthography, and native fluency of AI-generated Bengali across daily professional and creative activities.

---

## 🎯 What Bhashabid Does & Where Frontier Models Fail (An Honest Assessment)

Frontier language models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, DeepSeek) are exceptionally powerful reasoning engines, but they are trained predominantly on English-centric corpora. While they possess vast latent Bengali vocabularies, their generative decoders frequently fall back onto **English syntactic habits, literal idioms, and naive numerical assemblies**.

Bhashabid does not exaggerate its capabilities or claim to replace foundation models. Instead, it acts as a **specialized coprocessor**: executing deterministic algorithms for rules that require mathematical precision, and serving modular reference knowledge when the model requires domain-specific judgment.

### Side-by-Side Honest Comparison:

| Linguistic Dimension | Where Frontier Models Consistently Fail (Raw) | What Bhashabid Does (Coprocessor) | Real-World Example |
| :--- | :--- | :--- | :--- |
| **1. Cardinal Numerals & Currency** | Naively compounds numbers or uses decimal digit translation (*নব্বই নয়* instead of *নিরানব্বই*); formats currency with Western 3-digit commas (`1,234,567`). | Provides a 100% deterministic lookup engine for all 0-99 irregular cardinals, fractions (*দেড়, আড়াই*), and South Asian lakh/crore comma grouping. | Input `99` ➔ Raw: *"নব্বই নয়"* ❌ <br>Bhashabid: **"নিরানব্বই"** ✔️ |
| **2. English Passive Voice Calques** | Translates English passives literally using *"দ্বারা"* (*"দ্বারা চালিত"*, *"দ্বারা অনুষ্ঠিত"*), producing unnatural, stiff Bengali. | Real-time static linter flags passive calques and synthesizes natural active causal phrasing. | Raw: *"খাদ্যমূল্য বৃদ্ধির দ্বারা চালিত"* ❌ <br>Bhashabid: **"খাদ্যপণ্যের মূল্যবৃদ্ধির কারণে... দাঁড়িয়েছে"** ✔️ |
| **3. Judicial & High Court Formulas** | Translates show-cause Rule Nisi orders as conversational clauses (*"জিজ্ঞেস করে রুল জারি করেছে"*); omits judicial honorific plural. | Enforces canonical Bangladesh Supreme Court reporting formulas and Article 102 constitutional writ prayers. | Raw: *"কেন নিষ্ক্রিয়তা বেআইনি হবে না জিজ্ঞেস করে রুল দিয়েছে"* ❌ <br>Bhashabid: **"কেন বেআইনি ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন"** ✔️ |
| **4. Administrative Petitions & Salutations** | Calques *"Dear Sir"* as conversational *"প্রিয় মহাশয়"*; uses broken colonial closings (*"আপনার বিশ্বস্ত দাস"*). | Enforces Bangladesh Secretariat instructions (*সচিবালয় নির্দেশমালা*) and dignified petition protocols. | Raw: *"প্রিয় মহাশয়, আশা করি ভালো আছেন"* ❌ <br>Bhashabid: **"বরাবর... বিষয়:... জনাব, বিনীত নিবেদন এই যে..."** ✔️ |
| **5. Sports Vernacular** | Translates sports defeat clichés literally (*"conceded defeat against"* ➔ *"বিরুদ্ধে পরাজয় স্বীকার করেছে"*). | Embeds authentic sports journalism idioms (*প্রতিপক্ষের কাছে হেরেছে*). | Raw: *"সফরকারীদের বিরুদ্ধে পরাজয় স্বীকার করেছে"* ❌ <br>Bhashabid: **"সফরকারীদের কাছে ৫ উইকেটে হেরেছে"** ✔️ |
| **6. Bangla Academy Orthography** | Persistently spells loanwords with *"ষ"* (*ষ্টেশন, পোষ্ট*); uses long *"ী"* in non-tatsama words (*পাখী, দাদী, হাতী*). | Deterministically normalizes text to modern Bangla Academy standards (short *ি/ু* for tatbhava words, *স* for loanwords). | Raw: *"রেল ষ্টেশনে পাখী ডাকছে"* ❌ <br>Bhashabid: **"রেল স্টেশনে পাখি ডাকছে"** ✔️ |
| **7. Classical Poetic Scansion** | Produces pseudo-poetry with superficial line breaks but zero metrical scansion or caesura harmony. | Deterministic phonological syllabifier (*মুক্তদল* vs *রুদ্ধদল*) verifies Dalabritta, Matrabritta, and 14-akshar Payar (8+6). | Raw: Broken 16-syllable prose line ❌ <br>Bhashabid: **Validates exact 8+6=14 akshar Payar cadence** ✔️ |
| **8. Sentence-Ending Punctuation** | Terminates Bengali sentences with ASCII periods (`.`) instead of Dari (`।`). | Deterministically converts sentence-ending periods to Dari while safely preserving decimal numbers (`৩.১৪`). | Raw: *"তিনি বাড়ি গেলেন."* ❌ <br>Bhashabid: **"তিনি বাড়ি গেলেন।"** ✔️ |
| **9. Land Records & Deeds** | Translates statutory conveyancing into informal colloquial text (*"জমির বিক্রির কাগজ"*). | Enforces statutory Registration Act deed taxonomy (সাফ-কবলা, মৌজা, খতিয়ান, দাগ নং, চৌহদ্দি, নামজারি). | Raw: *"জমির বিক্রির কাগজ হস্তান্তর করলাম"* ❌ <br>Bhashabid: **"রেজিস্ট্রিকৃত সাফ-কবলা বিক্রয় দলিলমূলে চূড়ান্ত দখল বুঝিয়ে দেওয়া হলো"** ✔️ |
| **10. Disaster Early Warning** | Translates "storm surge" literally as *"ঝড় বৃদ্ধি"*; hallucinates warning terms (*"বড় বিপদ সংকেত"*). | Enforces official BMD maritime warning signals (মহাবিপদ সংকেত ১-১০) and canonical *জলোচ্ছ্বাস*. | Raw: *"উপকূলীয় অঞ্চলে ঝড় বৃদ্ধি দেখা যেতে পারে"* ❌ <br>Bhashabid: **"উপকূলীয় জেলাসমূহে ৫-৭ ফুট উচ্চতার জলোচ্ছ্বাসের আশঙ্কা রহিয়াছে"** ✔️ |
| **11. NCTB Creative Pedagogy** | Generates arbitrary essay questions without adhering to the 4-tier Bloom rubric. | Formulates canonical NCTB Creative Question framework (উদ্দীপক, জ্ঞানমূলক, অনুধাবনমূলক, প্রয়োগমূলক, উচ্চতর দক্ষতামূলক). | Raw: Unstructured single essay prompts ❌ <br>Bhashabid: **Structured 4-tier Bloom's taxonomy rubric (ক/খ/গ/ঘ)** ✔️ |

---

## 👥 Who Should Use Bhashabid & Why?

Bhashabid is engineered for anyone who needs **authentic, dignified, and error-free Bengali** without falling victim to robotic machine-translation habits:

| Persona / Sector | Why They Need Bhashabid | Key Capabilities Used |
| :--- | :--- | :--- |
| **Lawyers, Advocates & Legal Scholars** | Frontier LLMs fabricate colloquial terms for writs (calling *Habeas Corpus* "বন্দি মুক্তির আবেদন") or ruin legal notices by translating *"Without Prejudice"* as *"কোনো ক্ষতি ছাড়া"*. Bhashabid enforces authentic Supreme Court formulas, statutory Article 102 prayers, and precise Bengali terms (*স্বত্বহানি ব্যতিরেকে*). | `bhashabid writ` & [`constitutional_writs.md`](skills/bangla-expert/references/constitutional_writs.md) |
| **Land Owners, Buyers & Registry Writers** | Property conveyance requires strict terminology (CS/SA/RS/BS খতিয়ান, দাগ নং, মৌজা, চৌহদ্দি, সাফ-কবলা, নামজারি). Bhashabid prevents loose, legally hazardous machine phrasing. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **Government & Corporate Officials** | Administrative letters, secretariat memos, and DC petitions must follow the official *Bangladesh Secretariat Instructions* (*সচিবালয় নির্দেশমালা*)—not casual English email calques (*"প্রিয় মহাশয়"*). Bhashabid enforces proper salutations and formal closings (*বিনীত নিবেদক*). | [`official_letters.md`](skills/bangla-expert/references/official_letters.md) & `bhashabid lint` |
| **Journalists, Editors & Financial Analysts** | Macroeconomic and sports reporting require strict terminological precision (e.g., using Bangladesh Bank's *নীতি সুদহার* instead of *পলিসি রেট*; *মূল্যস্ফীতি* instead of *মুদ্রাস্ফীতি*). Bhashabid ensures active causal phrasing instead of awkward passive voice. | [`journalism_domains.md`](skills/bangla-expert/references/journalism_domains.md) & `bhashabid lint` |
| **Agronomists, Farmers & Disaster Responders** | Early warning bulletins demand exact terminology (*মহাবিপদ সংকেত*, *জলোচ্ছ্বাস*, *সুষম সার ও বালাইনাশক*) to prevent panic or life-threatening misinformation. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **Healthcare & Medical Communicators** | Frontier LLMs make dangerous medical translation errors (e.g., translating clinical *"drugs"* into *"মাদক"* instead of *"ওষুধ/অ্যান্টিবায়োটিক"*). Bhashabid enforces safe, unambiguous clinical terms and emergency triage protocols. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **Educators, Teachers & Curriculum Authors** | Structuring exam papers under the national curriculum requires strict adherence to NCTB's 4-tier Creative Questioning taxonomy (*উদ্দীপক*, *জ্ঞান*, *অনুধাবন*, *প্রয়োগ*, *উচ্চতর দক্ষতা*). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **Poets, Novelists & Creative Writers** | Generative AI models struggle with rhythm, breaking living spoken dialogue tags and mangling traditional 14-akshar Payar (8+6) verse. Bhashabid deterministically calculates syllables (*মুক্তদল/রুদ্ধদল*) and validates poetic metres. | `bhashabid prosody` & [`creative_writing.md`](skills/bangla-expert/references/creative_writing.md) |
| **Software Engineers & AI Agent Builders** | Developers building Bengali bots, search engines, or RAG pipelines can plug in the **Model Context Protocol (MCP)** server or Python library to audit AI outputs locally at 50,000–500,000 words/second with **zero token cost ($0.00)**. | `bhashabid-mcp` & Python SDK |
| **Students, Researchers & Everyday Users (No-Code)** | Anyone using ChatGPT, Claude, or Gemini in their web browser can simply paste `STANDALONE_ALL_IN_ONE.md` into Custom Instructions to instantly transform raw LLMs into seasoned native Bengali editors. | [`STANDALONE_ALL_IN_ONE.md`](skills/bangla-expert/STANDALONE_ALL_IN_ONE.md) |

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
# Run stdio MCP server for Claude Desktop / Cursor / Antigravity
bhashabid-mcp
# or: bhashabid mcp
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

## 📚 The 11 Supported Professional Sectors

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
| **9. Land Records & Deeds** | Sub-Kabala conveyance, Heba, partition deeds, CS/SA/RS/BS Khatian, plot and boundary (*চৌহদ্দি*) descriptions. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **10. Agronomy & Disaster Warnings** | BMD cyclone warning signals (1-10 মহাবিপদ সংকেত), storm surge (*জলোচ্ছ্বাস*), fertilizer and pesticide balance. | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |
| **11. Education & Pedagogy** | NCTB 4-tier Creative Questioning framework (উদ্দীপক, জ্ঞানমূলক, অনুধাবনমূলক, প্রয়োগমূলক, উচ্চতর দক্ষতামূলক). | [`academic_legal_medical.md`](skills/bangla-expert/references/academic_legal_medical.md) |

---

## 🛡️ Rigorous Scientific Governance & Autonomy

Bhashabid operates under strict constitutional rules:
1. **Principle P2 (Provenance)**: Every card requires verified sources, good/bad examples, and common LLM traps. **26/26 cards (100%)** have been authenticated and digitally signed by lead human native speaker `Ashikur Rahman Bhuiyan`.
2. **Principle P4 (Deterministic Tools for Rules)**: Rules that can be computed with math or grammar algorithms are code, not prompt guesses.
3. **Principle P8 (Anti-Self-Deception & Memory)**: Every trapped flaw is logged in [`memory/mistakes/ledger.jsonl`](memory/mistakes/ledger.jsonl) and automatically sealed as an active test in [`eval/unit/test_regression_ledger.py`](eval/unit/test_regression_ledger.py).

---

## 🚦 Release Status: v1.0.0 (Production Stable)

### ✅ Production Deliverables:
- [x] Full deterministic engine (`bn_numbers`, `bn_normalize`, `bn_lint`, `bn_prosody`, `bn_legal`).
- [x] Progressive Agent Skill (`skills/bangla-expert/SKILL.md`) < 390 tokens with 7 modular route guides.
- [x] Model Context Protocol (MCP) Server with 5 tools for Cursor, Claude Desktop, Windsurf, and Zed.
- [x] Developer CLI with 7 subcommands (`number`, `normalize`, `lint`, `prosody`, `writ`, `review`, `practice`).
- [x] 26 Knowledge Cards (100%) reviewed and signed off by lead human native speaker with SHA-256 signatures.
- [x] 64/64 passing unit and regression tests (100% green).
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
