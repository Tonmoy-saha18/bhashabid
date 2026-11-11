# Bhashabid System Requirements (02-requirements.md)

Requirements are specified in EARS (Easy Approach to Requirements Syntax) format:
`[Trigger / Condition], the system shall [Action] [Object] [Criteria].`

## 1. Numerals, Digits & Quantities (REQ-001 - REQ-015)

- **REQ-001**: When provided an integer from 0 to 99, the `bn_numbers` engine shall return the exact irregular Bengali word spelling (e.g., 0 -> শূন্য, 1 -> এক, 99 -> নিরানব্বই).
- **REQ-002**: When provided a positive integer >= 100, the `bn_numbers` engine shall format numbers using South Asian grouping (লক্ষণীয়: কমা বিভাজন ১২,৩৪,৫৬৭).
- **REQ-003**: When converting numbers >= 100 to words, the system shall express values in শত/শো, হাজার, লাখ/লক্ষ, and কোটি according to the selected profile.
- **REQ-004**: When provided a floating point number, the system shall read the decimal portion digit-by-digit using "দশমিক" (e.g., ৩.১৪ -> তিন দশমিক এক চার).
- **REQ-005**: When converting fractions to Bengali words, the system shall support standard fractional prefixes: সোয়া (1/4 above integer), দেড় (1.5), আড়াই (2.5), সাড়ে (>= 3.5), and পৌনে (1/4 below integer).
- **REQ-006**: When formatting monetary values, the system shall suffix or prefix with "টাকা" and convert decimal portions to "পয়সা" (e.g., 50.25 -> পঞ্চাশ টাকা পঁচিশ পয়সা).
- **REQ-007**: When given a number in Gregorian calendar context, the system shall format the day using conventional date ordinals (১লা, ২রা, ৩রা, ৪ঠা, ৫ই ... ৩১শে).
- **REQ-008**: When formatting general ordinals, the system shall output classical ordinals (প্রথম, দ্বিতীয়, তৃতীয়, চতুর্থ, পঞ্চম, ... দশম, একাদশ, দ্বাদশ).
- **REQ-009**: When given English ASCII digits (0-9), the system shall convert them to Bengali digits (০-৯) deterministically.
- **REQ-010**: When given Bengali digits (০-৯), the system shall convert them to English ASCII digits (0-9) deterministically.
- **REQ-011**: When a style profile specifies "bd_standard", the number 500 shall format to "পাঁচশত" or "পাঁচশো" as designated by the profile parameter without ambiguous mixing.
- **REQ-012**: When converting negative numbers to words, the system shall prepend "মাইনাস" or "ঋণাত্মক" based on the domain parameter.
- **REQ-013**: When provided an integer >= 10,000,000 (1 crore), the system shall compound crores recursively (e.g., ১০০ কোটি).
- **REQ-014**: When numbers are accompanied by Bengali classifiers (-টা, -টি, -খানা, -জন), the system shall maintain appropriate spacing and phonetic harmony.
- **REQ-015**: When an invalid or out-of-range numeric string is input, the engine shall raise a structured `InvalidNumberError` with informative diagnostics.

## 2. Orthography, Unicode & Normalization (REQ-016 - REQ-025)

- **REQ-016**: When processing any raw Bengali string, the normalizer shall normalize Unicode to NFC standard form.
- **REQ-017**: When encountering composite characters for য় (য + ় U+09BC), the normalizer shall canonicalize to U+09DF.
- **REQ-018**: When encountering composite characters for ড় (ড + ়) and ঢ় (ঢ + ়), the normalizer shall canonicalize to U+095C and U+095D.
- **REQ-019**: When encountering inappropriate Zero Width Joiner (ZWJ) or Zero Width Non-Joiner (ZWNJ), the normalizer shall strip unnecessary invisible codepoints while preserving valid conjuncts (য-ফলা, র-ফলা).
- **REQ-020**: When standardizing punctuation, the normalizer shall replace ASCII full stops (`.`) terminating Bengali sentences with the Bengali Dari (`।`, U+0964).
- **REQ-021**: When the Bangladesh Standard profile is active, foreign loanwords with /s/ shall use দন্ত্য-স (`স`) instead of মূর্ধন্য-ষ (`ষ`) according to Bangla Academy rules.
- **REQ-022**: When normalizing tatbhava/desi words, the system shall enforce হ্রস্ব-ই (`ি`) and হ্রস্ব-উ (`ু`) over দীর্ঘ-ঈ/দীর্ঘ-ঊ in accordance with modern orthography.
- **REQ-023**: When detecting the Khanda-ta (`ৎ`, U+09CE), the normalizer shall preserve it where etymologically required and reject invalid substitution with `ত্`.
- **REQ-024**: When processing whitespace, multiple consecutive spaces shall be collapsed without altering line breaks.
- **REQ-025**: When Bengali quotation marks are processed, ASCII quotes shall be converted to appropriate directional curly quotes.

## 3. Grammar, Registers & Syntactic Agreement (REQ-026 - REQ-035)

- **REQ-026**: When Cholito (চলিত) style is configured, the system shall prohibit Sadhu verb forms (e.g., prohibit করিয়াছিল in favor of করেছিল).
- **REQ-027**: When Sadhu (সাধু) style is configured, the system shall preserve archaic verb suffixes and full pronouns (তাহার, ইহারা, বলিয়া).
- **REQ-028**: When the honorific pronoun "আপনি" is used as subject, the predicate verb shall take the formal suffix (e.g., -েন: আপনি করেন / গেছেন).
- **REQ-029**: When the familiar pronoun "তুমি" is used as subject, the predicate verb shall take the familiar suffix (e.g., -ো: তুমি করো / গেছো).
- **REQ-030**: When the intimate/inferior pronoun "তুই" is used as subject, the predicate verb shall take the intimate suffix (e.g., -িস/-লি: তুই করিস / গেলি).
- **REQ-031**: When human referents are counted, the classifier "-জন" shall be preferred over "-টা".
- **REQ-032**: When translating English passive structures, the system shall default to natural Bengali active or ergative constructions rather than unnatural "দ্বারা" calques.
- **REQ-033**: When constructing declarative sentences, the system shall enforce Subject-Object-Verb (SOV) baseline order while permitting pragmatic topicalization.
- **REQ-034**: When postpositions (দিয়ে, জন্য, থেকে, কাছে) are attached to nouns/pronouns, the preceding word shall take the appropriate genitive or oblique case marker (-এর / -র).
- **REQ-035**: When double negatives or unnatural calques occur (e.g., "আমি এটা করতে পারি না কারণ..."), the system shall suggest authentic Bengali clause structures.

## 4. Skill Architecture, Evaluation & Memory (REQ-036 - REQ-040)

- **REQ-036**: The skill root file `skills/bangla-expert/SKILL.md` shall not exceed 600 tokens in size.
- **REQ-037**: When an agent encounters an evaluation failure, the Mistake Analyst shall append a structured record to `memory/mistakes/ledger.jsonl`.
- **REQ-038**: Every resolved mistake in the ledger shall have a corresponding unit or regression test reference in `eval/unit/`.
- **REQ-039**: The evaluation suite shall execute comparisons across at least 3 distinct model configurations (e.g., Baseline vs Skill vs Skill+Tools).
- **REQ-040**: The system shall halt all execution loops immediately upon detection of the file `state/STOP`.
