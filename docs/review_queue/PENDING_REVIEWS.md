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

## 📥 Pending Candidate Queue (3 Cards Awaiting Human Review)

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
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'পড়িয়া' requires naturalization to active causal phrasing (e.g. 'চলিত রূপে 'পড়ে' ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ চলিত রূপে 'পড়ে' ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ পড়িয়া

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'পড়িয়া'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-002 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 3: [CRD-DFT-003] Candidate Rule for Pattern: Byline, News, type, Web, Publish, date, 
- **File**: `knowledge\cards\drafts\CRD-DFT-003.yaml`
- **Domain**: `translation` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'Byline, News, type, Web, Publish, date, Friday, October, Tags, URL, category, News, category, Featured, image, News, images, Hide, Featured, Image, Details, summary, Long, Read, Title, position, Left' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ Byline, News, type, Web, Publish, date, Friday, October, Tags, URL, category, News, category, Featured, image, News, images, Hide, Featured, Image, Details, summary, Long, Read, Title, position, Left

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'Byline, News, type, Web, Publish, date, Friday, October, Tags, URL, category, News, category, Featured, image, News, images, Hide, Featured, Image, Details, summary, Long, Read, Title, position, Left'.
**Sources / Citations**: Corpus Harvester Anomaly Detector, Bangla Academy Corpus

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-003 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
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
