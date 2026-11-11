# Expert Linguistic Review Packet (Review Packet #001)

Prepared by: **Agent A15 (Human Review Liaison)**  
Target Reviewers: **Native Bengali Linguistic Experts**  
Standard: **Bangla Academy (Dhaka) & Paschimbanga Bangla Akademi (Kolkata)**  

> [!IMPORTANT]
> In accordance with Principle P2 of the Bhashabid Constitution, agents may NEVER mark knowledge cards as 'reviewed'. Only recorded, signed human native-speaker reviews may elevate card confidence from `data-supported` to `reviewed`.

---

## Instructions for Human Reviewers
1. Verify the linguistic validity of each rule summary, positive examples, and counter-examples.
2. Check for regional balance across Bangladesh standard and West Bengal conventions.
3. Provide sign-off handle, affiliation, and status: `APPROVED` | `NEEDS_REVISION` | `REJECTED`.

---

## Review Queue Cards

### Card 1: [CRD-GRM-001] Sadhu-Cholito Verb Consistency (গুরুচণ্ডালী দোষ পরিহার)
- **Domain**: `grammar` | **Profile**: `all` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Bengali prose must maintain strict stylistic consistency between Sadhu (সাধু) and Cholito (চলিত) registers. Mixing Sadhu verb forms (e.g. করিয়াছিলেন, যাইবে) with Cholito forms (e.g. করেছেন, যাবে) within the same discourse is a cardinal stylistic defect known as Guru-chandali Dosh.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ তিনি কাজটি করেছিলেন এবং বাড়ি ফিরেছিলেন। (বিশুদ্ধ চলিত)
  - ✓ তিনি কার্যটি করিয়াছিলেন এবং গৃহে ফিরিয়াছিলেন। (বিশুদ্ধ সাধু)

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ তিনি কাজটি করিয়াছিলেন এবং বাড়ি ফিরেছিলেন। (মিশ্রিত / গুরুচণ্ডালী)
  - ✗ আমরা সেখানে যাব এবং আহার গ্রহণ করিব। (মিশ্রিত)

**Common LLM Error**: LLMs switch between Sadhu and Cholito verb suffixes midway through complex compound sentences due to inconsistent context attention.
**Sources / Citations**: Suniti Kumar Chatterji, The Origin and Development of the Bengali Language, 1926, Bangla Academy Promito Bangla Bhashar Byakoron, Vol 1

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 2: [CRD-GRM-002] Honorific Concordance Across Pronouns and Verbs (আপনি / তুমি / তুই)
- **Domain**: `grammar` | **Profile**: `all` | **Register**: `all`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Bengali pronouns possess a three-tier honorific system that strictly governs verbal inflection: formal (আপনি -> -েন/-বেন), familiar (তুমি -> -ো/-বে), and intimate/inferior (তুই -> -িস/-বি). Clashing pronoun honorific with inappropriate verb ending is a severe grammatical violation.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ আপনি কেমন আছেন? (Formal)
  - ✓ তুমি কেমন আছো? (Familiar)
  - ✓ তুই কেমন আছিস? (Intimate)

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ আপনি কেমন আছো? (Severe honorific clash)
  - ✗ তুমি কেমন আছেন? (Incongruent agreement)
  - ✗ আপনি কি সেখানে যাবি? (Mixed registers)

**Common LLM Error**: When responding to polite prompts, LLMs frequently address the user as আপনি but inflect verbs in familiar তুমি form (e.g. আপনি কি এটা দেখতে পারো?).
**Sources / Citations**: Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1: Sarbanamer Prayog)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 3: [CRD-GRM-003] Bengali Case Markers and Postposition Agreement (কারক ও বিভক্তি)
- **Domain**: `grammar` | **Profile**: `all` | **Register**: `all`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Bengali nominals take overt inflectional case suffixes (বিভক্তি) such as -এর/-র (genitive), -কে/-রে (accusative/dative), and -এ/-তে/-য়ে (locative). When governed by postpositions (জন্য, কাছে, থেকে, দ্বারা), the preceding noun or pronoun must assume the required oblique or genitive form.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ তার জন্য অপেক্ষা করছি (Genitive + postposition)
  - ✓ নদীতে অনেক মাছ আছে (Locative -তে)

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ সে জন্য অপেক্ষা করছি (Missing genitive marker on pronoun)
  - ✗ নদী মধ্যে অনেক মাছ (Awkward missing locative)

