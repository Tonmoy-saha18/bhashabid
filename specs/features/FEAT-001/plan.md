# Implementation Plan: FEAT-001

## Cycle: 1
## Owner: A1 (Orchestrator) & A3 (Architect)

### Phase Schedule:
1. **Design & Schema** [A3 Architect]: Normalizer interface and card metadata schema.
2. **Deterministic Code** [A6 Developer]: Implement `tools/bn_normalize/` test-first.
3. **Knowledge Distillation** [A9 Knowledge Distiller]: Author initial cards in `knowledge/cards/` (CRD-ORT-001..002, CRD-GRM-001..002).
4. **Skill Layer** [A10 Skill Engineer]: Build `skills/bangla-expert/SKILL.md` and references (`numerals.md`, `orthography.md`, `grammar_registers.md`).
5. **Testing** [A7 Tester]: Exhaustive Unicode, Dari, whitespace, and token count unit tests in `eval/unit/`.
6. **QA & E2E Verification** [A11 QA Agent]: E2E scenario validation.
7. **Benchmarking** [A12 Evaluator]: Benchmark matrix evaluation (Baseline vs Skill vs Skill+Tools).
8. **Mistake Analysis** [A13 Mistake Analyst]: Triage eval results and ledger maintenance.
9. **Constitutional Audit & Gate** [A14 Reviewer]: GO/NO-GO audit report.
