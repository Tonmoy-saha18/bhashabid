# Specifications & Features Changelog

## [2026-11-11] - Principle P2 Human Review Milestones
- **21 Knowledge Cards Promoted to `reviewed`**:
  - Reviewer: Ashikur Rahman Bhuiyan (`ashikur.bhuiyan@brainstation-23.com`)
  - Status: `APPROVED` with cryptographic SHA-256 signatures sealed in cards (`CRD-DOM-001..008`, `CRD-GRM-001..005`, `CRD-NUM-001`, `CRD-ORT-001..003`, `CRD-TRN-001..004`).
  - Principle P2 provenance audit verified 100% compliant.

## [2026-11-11] - Advanced Prosody, Constitutional Writs & Authenticated Human Review Solutions
- **Bengali Poetic Prosody Engine** (`tools/bn_prosody/`):
  - Phonetic syllabifier (`মুক্তদল` vs `রুদ্ধদল`).
  - Mora counting across 3 classical metres (দলবৃত্ত, মাত্রাবৃত্ত, অক্ষরবৃত্ত).
  - 14-akshar Payar metre validator (৮ + ৬ পর্ব ও মধ্যযতি) and end-rhyme (অন্ত্যমিল) checker.
  - Knowledge card: `CRD-DOM-009.yaml`.
- **Article 102 Constitutional Writs Engine** (`tools/bn_legal/`):
  - Statutory grounding for 5 constitutional writs (Habeas Corpus, Mandamus, Certiorari, Prohibition, Quo Warranto).
  - Deterministic prayer generator and classification engine.
  - Knowledge card: `CRD-TRN-005.yaml` & Reference guide: `references/constitutional_writs.md`.
- **Principle P2 Authenticated Human Review Protocol** (`tools/human_reviewer.py` & `tools/verify_provenance.py`):
  - Native-speaker review harness with cryptographic SHA-256 content checksums.
  - Strict P2 audit preventing agent self-promotions.
- **Developer CLI Expanded** (`tools/cli.py`): Added `prosody`, `writ`, and `review` subcommands.
- **Test Suite**: Expanded to 59/59 passing unit tests.

## [2026-11-11] - Multi-Domain Sector Expansion & Stress Audit
- **8 Core Domains Added**:
  - `CRD-DOM-001`: Official Administrative Applications & Petitions (দাপ্তরিক আবেদন ও দরখাস্ত)
  - `CRD-DOM-002`: Letter Writing & Epistolary Hierarchy (চিঠিপত্র ও সামাজিক যোগাযোগ)
  - `CRD-DOM-003`: Literary Fiction, Story Writing & Dialogue (কথাসাহিত্য ও কথ্য সংলাপ)
  - `CRD-DOM-004`: Academic & Scholarly Research Prose (শিক্ষায়তনিক ও গবেষণা প্রবন্ধ)
  - `CRD-DOM-005`: Book Authoring & Non-Fiction Essays (মননশীল প্রবন্ধ ও গ্রন্থ প্রণয়ন)
  - `CRD-DOM-006`: Corporate & Commercial Copywriting (বাণিজ্যিক বিজ্ঞাপন ও কর্পোরেট যোগাযোগ)
  - `CRD-DOM-007`: Legal Drafting & Contract Agreements (আইনি দলিল ও চুক্তিপত্র)
  - `CRD-DOM-008`: Healthcare & Medical Public Advisories (চিকিৎসাসেবা ও জনস্বাস্থ্য বার্তা)
- **Modular Guides Added**:
  - `skills/bangla-expert/references/official_letters.md`
  - `skills/bangla-expert/references/creative_writing.md`
  - `skills/bangla-expert/references/academic_legal_medical.md`
- **Progressive Routing**: Expanded `skills/bangla-expert/SKILL.md` (289 words, strictly within < 600 token limit).
- **Mistake Ledger**: Logged and resolved `MST-0008`..`MST-0011` in `memory/mistakes/ledger.jsonl`.
- **Deterministic Linter**: Added rules for application greetings (`প্রিয় মহাশয়`), letter sign-offs (`আপনার বিশ্বস্তভাবে`), academic calques (`পেপারটি তর্ক করে`), and marketing buzzwords (`গেম চেঞ্জার`, `পেইন পয়েন্ট`).
- **Audit Report**: Generated `eval/reports/multi_domain_stress_audit.md` (100% linter defect reduction).
- **Review Queue**: Expanded to 21 atomic cards in `docs/review_queue/packet_001_initial_cards.md`.
- **Test Suite**: 52/52 tests passing.

## [2026-11-11] - Stress Testing & Domain Hardening
- **MST-0006**: Judicial show-cause Rule Nisi calque detection added to `tools/bn_lint/calques.py`. Card `CRD-TRN-002` created.
- **MST-0007**: Sports defeat reporting calque detection added to `tools/bn_lint/calques.py`. Card `CRD-TRN-004` created.
- **CRD-TRN-003**: Macroeconomic & TBS financial news conventions card and reference guide created.
- **Progressive Skill Routing**: Added `references/journalism_domains.md` to `skills/bangla-expert/SKILL.md` (< 600 tokens maintained).
- **Test Suite**: Expanded to 48/48 tests, verifying new calques and regression ledger assertions.
