# Test Plan: FEAT-002

## 1. Linter Unit Tests (`eval/unit/test_bn_lint.py`)
- Detect Guru-chandali mixing when Sadhu verbs (e.g. `করিয়াছিল`, `আসিয়া`) appear with Cholito verbs (`গেছে`, `বলল`).
- Detect Honorific clash when subject pronoun and verb inflection clash (`আপনি করো`, `তুমি করেন`).
- Detect unnatural passive English calques (`দ্বারা কৃত`, `দ্বারা চালিত`).
- Clean texts produce 0 warnings.

## 2. MCP Server Tests (`eval/unit/test_mcp_server.py`)
- Tool discovery endpoint lists `convert_number`, `normalize_text`, and `lint_text`.
- Calling `convert_number` with `{"number": 99}` returns `{"words": "নিরানব্বই"}`.
- Calling `normalize_text` with `{"text": "রেলষ্টেশন."}` returns `{"normalized": "রেলস্টেশন।"}`.
- Calling `lint_text` with flawed text returns structured diagnostics.

## 3. Knowledge Cards Schema Validation
- All new cards validate against schema with source attribution.
