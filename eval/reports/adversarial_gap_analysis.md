# Bhashabid Stress-Test & Adversarial Gap Analysis Report

## Executive Summary
This adversarial session audited Bhashabid against real-world, complex journalistic texts from **The Business Standard (TBS)**, **The Daily Star**, and **Prothom Alo** across 4 specialized domains:
1. Diplomatic & Political Reporting (relative clause nesting & diplomatic idioms)
2. Macroeconomic & Inflation Statistics (percentage syntax, policy rates, basis points)
3. High Court Judicial Reporting (Rule Nisi show-cause formulas)
4. Sports Reporting (sports terminology, avoiding defeat calques)

---

## 1. Where the Raw Baseline LLM Completely Breaks Down

| Test Case | Domain | Raw LLM Pathology | Bhashabid Solution |
|---|---|---|---|
| **STRESS-01** | Diplomatic | Literal English relative clauses: `"যা ১৯৭১ সালের মুক্তিযুদ্ধের সময় থেকে শুরু হয়েছিল"` | Natural participial clause: `"১৯৭১ সালের মহান মুক্তিযুদ্ধের সময় থেকে শুরু হওয়া..."` |
| **STRESS-02** | Economics | Passive calque: `"খাদ্যমূল্য বৃদ্ধির দ্বারা চালিত"` and overusing `%` signs | Active syntax: `"খাদ্যপণ্যের মূল্যবৃদ্ধির কারণে"` and idiomatic `"শতাংশ"` |
| **STRESS-03** | Judicial | Catastrophic legal calque: `"বেআইনি ঘোষণা করা উচিত নয় তা জিজ্ঞেস করে"` | Authentic Bangladeshi legal formula: `"কেন বেআইনি ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন"` |
| **STRESS-04** | Sports | Clumsy translation of sports idioms: `"পরাজয় স্বীকার করেছে"` and `"সফরকারীদের বিরুদ্ধে"` | Authentic sports vernacular: `"সফরকারীদের কাছে ৫ উইকেটে হেরেছে"` and `"লড়াকু অর্ধশতক"` |

---

## 2. Brutal Self-Audit: Remaining Skill Weaknesses & Gaps

Even with our current skill and tools, rigorous inspection reveals **three clear limitations/weaknesses**:

### Gap 1: Formulaic Judicial Phrasing (Rule Nisi)
- **Weakness**: In legal journalism, High Court show-cause orders follow a strict, ritualized syntactic template:
  `"[বিষয়বস্তু] কেন [আইনগত ফলাফল] হবে না, তা জানতে চেয়ে রুল জারি করেছেন হাইকোর্ট।"`
- **LLM Tendency**: Models translate *"asking why... should not be declared illegal"* into conversational prose (*"জিজ্ঞেস করে"*), destroying legal register.
- **Remedy**: Create a dedicated knowledge card `CRD-TRN-002` (Judicial & High Court Reporting Idioms) and add legal formula patterns to `tools/bn_lint/`.

### Gap 2: Economic & Financial Terminology (TBS Style Guide)
- **Weakness**: English terms like *"basis points"*, *"policy rate"*, *"repo rate"*, *"concessionary loan"*, *"fiscal deficit"* are frequently mis-translated or inconsistently transliterated.
- **LLM Tendency**: Using `"দ্বারা চালিত"` for *"driven by"*, or transliterating *"basis points"* as *"বেসিস পয়েন্ট"* without standard context.
- **Remedy**: Create knowledge card `CRD-TRN-003` (Financial & Macroeconomic Reporting Guidelines) and expand dictionary.

### Gap 3: Sports Vernacular Calques
- **Weakness**: Translating *"conceded a defeat"* as *"পরাজয় স্বীকার করেছে"* (which sounds like an army surrendering in a war, not a cricket match!).
- **Remedy**: Create knowledge card `CRD-TRN-004` (Sports Journalism & Action Verbs).

---

## 3. Systematic Action Plan (Converting Identified Gaps into Capabilities)
1. **Log Mistakes in Ledger**: Log `MST-0006` (Judicial Rule Nisi calque) and `MST-0007` (Sports defeat calque).
2. **Author New Knowledge Cards**:
   - `CRD-TRN-002.yaml`: Judicial & Court Reporting Formulas
   - `CRD-TRN-003.yaml`: Financial & Business News Syntax
   - `CRD-TRN-004.yaml`: Sports Vernacular & Action Verbs
3. **Upgrade `tools/bn_lint`**: Add rules to flag `জিজ্ঞেস করে রুল` and `পরাজয় স্বীকার করেছে`.
4. **Add Regression Tests**: Guarantee these 4 news domains pass 100%.
