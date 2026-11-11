# Test Plan: FEAT-004

## 1. Dialect Profile Tests (`eval/unit/test_dialect_profiles.py`)
- In `bd_standard`: numbers default to `শত`, loanwords use `স`/`স্ট`.
- In `wb_standard`: numbers support `শো`, `লক্ষ`, `কুড়ি`, and regional variations.
- Switching profile parameter alters output predictably.

## 2. Batch Normalizer Tests (`eval/unit/test_batch_normalizer.py`)
- Stream 1,000 lines through `BatchNormalizer`.
- Verify metric counts: words processed, corrections made, elapsed time > 0, throughput > 10,000 words/sec.

## 3. Human Review Packet Tests (`eval/unit/test_review_packet.py`)
- Verify all cards in `knowledge/cards/` are indexed in the packet.
- Verify confidence labels remain `data-supported` (strictly enforcing Principle P2).
