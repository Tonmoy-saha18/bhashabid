# Feature Specification: FEAT-003 (CLI Tooling, Multi-Model Benchmark Matrix & Distribution Packaging)

## 1. Overview
FEAT-003 delivers the developer-facing CLI interface (`tools/cli.py`), runtime IDE adapters (`adapters/cursor/`, `adapters/claude/`), the cross-model evaluation matrix, Architecture Decision Records (`docs/adr/`), and standard distribution packaging (`pyproject.toml`).

## 2. Requirements Addressed
- **REQ-001 - REQ-015**: Numeral conversions accessible via CLI `bhashabid number`.
- **REQ-016 - REQ-025**: Normalization accessible via CLI `bhashabid normalize`.
- **REQ-026 - REQ-035**: Linguistic linting accessible via CLI `bhashabid lint`.
- **REQ-039**: Multi-model benchmark matrix (Baseline vs Skill vs Skill+Tools).

## 3. CLI Interface Contracts
- `bhashabid number <val> [--format words|grouped|currency|fraction|ordinal]`
- `bhashabid normalize <text_or_path> [--profile bd_standard|wb_standard]`
- `bhashabid lint <text_or_path> [--json]`
- `bhashabid mcp`
