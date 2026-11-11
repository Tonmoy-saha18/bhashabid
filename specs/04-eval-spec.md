# Bhashabid Evaluation Specification (04-eval-spec.md)

## 1. Evaluation Matrix & Task Families

The Bhashabid evaluation engine tests linguistic performance across distinct task dimensions:

| Task ID | Task Family | Description | Primary Metric | Target Baseline |
|---|---|---|---|---|
| EV-NUM | Numerals & Digits | 0-99 conversion, lakh/crore, decimals, ordinals, fractions | Exact Match (100%) | 100% |
| EV-ORTH | Orthography & Unicode | NFC canonicalization, Dari punctuation, য়/ড়/ঢ় cleanup | Exact Match (100%) | 100% |
| EV-REG | Register Consistency | Sadhu/Cholito separation, honorific agreement | Defect Rate (0) | 0 violations |
| EV-TRANS | Translation (EN <-> BN) | Literary, technical, news articles | chrF++ / COMET | >= 25% lift |
| EV-CORR | Flawed Bengali Correction | Spotting spelling, syntax, and calque flaws | Precision / Recall | F1 >= 0.90 |
| EV-GEN | Natural Article Writing | Writing coherent prose from scratch | Rubric (1-5) | Average >= 4.5 |

## 2. Proposed Exit Criteria & Thresholds for "Ready"

Before any major release or milestone is approved, the following quantitative gates must be passed:

1. **Deterministic Tools**:
   - `eval/unit/test_bn_numbers.py`: **100.0%** passing (exhaustive 0-99 tests, boundary values, negative numbers, fractions).
   - `eval/unit/test_bn_normalize.py`: **100.0%** passing.
   - P0/P1 Open Defects: **0**.

2. **Benchmark Quality**:
   - Statistically significant improvement ($p < 0.05$) comparing `Model + Skill + Tools` versus `Baseline Model` across >= 3 model architectures.
   - Regression on held-out test set: **< 1.0%**.

3. **Knowledge Coverage**:
   - 100% of knowledge cards must cite documented bibliographic or lexicographic sources.
   - Zero cards marked `reviewed` without recorded human verification.

4. **Mistake Loop Health**:
   - 100% of resolved ledger mistakes (`memory/mistakes/ledger.jsonl`) must have active automated regression tests in `eval/unit/`.

## 3. Data Split Policy
- **Dev Set (60%)**: Used during build cycles for prompt and rule tuning.
- **Test Set (20%)**: Used by the QA and Evaluator agents to gate candidate branches.
- **Hidden Holdout (20%)**: Stored separately, never exposed to generative prompts, reserved solely for release audits by A14.
