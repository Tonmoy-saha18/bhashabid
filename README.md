# Bhashabid (ভাষাবিদ)

> An open-source, spec-driven Bengali linguistic engine, deterministic toolset, evaluation matrix, and progressive skill for AI agents.

## Overview / সংক্ষিপ্ত পরিচিতি

**Bhashabid** (ভাষাবিদ - "The Bengali Linguist") empowers any AI assistant, LLM, or autonomous agent to write, translate, edit, and evaluate authentic Bengali (বাংলা) prose. It solves common LLM pathologies in Bengali:
- Digit / numeral errors and non-standard grouping
- Sadhu (সাধু) / Cholito (চলিত) pronoun and verbal mixing
- Honorific mismatch (তুই / তুমি / আপনি)
- English calques, literal translations, and syntactic distortion
- Unicode and orthographic irregularities (e.g., য় vs ড় vs ঢ়, ZWJ/ZWNJ, খণ্ড ত ৎ)

### Key Architectural Pillars
1. **Deterministic Tools**: Python/Rust native rules for number words, formatting, NFC normalization, date conversion, and linting.
2. **Progressive Skill Layer**: Minimal token footprint `SKILL.md` routing to modular reference guides on demand.
3. **Evidence-Driven Memory**: Rigorous mistake ledger (`memory/mistakes/ledger.jsonl`) converting failures into automated regression tests.
4. **Multi-Register Profiles**: Seamlessly configure Bangladesh standard (Bangla Academy), West Bengal orthography, formal news, academic, literary fiction, or conversational styles.

---

## প্রকল্প বিবরণ (বাংলা)

ভাষাবিদ (Bhashabid) হলো একটি উন্মুক্ত কৃত্রিম বুদ্ধিমত্তা সহায়তা ফ্রেমওয়ার্ক, যা যেকোনো বৃহৎ ভাষিক মডেলকে (LLM) শুদ্ধ, সাবলীল ও ব্যাকরণসম্মত প্রমিত বাংলা রচনা, অনুবাদ ও সম্পাদনায় সক্ষম করে তোলে।

### প্রধান সুবিধাসমূহ
- **সংখ্যা ও গণন রূপান্তর**: ০-৯৯ অনিয়মিত সংখ্যা বানান, লক্ষ-কোটি হিসাব, ভগ্নাংশ (দেড়, আড়াই, সোয়া, পৌনে), মুদ্রা ও তারিখের প্রমিত রূপান্তর।
- **বানান ও ইউনিকোড প্রমিতকরণ**: বাংলা একাডেমি প্রমিত বানানরীতি এবং ইউনিকোড NFC প্রক্রিয়াকরণ।
- **সর্বনাম ও ক্রিয়া সঙ্গতি**: সর্বনামের মর্যাদাভেদ (আপনি/তুমি/তুই) এবং ক্রিয়াপদের সঙ্গতি রক্ষা।
- **ভ্রান্তি থেকে শিক্ষা**: স্বয়ংক্রিয় রিগ্রেশন টেস্টের মাধ্যমে মডেলের পৌনঃপুনিক ভুল শনাক্তকরণ ও সংশোধন।

---

## Repository Structure

```
bhashabid/
├── specs/          # Formal EARS requirements, eval specs, and constitution
├── agents/         # 15 BMAD-style specialized agent contracts
├── state/          # Real-time lifecycle state, backlog, and budget
├── memory/         # Mistake ledgers, lessons learned, and decisions
├── tools/          # Deterministic Python tools (bn_numbers, bn_normalize, etc.)
├── skills/         # Progressive skill definitions (skills/bangla-expert/)
└── eval/           # Unit tests, benchmarks, rubrics, and holdouts
```

## Quick Start

```bash
# Clone the repository
git clone https://github.com/bhashabid/bhashabid.git
cd bhashabid

# Run test suite
python -m unittest discover -s eval/unit
```

## License
Code: Apache-2.0  
Knowledge Base & Text: CC BY-SA 4.0
