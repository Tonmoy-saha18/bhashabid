# memory/lessons/LES-002_bidirectional_honorific_repair.md
# Lesson LES-002: Bidirectional Honorific Repair Strategy

## 1. Context & Mistake Reference
- Linked Mistake: `MST-0005`
- Linked Requirements: `REQ-028`, `REQ-029`, `REQ-030`
- Relevant Tool: `tools/bn_lint/honorifics.py`
- Relevant Knowledge Card: `CRD-GRM-002`

## 2. Linguistic Principle: Ambiguity of Repair Direction
When an LLM produces an honorific agreement clash such as:
`তুমি সিদ্ধান্ত নেন` (Subject = Familiar 'তুমি', Verb = Formal 'নেন')

There are always **two equally valid linguistic repair directions** depending on the intended social register of the speaker:
1. **Verb Adjustment (Preserve Familiar Register)**:
   Change the predicate verb to agree with the subject pronoun:
   `তুমি সিদ্ধান্ত নেন` -> **`তুমি সিদ্ধান্ত নাও`**
2. **Pronoun Adjustment (Preserve Formal Register)**:
   Change the subject pronoun to agree with the predicate verb:
   `তুমি সিদ্ধান্ত নেন` -> **`আপনি সিদ্ধান্ত নেন`**

## 3. Engineering Invariant
A passive lint warning that only mentions grammatical rules (e.g., "Use -েন suffix") forces the downstream agent or user to guess how to fix the sentence.
*Invariant Rule*: Whenever an honorific clash is detected, the linter must synthesize and provide **both concrete rewrites**:
- `Option 1 (Verb Adjustment)`
- `Option 2 (Pronoun Adjustment)`
This enables the autonomous agent to choose the path matching its target register profile (`formal` vs `conversational`).
