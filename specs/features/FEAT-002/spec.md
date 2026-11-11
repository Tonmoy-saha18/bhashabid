# Feature Specification: FEAT-002 (Linguistic Linter, Grammar Knowledge & MCP Server)

## 1. Overview
FEAT-002 introduces automated static linting (`tools/bn_lint`), expands the linguistic knowledge base with Sandhi, Samas, and Case Markers (`knowledge/cards/`), implements the standard MCP Server (`tools/mcp_server/`), and sets up the clean corpus ingestion pipeline (`pipeline/`).

## 2. Requirements Addressed
- **REQ-026 - REQ-027**: Sadhu-Cholito mixing detection (Guru-chandali dosh).
- **REQ-028 - REQ-030**: Honorific concordance verification (আপনি/তুমি/তুই).
- **REQ-032, REQ-034, REQ-035**: English passive calque avoidance and postposition case markers.
- **REQ-037 - REQ-038**: Mistake ledger and regression harness expansion.

## 3. Interfaces & Contracts
`bn_lint.lint_text(text: str, profile: str = "bd_standard") -> list[LintIssue]`
`tools.mcp_server.server`: Handles standard MCP JSON-RPC requests for tools (`convert_number`, `normalize_text`, `lint_text`).