**Common LLM Error**: LLMs translate English prepositions ('for him') by combining bare nominative pronouns with postpositions (e.g. তিনি জন্য instead of তাঁর জন্য).
**Sources / Citations**: Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1: Karok o Bibhokti)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 4: [CRD-GRM-004] Bengali Euphonic Junctions (সন্ধি: স্বরসন্ধি ও ব্যঞ্জনসন্ধি)
- **Domain**: `grammar` | **Profile**: `all` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Sandhi joins adjacent sounds across morpheme boundaries. In Tatsama words, Sanskrit sandhi governs combinations (বিদ্যা + আলয় = বিদ্যালয়, পরি + ঈক্ষা = পরীক্ষা). In native Bengali words (খাঁটি বাংলা সন্ধি), phonetic assimilation is natural and non-pedantic (পাঁচ + জন = পাঁচজন).

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ সূর্য + উদয় = সূর্যোদয়
  - ✓ দিক + অন্ত = দিগন্ত

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ সূর্য্য উদয় (Unjoined tatsama compound where sandhi is expected)
  - ✗ পরীখ্যা (Misspelled vowel sandhi)

**Common LLM Error**: LLMs fail to apply regular sandhi in formal and academic compounds, resulting in disjointed or erroneously spelled root words.
**Sources / Citations**: Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1: Sandhi)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 5: [CRD-GRM-005] Bengali Compound Formation (সমাস: দ্বন্দ্ব, দ্বিগু, তৎপুরুষ ও কর্মধারয়)
- **Domain**: `grammar` | **Profile**: `all` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Samas condenses multi-word syntactic phrases (ব্যাসবাক্য) into single compound words (সমস্তপদ). Major types: Dwandwa (মা ও বাবা = মা-বাবা), Tatpurush (রাজার পুত্র = রাজপুত্র), Karmadharaya (নীল যে পদ্ম = নীলপদ্ম), and Bahubrihi (দশ আনন যার = দশানন).

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ পিতা-মাতা (দ্বন্দ্ব সমাস)
  - ✓ স্মৃতিসৌধ (স্মৃতিরক্ষার্থে সৌধ - মধ্যপদলোপী কর্মধারয়)

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ পিতা এবং মাতা (Uncondensed in formal administrative contexts)

**Common LLM Error**: LLMs often generate overly verbose periphrastic explanations where concise standard compound words exist.
**Sources / Citations**: Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1: Samas)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 6: [CRD-NUM-001] Irregular Bengali Cardinal Numbers 0-99 (০-৯৯ অনিয়মিত সংখ্যা)
- **Domain**: `numerals` | **Profile**: `bd_standard` | **Register**: `all`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Numbers 0 through 99 in Bengali do not follow a simple positional decimal compounding system. Each number from 1 to 99 has an irregular, phonetically evolved spelling defined by Bangla Academy standard orthography.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ ৯৯ = নিরানব্বই
  - ✓ ৭৫ = পঁচাত্তর
  - ✓ ৮৩ = তিরাশি

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ ৯৯ = নয়-দশ-নয়
  - ✗ ৭৫ = পাঁচ-সত্তর

**Common LLM Error**: LLMs attempt to compose 2-digit numbers by joining tens and ones words naively, producing unnatural non-existent Bengali words.
**Sources / Citations**: Bangla Academy Promito Bangla Bhashar Byakoron (Vol 1 & 2), 2012, Samsad Bengali-English Dictionary (6th Ed.)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 7: [CRD-ORT-001] Unicode NFC Canonicalization and Composite Graphemes (য়, ড়, ঢ়)
- **Domain**: `orthography` | **Profile**: `all` | **Register**: `all`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Bengali Unicode text must always be canonicalized to NFC form. In particular, composite sequences like য + ় (U+09BC) must be normalized to U+09DF (য়), ড + ় to U+09DC (ড়), and ঢ + ় to U+09DD (ঢ়) to prevent broken rendering, indexing failures, and search mismatch.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বইটি ভালো হয়েছে (with precomposed U+09DF)
  - ✓ বড় গাছটি দাঁড়িয়ে আছে (with precomposed U+09DC and U+095D)

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ বইটি ভালো হয়েছে (using decomposed য + ়)
  - ✗ বড় গাছটি (using decomposed ড + ়)

