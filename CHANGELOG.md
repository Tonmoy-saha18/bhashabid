# Changelog

All notable changes to Bhashabid are documented here following Semantic Versioning.

## [0.4.0] - 2026-11-11 - Cycle 4 Release
### Added
- Regional Dialect Profiles in `tools/bn_normalize/profiles.py` (`bd_standard` vs `wb_standard`).
- High-throughput streaming batch normalizer in `pipeline/03_process/batch_normalizer.py` (> 290,000 words/sec).
- Human Review Liaison packet generator (`tools/review_packet_generator.py`) and review queue packet (`docs/review_queue/packet_001_initial_cards.md`).
- Knowledge card `CRD-ORT-003` (Regional Orthographic Variations).
- Comprehensive test suite expansion (46 automated tests passing in 3.6s).

## [0.3.0] - 2026-11-11 - Cycle 3 Release
### Added
- Developer CLI `bhashabid` (`tools/cli.py`) with `number`, `normalize`, and `lint` subcommands.
- Standard distribution packaging via `pyproject.toml` (v0.3.0).
- IDE & Runtime Adapters: Cursor rules (`adapters/cursor/.cursorrules`) and Claude prompt (`adapters/claude/claude_system_prompt.txt`).
- Architecture Decision Records: ADR-001 (Progressive Skill Disclosure) and ADR-002 (Deterministic Bengali Token Boundaries).
- Cross-Model Benchmark Matrix (`eval/benchmarks/benchmark_matrix.py`) showing +90.0% net lift over raw baseline LLMs.
- Full traceability: All 40 initial requirements (REQ-001 through REQ-040) marked `IMPLEMENTED` with 41 passing automated tests.

## [0.2.0] - 2026-11-11 - Cycle 2 Release
### Added
- Static Linguistic Linter `tools/bn_lint` detecting Sadhu-Cholito mixing (Guru-chandali), honorific clashes, and English calques.
- Bidirectional honorific suggestion engine (`তুমি সিদ্ধান্ত নাও` vs `আপনি সিদ্ধান্ত নেন`).
- Model Context Protocol (MCP) server `tools/mcp_server/`.
- Knowledge cards for Case Markers (`CRD-GRM-003`), Sandhi (`CRD-GRM-004`), Samas (`CRD-GRM-005`), and Anti-Calques (`CRD-TRN-001`).
- Source verification and cleaning pipeline skeleton in `pipeline/`.

## [0.1.0] - 2026-11-11 - Cycle 1 Release
### Added
- Deterministic normalizer `tools/bn_normalize` (Unicode NFC, composite nukta precomposition, Dari punctuation, loanword orthography).
- Progressive skill architecture `skills/bangla-expert/SKILL.md` (< 600 tokens) with modular reference guides.
- Knowledge cards: `CRD-NUM-001`, `CRD-ORT-001`, `CRD-ORT-002`, `CRD-GRM-001`, `CRD-GRM-002`.
- Initial benchmark suite in `eval/benchmarks/run_cycle1_evals.py`.

## [0.0.1] - 2026-11-11 - Bootstrap
### Added
- Repository foundation, constitution, EARS requirements (REQ-001..040), 15 BMAD agent personas.
- Deterministic numeral engine `tools/bn_numbers` with 0-99 irregular lookup, lakh/crore formatting, ordinals, currency, and fractions.
- Mistake ledger `memory/mistakes/ledger.jsonl` and automated regression test runner.
