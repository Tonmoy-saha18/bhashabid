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

## Cycle 2: Advanced Linter & Syntactic Sandhi/Samas Engine (Upcoming)
- [ ] TASK-020: Implement `tools/bn_lint` (static AST/heuristic linter detecting Guru-chandali, honorific clash, and calques).
- [ ] TASK-021: Knowledge cards for Sandhi, Samas, and case markers (-এর, -কে, -তে, -এ).
- [ ] TASK-022: Parallel corpus ingestion pipeline (`pipeline/01_sources/` to `03_clean/`) using approved sources.
- [ ] TASK-023: MCP Server implementation (`tools/mcp_server/`) exposing tools over standard protocol.
