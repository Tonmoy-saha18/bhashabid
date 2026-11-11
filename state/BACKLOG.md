# Bhashabid Project Backlog

## Cycle 0: Bootstrap & Foundations (COMPLETED)
- [x] TASK-001: Project structure, licenses, and documentation.
- [x] TASK-002: Requirements REQ-001 to REQ-040.
- [x] TASK-003: 15 Agent personas.
- [x] TASK-004: Tool `bn_numbers` with full irregular coverage (0-99).
- [x] TASK-005: User approval for sources and budget.

## Cycle 1: Normalization, Orthography & Core Skill (COMPLETED)
- [x] TASK-010: Implement `bn_normalize` (NFC, য়/ড়/ঢ় canonicalization, Dari punctuation, loanword S-rule).
- [x] TASK-011: Knowledge cards for orthography, Sadhu/Cholito verb consistency, and honorifics.
- [x] TASK-012: Progressive `SKILL.md` (< 600 tokens) and reference guides.
- [x] TASK-013: Unit tests, token budget checks, and benchmark comparison (+100.0% win rate).
- [x] TASK-014: Live tasks audit and mistake ledger updates (MST-0002, MST-0003, LES-001).

## Cycle 2: Advanced Linter, MCP Server & Grammar Cards (COMPLETED)
- [x] TASK-020: Implement `tools/bn_lint` (static AST/heuristic linter detecting Guru-chandali, honorific clash, and calques).
- [x] TASK-021: Knowledge cards for Case markers (`CRD-GRM-003`), Sandhi (`CRD-GRM-004`), Samas (`CRD-GRM-005`), and Anti-Calque translation (`CRD-TRN-001`).
- [x] TASK-022: MCP Server implementation (`tools/mcp_server/`) exposing tools over standard protocol.
- [x] TASK-023: Corpus ingestion & verification pipeline (`pipeline/01_sources/` and `pipeline/02_clean/`).
- [x] TASK-024: Unit tests and regression suite expansion (32 tests passing).
- [x] TASK-025: Mistake ledger logging (MST-0004) and benchmark reporting (`cycle_002_report.md`).

## Cycle 3: Multi-Model Evaluation Matrix & CLI Tooling (Upcoming)
- [ ] TASK-030: Standalone CLI interface `bhashabid` (`tools/cli.py`) for command-line number conversion, normalization, and linting.
- [ ] TASK-031: Multi-model prompt evaluation matrix (Baseline vs Skill vs Skill+Tools) on held-out translation sets.
- [ ] TASK-032: Automated packaging for PyPI / wheel distribution.
