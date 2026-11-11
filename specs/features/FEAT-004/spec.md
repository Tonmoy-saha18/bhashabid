# Feature Specification: FEAT-004 (Regional Dialect Profiles, Batch Pipeline & Human Review Liaison)

## 1. Overview
FEAT-004 introduces parameterized regional dialect profiles for Bangladesh (`bd_standard`) and West Bengal (`wb_standard`), a high-throughput streaming batch normalizer (`pipeline/03_process/`), an automated corpus evaluation runner (`pipeline/04_eval/`), and the Human Review Liaison packet system (`docs/review_queue/`) managed by Agent A15.

## 2. Requirements Addressed
- **REQ-011 & P5**: Parameterized regional profiles (`bd_standard` vs `wb_standard`) for numerals and orthography without guessing.
- **P2 & P3**: Provenance, human review liaison workflow, and licensed corpus batching.
- **REQ-039**: Batch metric accounting and throughput profiling.

## 3. Interfaces & Contracts
`bn_normalize.normalize(text: str, profile: str = "bd_standard" | "wb_standard")`
`pipeline.03_process.batch_normalizer.BatchNormalizer.process_stream(lines: Iterable[str]) -> BatchResult`
`tools.review_packet_generator.generate_review_packet() -> str`
