# Bhashabid Continuous Daily Practice & Learning Plan (দৈনিক ২-৩ ঘণ্টার নিবিড় অনুশীলন ও আত্মউন্নয়ন রূপরেখা)

## 1. Executive Objective
To systematically transition Bhashabid from an experimental research engine into a production-grade, hardened Bengali linguistic coprocessor that hundreds of thousands of people (citizens, journalists, authors, lawyers, administrators, researchers) can use daily with complete trust.

The daily 2.5-hour practice cycle runs autonomously under strict constitutional supervision (Principles P1–P8), trapping flaws, cataloging mistakes, hardening rules, expanding tests, and preparing review packets for human experts.

---

## 2. Daily 150-Minute Block Schedule (সময়সূচি ও পর্যায়ক্রম)

| Block | Duration | Focus Area | Responsible Agents | Primary Output |
| :---: | :---: | :--- | :--- | :--- |
| **Block 1** | **20 min** | **Corpus Ingestion & Fresh Parallel Mining** | A4 (Curator) & A5 (Learner) | Crawl/ingest latest open news, legal circulars, and academic releases into `pipeline/01_sources/`. |
| **Block 2** | **35 min** | **Adversarial Domain Stress-Testing** | A11 (QA) & A12 (Evaluator) | Rotate across 2-3 target sectors (e.g. Day 1: Legal + Fiction; Day 2: Macroeconomics + Admin). Run parallel baseline vs skill evaluations. |
| **Block 3** | **30 min** | **Deterministic Trapping & Mistake Ledgering** | A13 (Mistake Analyst) & A8 (Memory) | Execute `bn_lint`, `bn_prosody`, `bn_legal`. Auto-triage all defects and log into `memory/mistakes/ledger.jsonl`. |
| **Block 4** | **35 min** | **Dual Reification: Code & Knowledge Hardening** | A6 (Developer) & A9 (Distiller) | Implement new regex guards in `tools/bn_lint/`, write new atomic cards in `knowledge/cards/`, and update reference modules. |
| **Block 5** | **20 min** | **Regression Sealing & Test Suite Execution** | A7 (Tester) & A14 (Reviewer) | Convert every logged mistake into an active unit test. Run full test suite; guarantee 0% regression rate. |
| **Block 6** | **10 min** | **Reporting & Review Packet Generation** | A15 (Human Liaison) & A1 (Orchestrator) | Generate daily health report in `eval/reports/daily_runs/` and regenerate `docs/review_queue/` for human review. |

---

## 3. Seven-Day Sector Rotation Matrix (সাপ্তাহিক চক্র)

To ensure comprehensive coverage without domain stagnation, the daily practice rotates sectors across the week:

- **Monday (সোম)**: Judicial Decrees, High Court Writs & Legal Contracts (Art. 102, deed preambles, statutory notice drafting).
- **Tuesday (মঙ্গল)**: Macroeconomics, Banking (TBS & BB style), Monetary Policy, and Commercial Advertising.
- **Wednesday (বুধ)**: Administrative Circulars, Secretariat Instructions, and Official Petitions / Epistolary Hierarchy.
- **Thursday (বৃহস্পতি)**: Literary Fiction, Living Dialogue Cadence, Pacing, and Non-Fiction Essay Architecture.
- **Friday (শুক্র)**: Classical Prosody (পয়ার, মাত্রাবৃত্ত, দলবৃত্ত) and Poetry Rhyme & Metre Verification.
- **Saturday (শনি)**: Academic Research Journals, Scientific Methodology, and Healthcare/Public Health Advisories.
- **Sunday (রবি)**: System Audit, Dialect Reconciliation (`bd_standard` vs `wb_standard`), and Human Review Packet Sign-Off.

---

## 4. Hard Autonomy & Safety Boundaries

1. **Kill-Switch Immediate Halt**:
   The loop polls for `state/STOP` every iteration. If present, it safely closes all file descriptors and exits within 500ms.
2. **Zero Paid API Cost**:
   Monetary spend limit remains strictly `$0.00` per `state/BUDGET.md`.
3. **P2 Provenance Inviolability**:
   The autonomous loop **never** promotes cards to `reviewed`. All new discoveries remain at `data-supported` until authenticated by human review.
4. **The "Never Fail Twice" Invariant**:
   A daily cycle is classified as `FAILED` if any previously resolved mistake from `memory/mistakes/ledger.jsonl` fails in `test_regression_ledger.py`.