**Common LLM Error**: Language models randomly emit decomposed Nukta forms depending on tokenization, causing broken rendering on mobile and web viewports.
**Sources / Citations**: Unicode Standard Version 15.0 - Bengali Block, Bangla Academy Promito Bangla Banan Riti, 2012

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 8: [CRD-ORT-002] Bangla Academy Loanword S-Rule (বিদেশি শব্দে 'স' বনাম 'ষ')
- **Domain**: `orthography` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: In the Bangladesh Standard (Bangla Academy) orthography, foreign loanwords (English, Persian, Arabic) with /s/ or /ʃ/ must use দন্ত্য-স ('স') or তালব্য-শ ('শ') based on phonetic convention, and NEVER মূর্ধন্য-ষ ('ষ'). Consequently, combinations like 'ষ্ট' or 'ষ্ঠ' in English loanwords are errors for 'স্ট'.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ তিনি রেলস্টেশনে অপেক্ষা করছেন।
  - ✓ চিঠিটি ডাকযোগে পোস্ট করা হয়েছে।
  - ✓ প্রধান মাস্টারমশাই বিদ্যালয়ে এলেন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ তিনি রেলষ্টেশনে অপেক্ষা করছেন।
  - ✗ চিঠিটি ডাকযোগে পোষ্ট করা হয়েছে।
  - ✗ প্রধান মাষ্টারমশাই বিদ্যালয়ে এলেন।

**Common LLM Error**: LLMs carry over archaic 19th-century Sanskrit sandhi rules to modern English loanwords, incorrectly generating ষ্টেশন, পোষ্ট, মাষ্টার.
**Sources / Citations**: Bangla Academy Promito Bangla Banan Riti (Clause 2.01, Foreign Loanwords), 2012

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 9: [CRD-ORT-003] Regional Orthographic Variations (বাংলাদেশ প্রমিত বনাম পশ্চিমবঙ্গ বানানরীতি)
- **Domain**: `orthography` | **Profile**: `all` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: While core Sanskrit grammar is identical, modern standard Bengali possesses systematic regional orthographic variations between the Bangla Academy (Dhaka) standard and Paschimbanga Bangla Akademi (Kolkata) standard. Bangla Academy strictly enforces short-vowel ি (পাখি, হাতি, শাড়ি, বাড়ি, সরকারি, জাপানি) and loanword স (স্টেশন, মাস্টার). West Bengal orthography broadly accepts these but permits traditional tatbhava spellings in literature and prefers specific numeral variants (পাঁচশো, কুড়ি).

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বাংলাদেশ রীতি: তিনি রেলস্টেশনে অপেক্ষা করছেন এবং পাঁচশত টাকা জমা দিলেন।
  - ✓ পশ্চিমবঙ্গ রীতি: তিনি রেলস্টেশনে অপেক্ষা করছেন এবং পাঁচশো টাকা জমা দিলেন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ রেলষ্টেশনে পাঁচ শত (Inconsistent mixing without explicit profile)

**Common LLM Error**: LLMs guess regional variants randomly within the same paragraph, mixing পাঁচশত and পাঁচশো arbitrarily.
**Sources / Citations**: Bangla Academy Promito Bangla Banan Riti (2012), Paschimbanga Bangla Akademi Banan Bidhi (2000)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 10: [CRD-TRN-001] Translation Idioms vs Literal English Calques (ভাবানুবাদ বনাম আক্ষরিক অনুবাদ)
- **Domain**: `translation` | **Profile**: `all` | **Register**: `all`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Idiomatic expressions, proverbs, and metaphors must be translated by cultural equivalent (ভাবানুবাদ), never by literal word-for-word calque. Passive English sentences ('The road was inaugurated by the mayor') should be converted to active Bengali sentences ('মেয়র মহোদয় রাস্তাটি উদ্বোধন করলেন').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ Actions speak louder than words -> কথার চেয়ে কাজের মূল্য বেশি।
  - ✓ Piece of cake -> অত্যন্ত সহজ কাজ / জলভাত।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ Actions speak louder than words -> কাজ শব্দের চেয়ে জোরে কথা বলে।
  - ✗ Piece of cake -> এক টুকরো কেক।

**Common LLM Error**: LLMs transcribe English idioms word-by-word into nonsensical Bengali phrases.
**Sources / Citations**: Bangla Academy Bengali-English & English-Bengali Dictionary

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 11: [CRD-TRN-002] High Court & Judicial Reporting Formulas (হাইকোর্টের রুল ও রিট মামলার প্রমিত পরিভাষা)
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: In Bangladeshi judicial reporting, High Court show-cause orders (Rule Nisi) follow a strict, standardized formula: '[বিষয়বস্তু] কেন [আইনগত ফলাফল] ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন হাইকোর্ট।' Translating 'issued a rule asking why... should not be declared illegal' literally as 'জিজ্ঞেস করে রুল জারি করেছে' is a catastrophic calque that destroys the formal legal register. Courts always take the honorific plural verb 'জারি করেছেন'.

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ নদী দখল নিয়ন্ত্রণে বিবাদীদের নিষ্ক্রিয়তা কেন বেআইনি ঘোষণা করা হবে না, তা জানতে চেয়ে রুল জারি করেছেন হাইকোর্ট।
  - ✓ বিচারপতিদ্বয়ের সমন্বয়ে গঠিত বেঞ্চ এ আদেশ দেন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ কেন নিষ্ক্রিয়তা বেআইনি হওয়া উচিত নয় তা জিজ্ঞেস করে একটি রুল জারি করেছে।
  - ✗ হাইকোর্ট একটি রুল দিয়েছে কেন এটা করা হবে না।

