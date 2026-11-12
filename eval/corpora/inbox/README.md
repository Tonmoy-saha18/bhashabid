# Autonomous Ingestion Inbox (`eval/corpora/inbox/`)

Drop any new raw Bengali text files (`.txt`, `.jsonl`, `.md`, news transcripts, court judgments, circulars) into this directory.

The autonomous learning engine (`tools/corpus_harvester.py` and `tools/daily_practice_runner.py`) will automatically:
1. Detect newly dropped files.
2. Tokenize them into sentences while protecting decimals, abbreviations, and citations.
3. Audit them across all 11 professional sectors and linters.
4. Flag novel anomalies and synthesize candidate draft cards into `knowledge/cards/drafts/`.
5. Update `docs/review_queue/PENDING_REVIEWS.md` for human review.
