# Expert Linguistic Review Packet (PENDING_REVIEWS.md)

Standard: **Bangla Academy (Dhaka) & Paschimbanga Bangla Akademi (Kolkata)**  
Constitutional Rule: **Principle P2 (Human Native Provenance Required)**

> [!IMPORTANT]
> The only cards awaiting human review are candidate drafts located in `knowledge/cards/drafts/`.
> Production cards in `knowledge/cards/` are already reviewed, tested, and active.

---

## Instructions for Human Reviewers via GitHub PR
1. Inspect the pending draft cards below or directly in `knowledge/cards/drafts/`.
2. Open a Pull Request on GitHub with your review decision, reviewer name, and affiliation.
3. Once approved and merged, draft cards remain preserved in `knowledge/cards/drafts/` as a permanent public record of your contribution!

---

## 📥 Pending Candidate Queue (5 Cards Awaiting Human Review)

### Draft 1: [CRD-DFT-001] Candidate Rule for Pattern: দ্বারা চালিত
- **File**: `knowledge\cards\drafts\CRD-DFT-001.yaml`
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'দ্বারা চালিত' requires naturalization to active causal phrasing (e.g. 'পরিচালিত', 'নেতৃত্বে', 'কারণে').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ খাদ্যপণ্যের মূল্যবৃদ্ধির কারণে মূল্যস্ফীতি বেড়েছে।
  - ✓ প্রকল্পটির কাজ বিদ্যুৎ বিভাগের অধীনে পরিচালিত হচ্ছে।
  - ✓ প্রধান উপদেষ্টার সভাপতিত্বে অনুষ্ঠিত বৈঠকে এ সিদ্ধান্ত গৃহীত হয়।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ মূল্যবৃদ্ধি দ্বারা চালিত মূল্যস্ফীতি।
  - ✗ প্রকল্পটি বিদ্যুৎ বিভাগ দ্বারা পরিচালিত।
  - ✗ প্রধান উপদেষ্টা দ্বারা সভাপতিত্ব করা বৈঠকে।