**Common LLM Error**: LLMs translate 'asking why... should not' as conversational 'জিজ্ঞেস করে' and drop the judicial honorific plural.
**Sources / Citations**: Supreme Court of Bangladesh Style & Terminology Norms, Bangladesh Legal Reporting Handbook (BILS / Press Institute)

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 12: [CRD-TRN-003] Macroeconomic & Financial News Syntax (অর্থনৈতিক সংবাদ ও বাংলাদেশ ব্যাংক পরিভাষা)
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: In economic journalism (e.g. The Business Standard, Bangladesh Bank releases), numbers and statistical movements require precise conventions: percentages in prose should prefer 'শতাংশ' over '%' symbols in formal leads; interest rate changes use 'বেসিস পয়েন্ট' (basis points); policy rate is 'নীতি সুদহার'; movements 'driven by' must be rendered as active cause ('...কারণে মূল্যস্ফীতি দাঁড়িয়েছে') rather than clumsy passives ('...দ্বারা চালিত').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ খাদ্যপণ্যের মূল্যবৃদ্ধির কারণে অক্টোবরে সার্বিক মূল্যস্ফীতি বেড়ে দাঁড়িয়েছে ১০.৮৭ শতাংশে।
  - ✓ বাংলাদেশ ব্যাংক তাদের নীতি সুদহার ৫০ বেসিস পয়েন্ট বাড়িয়ে ১০ শতাংশ নির্ধারণ করেছে।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ মূল্যস্ফীতি ১০.৮৭% হয়েছে, যা খাদ্যমূল্যের দ্বারা চালিত।
  - ✗ কেন্দ্রীয় ব্যাংক পলিসি রেট ৫০ বেসিস পয়েন্টে হাইক করেছে।

**Common LLM Error**: LLMs paste English corporate jargon directly ('হাইক করেছে', 'দ্বারা চালিত') and rely exclusively on '%' symbols instead of 'শতাংশ'.
**Sources / Citations**: Bangladesh Bank Monetary Policy Statement (MPS) Glossary, The Business Standard (TBS) Bangla Desk Style Guide

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---

### Card 13: [CRD-TRN-004] Sports Vernacular & Cricket Reporting (ক্রিকেট ও ক্রীড়া সংবাদ পরিভাষা)
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `data-supported` (Candidate for Human Review)
- **Rule Summary**: Sports news in Bengali uses lively, active phrasing. The common English cliché 'conceded a defeat against X' must NEVER be translated as 'X-এর বিরুদ্ধে পরাজয় স্বীকার করেছে' (which sounds like military surrender). The standard, idiomatic sports phrasing is 'X-এর কাছে [উইকেট/রানে] হেরেছে' or 'পরাজিত হয়েছে'. Batsmen are referred to as 'ব্যাটার' or 'ব্যাটসম্যান', scores are 'অর্ধশতক' (half-century) and 'শতক' (century).

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ মিডল অর্ডার ব্যাটারের লড়াকু অর্ধশতক সত্ত্বেও সফরকারীদের কাছে ৫ উইকেটে হেরেছে বাংলাদেশ।
  - ✓ টস জিতে ফিল্ডিংয়ের সিদ্ধান্ত নেয় স্বাগতিক দল।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ বাংলাদেশ সফরকারীদের বিরুদ্ধে পাঁচ উইকেটের পরাজয় স্বীকার করেছে।
  - ✗ একটি সাহসী হাফ-সেঞ্চুরির পরেও দলটি আত্মসমর্পণ করেছে।

**Common LLM Error**: LLMs translate 'conceded defeat' literally as 'পরাজয় স্বীকার করেছে' and 'against' as 'বিরুদ্ধে' instead of authentic sports 'কাছে'.
**Sources / Citations**: Prothom Alo Khela Desk Style Manual, Pavilion Cricket Lexicon

**Human Reviewer Decision Box**:
- [ ] **APPROVED** (Elevate to `reviewed`)
- [ ] **REVISE** (Needs amendment)
- *Reviewer Handle / Name*: ____________________
- *Reviewer Notes*: ____________________

---
