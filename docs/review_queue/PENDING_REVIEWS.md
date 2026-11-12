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

## 📥 Pending Candidate Queue (20 Cards Awaiting Human Review)

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

### Draft 6: [CRD-DFT-007] Candidate Rule for Pattern: তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপ
- **File**: `knowledge\cards\drafts\CRD-DFT-007.yaml`
- **Domain**: `Constitutional Law & Writs` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করে' requires naturalization to active causal phrasing (e.g. 'বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করে'').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করে'

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করে থাকেন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'তিনি চীফ মেট্রোপলিটন ম্যাজিস্ট্রেটের ডেপুটি হিসেবে তার অবর্তমানে তার দায়িত্বভার পালন করে'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Bangladesh Case Law & Jurisprudence, Principle P2 Human Provenance Audit Gate, Constitution of the People's Republic of Bangladesh (Article 102), Supreme Court of Bangladesh Judicial Precedents, Bangla Academy Law Dictionary

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-007 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 7: [CRD-DFT-008] Candidate Rule for Pattern: alphabet
- **File**: `knowledge\cards\drafts\CRD-DFT-008.yaml`
- **Domain**: `Academic Research & Methodology` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'alphabet' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ আবজাদ. একটি আবজাদ ( (); অথবা আবগাদ, আক্ষ. অনু. alphabet) হলো একটি লিখন পদ্ধতি, যেখানে কেবল ব্যঞ্জনবর্ণগুলোকে অক্ষর বা চিহ্নের মাধ্যমে উপস্থাপন করা হয়, আর স্বরবর্ণগুলোকে পাঠককে অনুমান করে নিতে হয় (যদি না অন্য কোনোভাবে, যেমন—ডায়াক্রিটিক ব্যবহার করে সেগুলোকে উপস্থাপন করা হয়)

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'alphabet'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Linguistics & Academic Research, Principle P2 Human Provenance Audit Gate, Bangla Academy Linguistic Research Methodology Guidelines, Linguistic Society of Bangladesh Peer-Reviewed Standards

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-008 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 8: [CRD-DFT-009] Candidate Rule for Pattern: Help, OAuth
- **File**: `knowledge\cards\drafts\CRD-DFT-009.yaml`
- **Domain**: `ICT & Software Engineering` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'Help, OAuth' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ ওঅথ. মিডিয়াউইকির (উইকিপিডিয়া ব্যবহৃত সফটওয়্যার) ওঅথ সমর্থনের জন্য দেখুন mw:Help:OAuth ওঅথ হল প্রবেশ প্রতিনিধিদের জন্য একটি বিশেষ মুক্ত আদর্শ,যে পদ্ধতিতে ইন্টারনেট ব্যবহারকারীরা কোন পাসওয়ার্ড দেয়া ছাড়াই অন্য ওয়েবসাইটকে তাদের ওয়েবসাইট কিংবা অ্যাপ্লিকেশনের তথ্যাদিতে প্রবেশাধিকার দেন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'Help, OAuth'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Computer Science & Software, Principle P2 Human Provenance Audit Gate, Bangladesh Computer Council (BCC) Bengali Computing & Unicode Standards, Open-Source Bengali Localization Best Practices

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-009 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 9: [CRD-DFT-010] Candidate Rule for Pattern: Salesians, Don, Bosco
- **File**: `knowledge\cards\drafts\CRD-DFT-010.yaml`
- **Domain**: `Education & NCTB Pedagogy` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'Salesians, Don, Bosco' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ Salesians of Don Bosco (SDB)র অধীনস্থ ডনবস্কো সোসাইটি বিশ্ববিদ্যালয়টি পরিচালনা করেন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'Salesians, Don, Bosco'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Education & Pedagogy, Principle P2 Human Provenance Audit Gate, National Curriculum and Textbook Board (NCTB) Standard Bengali, Ministry of Education Pedagogical Guidelines

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-010 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 10: [CRD-DFT-011] Candidate Rule for Pattern: MissingDaughter
- **File**: `knowledge\cards\drafts\CRD-DFT-011.yaml`
- **Domain**: `Macroeconomics & Banking` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'MissingDaughter' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ বিডিওএসএনের #MissingDaughter কার্যক্রমের অংশ হিসেবে আয়োজিত এ প্রতিযোগিতার লক্ষ্য মেয়েদের প্রোগ্রামিংয়ে আগ্রহী করে তোলা এবং প্রযুক্তি খাতে তাদের অংশগ্রহণ বাড়ানো

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'MissingDaughter'.
**Sources / Citations**: Corpus Harvest Provenance: Prothom Alo (National & Economy), Principle P2 Human Provenance Audit Gate, Bangladesh Bank Prudential Regulations & Monetary Policy, Bangla Academy Financial & Economic Terminology, The Business Standard Verified Macroeconomic Feed

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-011 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 11: [CRD-DFT-012] Candidate Rule for Pattern: abdul, alim
- **File**: `knowledge\cards\drafts\CRD-DFT-012.yaml`
- **Domain**: `ICT & Software Engineering` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'abdul, alim' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ md abdul alim m2a এটি প্রতিষ্ঠা করেন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'abdul, alim'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Information Technology & Computing, Principle P2 Human Provenance Audit Gate, Bangladesh Computer Council (BCC) Bengali Computing & Unicode Standards, Open-Source Bengali Localization Best Practices

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-012 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 12: [CRD-DFT-013] Candidate Rule for Pattern: Career, Era, Opportunities, and, Challen
- **File**: `knowledge\cards\drafts\CRD-DFT-013.yaml`
- **Domain**: `Macroeconomics & Banking` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'Career, Era, Opportunities, and, Challenges' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ খুদে ভক্তের জন্য কেন কেঁদেছিলেন হুমায়ূন আহমেদ প্রতিযোগিতার পাশাপাশি বিকেল ৩টায় ‘Career in AI Era: Opportunities and Challenges’ শীর্ষক একটি প্যানেল আলোচনা অনুষ্ঠিত হবে

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'Career, Era, Opportunities, and, Challenges'.
**Sources / Citations**: Corpus Harvest Provenance: Prothom Alo (National & Economy), Principle P2 Human Provenance Audit Gate, Bangladesh Bank Prudential Regulations & Monetary Policy, Bangla Academy Financial & Economic Terminology, The Business Standard Verified Macroeconomic Feed

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-013 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 13: [CRD-DFT-014] Candidate Rule for Pattern: continution, form
- **File**: `knowledge\cards\drafts\CRD-DFT-014.yaml`
- **Domain**: `Education & NCTB Pedagogy` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'continution, form' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ শিক্ষার্থী থাকার প্রমাণ হিসেবে ৩ মাস পর পর বিভাগীয় এবং শিক্ষানুস্থানের প্রধানের স্বাক্ষর থাকা 'continution form' জমা দিতে হয়

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'continution, form'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Education & Pedagogy, Principle P2 Human Provenance Audit Gate, National Curriculum and Textbook Board (NCTB) Standard Bengali, Ministry of Education Pedagogical Guidelines

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-014 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 14: [CRD-DFT-015] Candidate Rule for Pattern: XXIII, VIII
- **File**: `knowledge\cards\drafts\CRD-DFT-015.yaml`
- **Domain**: `Constitutional Law & Writs` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'XXIII, VIII' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ এটি মূলত বাংলাদেশ সরকার কর্তৃক প্রণীত ১৯৮০ সালের আইন নং XXIII থেকে ১৯৮২ সালের অধ্যাদেশ নং VIII পর্যন্ত বলবৎ আইনের ৩৭ নং আইন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'XXIII, VIII'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Bangladesh Case Law & Jurisprudence, Principle P2 Human Provenance Audit Gate, Constitution of the People's Republic of Bangladesh (Article 102), Supreme Court of Bangladesh Judicial Precedents, Bangla Academy Law Dictionary

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-015 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 15: [CRD-DFT-016] Candidate Rule for Pattern: SVO
- **File**: `knowledge\cards\drafts\CRD-DFT-016.yaml`
- **Domain**: `Academic Research & Methodology` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'SVO' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ এ ধরনের পদক্রমকে ইংরেজিতে সংক্ষেপে SVO(Subject-Verb-Object) বলা হয়
  - ✗ ইংরেজি একটি উল্লেখযোগ্য SVO ভাষা
  - ✗ যেমন- "অহন(কর্তা) ভালোবাসে(ক্রিয়া) তাকে(কর্ম)" হলো একটি SVO পদক্রম

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'SVO'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Bengali Grammar & Philology, Principle P2 Human Provenance Audit Gate, Bangla Academy Linguistic Research Methodology Guidelines, Linguistic Society of Bangladesh Peer-Reviewed Standards

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-016 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 16: [CRD-DFT-017] Candidate Rule for Pattern: Ahan, Loves, Him
- **File**: `knowledge\cards\drafts\CRD-DFT-017.yaml`
- **Domain**: `Academic Research & Methodology` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'Ahan, Loves, Him' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ "Ahan(S) Loves(V) Him(O)" হলো একটি ইংরেজি বাক্য যা আলোচ্য পদক্রমঅনুসরণ করে গঠিত হয়েছে

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'Ahan, Loves, Him'.
**Sources / Citations**: Corpus Harvest Provenance: Bangla Wikipedia Bengali Grammar & Philology, Principle P2 Human Provenance Audit Gate, Bangla Academy Linguistic Research Methodology Guidelines, Linguistic Society of Bangladesh Peer-Reviewed Standards

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-017 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 17: [CRD-DFT-018] Candidate Rule for Pattern: তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদ
- **File**: `knowledge\cards\drafts\CRD-DFT-018.yaml`
- **Domain**: `Creative Fiction & Dialogue` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছে' requires naturalization to active causal phrasing (e.g. 'বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছে'').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছে'

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ খোলা জানালার বাইরে সন্ধ্যার হালকা বাতাস বইছিল, তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছে।

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'তিনি চেয়ার থেকে উঠে দাঁড়িয়ে বললেন যে বিদায় নেওয়ার সময় হয়েছে'.
**Sources / Citations**: Corpus Harvest Provenance: Learning from Mistakes Engine (Offline Autonomous Synthesis), Principle P2 Human Provenance Audit Gate, Bangla Academy Standard Bengali Grammar (প্রমিত বাংলা ভাষার ব্যাকরণ), Bangla Academy Modern Bengali Dictionary (আধুনিক বাংলা অভিধান)

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-018 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 18: [CRD-DFT-019] Candidate Rule for Pattern: nbsp
- **File**: `knowledge\cards\drafts\CRD-DFT-019.yaml`
- **Domain**: `Macroeconomics & Banking` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'nbsp' requires naturalization to active causal phrasing (e.g. 'প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ &nbsp;দুই দশক পর অ্যান্ডি স্যাকস চরিত্রে ফিরেছেন অ্যান

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'nbsp'.
**Sources / Citations**: Corpus Harvest Provenance: Prothom Alo (National & Economy), Principle P2 Human Provenance Audit Gate, Bangladesh Bank Prudential Regulations & Monetary Policy, Bangla Academy Financial & Economic Terminology, The Business Standard Verified Macroeconomic Feed

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-019 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 19: [CRD-DFT-020] Candidate Rule for Pattern: তিনি পদ ছাড়েন বলে
- **File**: `knowledge\cards\drafts\CRD-DFT-020.yaml`
- **Domain**: `Macroeconomics & Banking` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'তিনি পদ ছাড়েন বলে' requires naturalization to active causal phrasing (e.g. 'বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি পদ ছাড়েন বলেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে পদ ছাড়েন বলে'').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বিকল্প ১ (সম্ভ্রমাত্মক ক্রিয়াপদ): 'তিনি পদ ছাড়েন বলেন' অথবা বিকল্প ২ (সাধারণ সর্বনাম): 'সে পদ ছাড়েন বলে'

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ এর জের ধরে এনভিডিয়ার পরিচালনা পর্ষদের সিদ্ধান্তে তিনি পদ ছাড়েন বলে জানা গেছে

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'তিনি পদ ছাড়েন বলে'.
**Sources / Citations**: Corpus Harvest Provenance: Prothom Alo (National & Economy), Principle P2 Human Provenance Audit Gate, Bangladesh Bank Prudential Regulations & Monetary Policy, Bangla Academy Financial & Economic Terminology, The Business Standard Verified Macroeconomic Feed

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-020 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
```

---

### Draft 20: [CRD-DFT-021] Candidate Rule for Pattern: সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন
- **File**: `knowledge\cards\drafts\CRD-DFT-021.yaml`
- **Domain**: `Macroeconomics & Banking` | **Profile**: `bd_standard` | **Register**: `formal`
- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)
- **Rule Summary**: Automatically flagged pattern 'সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন' requires naturalization to active causal phrasing (e.g. 'বিকল্প ১ (সাধারণ ক্রিয়াপদ): 'সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করে' অথবা বিকল্প ২ (সম্ভ্রমাত্মক সর্বনাম): 'তিনি কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন'').

**Positive Examples (শুদ্ধ প্রয়োগ)**:
  - ✓ বিকল্প ১ (সাধারণ ক্রিয়াপদ): 'সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করে' অথবা বিকল্প ২ (সম্ভ্রমাত্মক সর্বনাম): 'তিনি কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন'

**Negative Examples (ভ্রান্ত প্রয়োগ)**:
  - ✗ নরওয়ে প্রশাসন যদি ভারতীয়দের সঙ্গে এমন আচরণ করত, তবে কেমন হতো সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন

**Common LLM Error**: LLMs emit literal calques or non-standard syntax for 'সে কথা ভাবা দরকার বলেও তিনি উল্লেখ করেন'.
**Sources / Citations**: Corpus Harvest Provenance: Prothom Alo (National & Economy), Principle P2 Human Provenance Audit Gate, Bangladesh Bank Prudential Regulations & Monetary Policy, Bangla Academy Financial & Economic Terminology, The Business Standard Verified Macroeconomic Feed

**Quick Action Command**:
```bash
bhashabid review --card CRD-DFT-021 --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve
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
