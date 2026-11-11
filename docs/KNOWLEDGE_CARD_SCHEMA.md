# Knowledge Card Schema Specification (KNOWLEDGE_CARD_SCHEMA.md)

All linguistic knowledge cards stored under `knowledge/cards/` must be structured YAML files complying with this specification.

## Schema Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique identifier (e.g., `CRD-NUM-001`, `CRD-GRM-005`). |
| `title` | string | Yes | Clear descriptive title in English and Bengali. |
| `domain` | enum | Yes | One of: `numerals`, `orthography`, `grammar`, `register`, `idioms`, `translation`. |
| `profile` | enum | Yes | One of: `all`, `bd_standard`, `wb_standard`. |
| `register` | enum | Yes | One of: `all`, `sadhu`, `cholito`, `formal`, `conversational`, `literary`. |
| `rule_summary` | string | Yes | Concise linguistic explanation of the rule or pattern. |
| `good_examples` | list[string] | Yes | At least 2 authentic, correct Bengali phrases/sentences. |
| `bad_examples` | list[string] | Yes | At least 2 incorrect phrases showing the typical error. |
| `common_llm_error` | string | Yes | Specific analysis of why LLMs frequently fail at this pattern. |
| `sources` | list[string] | Yes | Bibliographic or lexicographic citations (author, work, section/URL). |
| `confidence` | enum | Yes | One of: `llm-hypothesis`, `data-supported`, `reviewed`. |
| `created_date` | string | Yes | ISO 8601 date (YYYY-MM-DD). |
| `last_modified` | string | Yes | ISO 8601 date (YYYY-MM-DD). |

## Sample Card YAML

```yaml
id: CRD-NUM-001
title: "Irregular Bengali Cardinal Numbers 0-99 (০-৯৯ অনিয়মিত সংখ্যা)"
domain: numerals
profile: bd_standard
register: all
rule_summary: "Numbers 0 through 99 in Bengali do not follow a simple positional decimal compounding system. Each number from 1 to 99 has an irregular, phonetically evolved spelling defined by Bangla Academy standard orthography."
good_examples:
  - "৯৯ = নিরানব্বই"
  - "৭৫ = পঁচাত্তর"
  - "৮৩ = তিরাশি"
bad_examples:
  - "৯৯ = নয়-দশ-নয় (Calqued positional assembly)"
  - "৭৫ = পাঁচ-সত্তর (Invalid morphological compounding)"
common_llm_error: "LLMs attempt to compose 2-digit numbers by joining tens and ones words naively, producing unnatural non-existent Bengali words."
sources:
  - "Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1 & 2), 2012"
  - "Samsad Bengali-English Dictionary (6th Ed.)"
confidence: data-supported
created_date: 2026-11-11
last_modified: 2026-11-11
```
