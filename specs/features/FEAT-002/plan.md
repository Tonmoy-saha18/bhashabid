# Implementation Plan: FEAT-002

## Cycle: 2
## Owners: A1 (Orchestrator), A3 (Architect), A6 (Developer), A9 (Knowledge Distiller)

### Schedule:
1. **Design & Contracts** [A3]: Define `LintIssue` schema and MCP tool signatures.
2. **Linter Engine** [A6]: Implement `tools/bn_lint/` (Guru-chandali, honorifics, calques) test-first.
3. **Knowledge Cards** [A9]: Author cards for Case Markers (`CRD-GRM-003`), Sandhi (`CRD-GRM-004`), Samas (`CRD-GRM-005`), and Anti-Calque (`CRD-TRN-001`).
4. **MCP Server** [A6]: Implement `tools/mcp_server/` protocol handler and CLI entrypoint.
5. **Corpus Pipeline** [A4]: Implement ingestion skeleton `pipeline/01_sources/` and `pipeline/02_clean/`.
6. **Testing & QA** [A7 / A11]: Add unit tests in `eval/unit/test_bn_lint.py` and `eval/unit/test_mcp_server.py`.
7. **Evaluation & Gating** [A12 / A14]: Benchmark linter precision/recall and issue Cycle 2 audit report.
