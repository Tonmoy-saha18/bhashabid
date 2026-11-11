# Bhashabid Developer & Agent Guide (CLAUDE.md)

Welcome to Bhashabid. When operating inside this repository, adhere strictly to the project constitution (`specs/00-constitution.md`).

## Core Operating Instructions
1. **Spec First (P1)**: Every tool, card, or skill change must cite a requirement ID from `specs/02-requirements.md` or a feature spec.
2. **Autonomy Boundaries**:
   - *Autonomous*: Write code, write tests, run tests, ingest registered sources, draft cards as `llm-hypothesis` or `data-supported`, run benchmarks, log mistakes.
   - *User Approval Required*: Registering new external sources with unverified licenses, budget increases, main branch merges, tagging releases, card promotion to `reviewed`.
   - *Forbidden*: Never mark a card `reviewed` without recorded human native speaker confirmation. Never scrape paywalled content. Never bypass `state/STOP`.
3. **Kill Switch**: If `state/STOP` exists, halt execution immediately.
4. **Deterministic First**: Solve numerals, ordinals, dates, punctuation, and Unicode via `tools/`. Do not rely on LLM prompts for deterministic logic.
5. **Testing**: Run tests using `python -m unittest discover -s eval/unit`.