**Common LLM Error**: LLMs emit literal English passive calques ('দ্বারা চালিত', 'দ্বারা অনুষ্ঠিত') instead of natural active causal syntax.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Promito Byaboharik Bangla Obhidhan

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-001 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 2: [CRD-DFT-002] Candidate Rule for Pattern: পড়িয়া
- **File**: `knowledge\cards\drafts\CRD-DFT-002.yaml`
- **Domain**: `Education & NCTB Pedagogy` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'পড়িয়া' requires naturalization to active causal phrasing (e.g. 'চলিত রূপে 'পড়ে' ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ চলিত রূপে 'পড়ে' ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ পড়িয়া
  - ✗ উদ্দীপকটি পড়িয়া নিচের প্রশ্নগুলোর উত্তর দাও: (ক) সালোকসংশ্লেষণ প্রক্রিয়ার প্রধান কাঁচামাল কী? (খ) উদ্ভিদের পাতাকে কেন রান্নাতত্ত্বের সাথে তুলনা করা হয়? বুঝিয়ে লেখ।

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'পড়িয়া'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus, National Curriculum and Textbook Board (NCTB) Standard Bengali, Ministry of Education Pedagogical Guidelines

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-002 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 3: [CRD-DFT-004] Candidate Rule for Pattern: জিজ্ঞেস করে একটি রুল
- **File**: `knowledge\cards\drafts\CRD-DFT-004.yaml`
- **Domain**: `Judicial & High Court` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'জিজ্ঞেস করে একটি রুল' requires naturalization to active causal phrasing (e.g. 'স্বাভাবিক বাংলা প্রকাশভঙ্গি 'কেন ... হবে না, তা জানতে চেয়ে রুল জারি করেছেন' ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ স্বাভাবিক বাংলা প্রকাশভঙ্গি 'কেন ... হবে না, তা জানতে চেয়ে রুল জারি করেছেন' ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ জিজ্ঞেস করে একটি রুল
  - ✗ হাইকোর্ট সরকারকে জিজ্ঞেস করে একটি রুল জারি করেছে কেন আটক বেআইনি হবে না।

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'জিজ্ঞেস করে একটি রুল'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus, Bangla Academy Standard Bengali Grammar, Constitution of the People's Republic of Bangladesh (Article 102), Supreme Court of Bangladesh Judicial Precedents, Bangla Academy Law Dictionary

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-004 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 4: [CRD-DFT-005] Candidate Rule for Pattern: বড় বিপদের সংকেত
- **File**: `knowledge\cards\drafts\CRD-DFT-005.yaml`
- **Domain**: `Disaster Early Warning` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'বড় বিপদের সংকেত' requires naturalization to active causal phrasing (e.g. 'স্বাভাবিক বাংলা প্রকাশভঙ্গি 'মহাবিপদ সংকেত' ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ স্বাভাবিক বাংলা প্রকাশভঙ্গি 'মহাবিপদ সংকেত' ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ বড় বিপদের সংকেত
  - ✗ ঘূর্ণিঝড় কাছে আসায় সমুদ্রবন্দরগুলোকে ১০ নম্বর বড় বিপদের সংকেত উত্তোলন করতে বলা হয়েছে।

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'বড় বিপদের সংকেত'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus, Bangla Academy Standard Bengali Grammar, Ministry of Agriculture & Department of Agricultural Extension (DAE), Disaster Management Bureau Standing Orders on Disaster (SOD)

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-005 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 5: [CRD-DFT-006] Candidate Rule for Pattern: ঝোপের চারপাশে পেটাচ্ছেন
- **File**: `knowledge\cards\drafts\CRD-DFT-006.yaml`
- **Domain**: `Creative Fiction & Dialogue` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'ঝোপের চারপাশে পেটাচ্ছেন' requires naturalization to active causal phrasing (e.g. 'স্বাভাবিক বাংলা প্রকাশভঙ্গি 'ঘুরিয়ে-পেঁচিয়ে কথা বলা / মূল প্রসঙ্গ এড়িয়ে যাওয়া' ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ স্বাভাবিক বাংলা প্রকাশভঙ্গি 'ঘুরিয়ে-পেঁচিয়ে কথা বলা / মূল প্রসঙ্গ এড়িয়ে যাওয়া' ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ ঝোপের চারপাশে পেটাচ্ছেন
  - ✗ আপনি কেন সবসময় ঝোপের চারপাশে পেটাচ্ছেন? এই কাজটি কোনো কেকের টুকরো নয়।

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'ঝোপের চারপাশে পেটাচ্ছেন'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus, Bangla Academy Standard Bengali Grammar (প্রমিত বাংলা ভাষার ব্যাকরণ), Bangla Academy Modern Bengali Dictionary (আধুনিক বাংলা অভিধান)

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-006 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

## 🛡️ Active Production Cards (28 Approved in `knowledge/cards/`)

### Card 1: [CRD-DOM-001] Official Administrative Applications & Petitions (দাপ্তরিক আবেদন ও দরখাস্তের প্রমিত কাঠামো)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 2: [CRD-DOM-002] Letter Writing & Correspondence Registers (চিঠিপত্র ও সামাজিক যোগাযোগের অনুশাসন)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 3: [CRD-DOM-003] Literary Fiction & Story Writing (কথাসাহিত্য, গল্প ও সংলাপ লিখন শৈলী)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 4: [CRD-DOM-004] Academic & Scholarly Research Prose (শিক্ষায়তনিক ও গবেষণা প্রবন্ধ শৈলী)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 5: [CRD-DOM-005] Book Authoring & Non-Fiction Essays (মননশীল প্রবন্ধ ও গ্রন্থ প্রণয়ন রীতি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 6: [CRD-DOM-006] Corporate & Marketing Copywriting (কর্পোরেট যোগাযোগ ও বাণিজ্যিক কপিরাইটিং)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 7: [CRD-DOM-007] Legal Drafting & Contracts (আইনি দলিল, চুক্তিপত্র ও নোটিশ লিখন)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 8: [CRD-DOM-008] Healthcare & Medical Public Advisories (চিকিৎসাসেবা ও জনস্বাস্থ্য যোগাযোগ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 9: [CRD-DOM-009] Classical Bengali Prosody & Poetic Scansion (বাংলা ছন্দবিজ্ঞান ও পয়ার প্রকরণ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 10: [CRD-DOM-010] Land Records & Property Deeds (ভূমি রেজিস্ট্রি, খতিয়ান ও সাফ-কবলা দলিল)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 11: [CRD-DOM-011] Agronomy, Meteorology & Disaster Bulletins (কৃষি সম্প্রসারণ, আবহাওয়া ও দুর্যোগ পূর্বাভাস)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 12: [CRD-DOM-012] NCTB Creative Pedagogy & Exam Questioning (জাতীয় শিক্ষাক্রম ও সৃজনশীল প্রশ্নপদ্ধতি কাঠামো)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 13: [CRD-DOM-013] Poetic Metaphors, Imagery & Figurative Diction (কাব্যিক রূপক, চিত্রকল্প ও ভাবার্থ প্রকাশ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 14: [CRD-GRM-001] Sadhu-Cholito Verb Consistency (গুরুচণ্ডালী দোষ পরিহার)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 15: [CRD-GRM-002] Honorific Concordance Across Pronouns and Verbs (আপনি / তুমি / তুই)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 16: [CRD-GRM-003] Bengali Case Markers and Postposition Agreement (কারক ও বিভক্তি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 17: [CRD-GRM-004] Bengali Euphonic Junctions (সন্ধি: স্বরসন্ধি ও ব্যঞ্জনসন্ধি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 18: [CRD-GRM-005] Bengali Compound Formation (সমাস: দ্বন্দ্ব, দ্বিগু, তৎপুরুষ ও কর্মধারয়)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 19: [CRD-NUM-001] Irregular Bengali Cardinal Numbers 0-99 (০-৯৯ অনিয়মিত সংখ্যা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 20: [CRD-ORT-001] Unicode NFC Canonicalization and Composite Graphemes (য়, ড়, ঢ়)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 21: [CRD-ORT-002] Bangla Academy Loanword S-Rule (বিদেশি শব্দে 'স' বনাম 'ষ')
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 22: [CRD-ORT-003] Regional Orthographic Variations (বাংলাদেশ প্রমিত বনাম পশ্চিমবঙ্গ বানানরীতি)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 23: [CRD-TRN-001] Translation Idioms vs Literal English Calques (ভাবানুবাদ বনাম আক্ষরিক অনুবাদ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 24: [CRD-TRN-002] High Court & Judicial Reporting Formulas (হাইকোর্টের রুল ও রিট মামলার প্রমিত পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 25: [CRD-TRN-003] Macroeconomic & Financial News Syntax (অর্থনৈতিক সংবাদ ও বাংলাদেশ ব্যাংক পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 26: [CRD-TRN-004] Sports Vernacular & Cricket Reporting (ক্রিকেট ও ক্রীড়া সংবাদ পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 27: [CRD-TRN-005] Article 102 Constitutional Writs Taxonomy & Drafting (সংবিধানের ১০২ অনুচ্ছেদের রিট মামলার প্রমিত পরিভাষা)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Lead Native-Speaker Reviewer)
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)

### Card 28: [CRD-TRN-006] Proverbs, Idioms & Metaphoric Equivalence (প্রবাদ-প্রবচন, বাগধারা ও রূপকার্থ সমীকরণ)
- **Status**: `APPROVED` | **Reviewer**: Ashikur Rahman Bhuiyan (Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>))
**Human Reviewer Decision Box**:
- [x] **APPROVED** (Verified by Ashikur Rahman Bhuiyan)
