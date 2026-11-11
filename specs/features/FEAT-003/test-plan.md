# Test Plan: FEAT-003

## 1. CLI Unit Tests (`eval/unit/test_cli.py`)
- Execute `bhashabid number 99` -> outputs `নিরানব্বই`.
- Execute `bhashabid number 1234567 --format grouped` -> outputs `১২,৩৪,৫৬৭`.
- Execute `bhashabid normalize "রেলষ্টেশন."` -> outputs `রেলস্টেশন।`.
- Execute `bhashabid lint "তুমি সিদ্ধান্ত নেন" --json` -> outputs structured JSON diagnostics with exit code 1.
- Clean text produces exit code 0.

## 2. Adapter Tests (`eval/unit/test_adapters.py`)
- Verify `.cursorrules` exists and contains core Bangla Academy orthography constraints.
- Verify `claude_system_prompt.txt` token count < 500 tokens.

## 3. Packaging Validation
- Verify `pyproject.toml` metadata, dependencies, and entrypoints.
