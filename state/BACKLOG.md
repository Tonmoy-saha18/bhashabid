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
- [x] TASK-024: Unit tests and regression suite expansion (33 tests passing).
- [x] TASK-025: Bidirectional honorific repair (MST-0005, LES-002).

## Cycle 3: Developer CLI, Benchmark Matrix & Distribution Packaging (COMPLETED)
- [x] TASK-030: Standalone CLI interface `bhashabid` (`tools/cli.py`) for command-line number conversion, normalization, and linting.
- [x] TASK-031: Multi-model prompt evaluation matrix comparing Baseline vs Skill vs Skill+Tools (+90.0% Net Lift).
- [x] TASK-032: Automated packaging for PyPI / wheel distribution (`pyproject.toml`).
- [x] TASK-033: IDE and runtime adapters (`adapters/cursor/`, `adapters/claude/`).
- [x] TASK-034: Architectural Decision Records (`docs/adr/001-progressive-skill-disclosure.md`, `docs/adr/002-deterministic-bengali-grapheme-regex.md`).
- [x] TASK-035: Unit and integration tests (41 tests passing).

## Cycle 4: Regional Dialect Profiles, Streaming Corpus Pipeline & Human Review Queue (COMPLETED)
- [x] TASK-040: Regional dialect adaptation profiles: West Bengal (`wb_standard`) vs Bangladesh Standard (`bd_standard`).
- [x] TASK-041: High-throughput streaming batch normalizer (`pipeline/03_process/`) with >290,000 words/sec throughput.
- [x] TASK-042: Interactive Human Review Liaison dashboard (`docs/review_queue/packet_001_initial_cards.md`).
- [x] TASK-043: Regional orthography knowledge card (`CRD-ORT-003`).
- [x] TASK-044: Comprehensive unit and regression test expansion (46 tests passing).

## Cycle 5: Long-Horizon Autonomous Corpus Mining & Web Demonstrator (Future)
- [ ] TASK-050: Ingest full Bengali Wikipedia dumps via `pipeline/` and generate frequency dictionary.
- [ ] TASK-051: Lightweight local web playground (FastAPI / HTML UI) for interactive Bengali linting and conversion.
- [ ] TASK-052: Continuous benchmark evaluation matrix running against live LLM endpoints.
