# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `479`
- **Clean Human Benchmark**: `468` (Verified authentic native sentences)
- **Canary Trapped**: `10` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `1` (Flagged for human linguistic review)

## Audit Breakdown by Source & Domain

| ID | Source | Domain | Category | Flaws Trapped | Sample / Flaw Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CORP-ACD-001` | University Research Journal | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-002-RAW` | Peer-Reviewed Journal Abstract (Raw LLM) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'পেপারটি তর্ক করে' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-ACD-002-GOLD` | Peer-Reviewed Journal Abstract (Human Gold) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-003` | Bangla Academy Bhashatotto Journal | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-004-RAW` | Social Science Review (Dhaka University) (Raw LLM) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-004-GOLD` | Social Science Review (Dhaka University) (Human Gold) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-005` | Doctoral Dissertation Defense Guidelines | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-001` | Cabinet Division Bangladesh | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-RAW` | Deputy Commissioner Office Circular (Raw LLM) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-GOLD` | Deputy Commissioner Office Circular (Human Gold) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-003` | Ministry of Public Administration (MoPA) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-004` | Formal D.O. Letter Precedent | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-005` | Office of the Prime Minister / Chief Adviser | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-001` | Department of Agricultural Extension (DAE) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-RAW` | Bangladesh Meteorological Department (BMD) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-GOLD` | Bangladesh Meteorological Department (BMD) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-003` | Flood Forecasting and Warning Centre (FFWC) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-RAW` | Bangladesh Rice Research Institute (BRRI) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-GOLD` | Bangladesh Rice Research Institute (BRRI) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-005` | Ministry of Disaster Management and Relief | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-001` | Bangladesh Bank (BRPD Circular) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-002` | Press Information Department (PID Handout) | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-003` | National Board of Revenue (NBR SRO) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-004` | Civil Petition Precedent | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-005` | Ministry of Land Sub-Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-001-RAW` | The Business Standard (TBS) (Raw LLM) | Macroeconomic & Finance | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'দ্বারা চালিত' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-001-GOLD` | The Business Standard (TBS) (Human Gold) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-002-RAW` | BDNews24 (Raw LLM) | Judicial & High Court | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'জিজ্ঞেস করে একটি রুল' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-002-GOLD` | BDNews24 (Human Gold) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-003-RAW` | Prothom Alo (Sports Desk) (Raw LLM) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-003-GOLD` | Prothom Alo (Sports Desk) (Human Gold) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-004-RAW` | The Daily Star Bangla (Raw LLM) | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-004-GOLD` | The Daily Star Bangla (Human Gold) | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-005-RAW` | Dhaka Tribune / Bangla Tribune (Raw LLM) | Disaster Early Warning | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'বড় বিপদের সংকেত' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-005-GOLD` | Dhaka Tribune / Bangla Tribune (Human Gold) | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-001` | Kashiram Das (Mahabharata) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-002` | Krittibas Ojha (Ramayana) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-003` | Michael Madhusudan Dutt (Meghnadbadh Kavya) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-004` | Rabindranath Tagore (Sanchayita) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-005` | Kazi Nazrul Islam (Bidrohi) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-001` | Modern Literary Fiction Anthology | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-002-RAW` | Literary Translation Benchmark (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `2` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'ঝোপের চারপাশে পেটানো' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-002-GOLD` | Literary Translation Benchmark (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-003` | Riverine Bengal Novel Excerpt | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-004-RAW` | Urban Fiction Dialogue (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-004-GOLD` | Urban Fiction Dialogue (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-005` | Short Story Psychological Monologue | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-001` | NCTB Creative Questioning Framework | Education & NCTB Pedagogy | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('পড়িয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `CORP-PED-002-RAW` | NCTB Secondary Assessment Manual (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-002-GOLD` | NCTB Secondary Assessment Manual (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-003` | Higher Secondary Board Examination Model | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-RAW` | NCTB Bengali First Paper Board Question (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-GOLD` | NCTB Bengali First Paper Board Question (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-005` | National Curriculum Framework 2026 | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-001` | Directorate General of Health Services (DGHS) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-RAW` | Clinical Practice Guidelines (Medicine) (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-GOLD` | Clinical Practice Guidelines (Medicine) (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-003` | Institute of Epidemiology, Disease Control and Research (IEDCR) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-RAW` | Bangladesh Paediatric Association (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-GOLD` | Bangladesh Paediatric Association (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-005` | National Mental Health Institute | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-001` | Bangladesh Computer Council (BCC) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-002-RAW` | Software Engineering Team Manual (Raw LLM) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-002-GOLD` | Software Engineering Team Manual (Human Gold) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-003` | Digital Bangladesh / Smart Bangladesh Blueprint | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-004-RAW` | API Architecture Specification (Raw LLM) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-004-GOLD` | API Architecture Specification (Human Gold) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-005` | Cyber Security Agency (BGD e-GOV CIRT) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-001` | Directorate of Land Records and Surveys (DLRS) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-002-RAW` | District Sub-Registry Office Precedent (Raw LLM) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-002-GOLD` | District Sub-Registry Office Precedent (Human Gold) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-003` | Ministry of Land Portal | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-004-RAW` | Civil Court Land Dispute Precedent (Raw LLM) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-004-GOLD` | Civil Court Land Dispute Precedent (Human Gold) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-005` | Assistant Commissioner (Land) AC Land Court | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-001` | Supreme Court of Bangladesh (High Court Division) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-RAW` | High Court Division Judgment Precedent (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-GOLD` | High Court Division Judgment Precedent (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-003` | Bangladesh Code (Statutory Law) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-RAW` | High Court Division Writ Bench (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-GOLD` | High Court Division Writ Bench (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-005` | Supreme Court Bar Association Records | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-001` | Bangladesh Bank Monetary Policy Department | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-RAW` | Financial Express Bangladesh (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-GOLD` | Financial Express Bangladesh (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-003` | BIBM (Bangladesh Institute of Bank Management) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-RAW` | Dhaka Chamber of Commerce & Industry (DCCI) (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-GOLD` | Dhaka Chamber of Commerce & Industry (DCCI) (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-005` | National Accounts Statistics (BBS) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-001` | NCTB Curriculum Manual | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-002` | Bangla Wikipedia (উইকিপিডিয়া) | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-003` | Classical Poetic Corpus | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-004` | Department of Agricultural Extension (DAE) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-005` | Healthcare Clinical Protocol | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-001` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-002` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-003` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-004` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-005` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-006` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-007` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-008` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-009` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-010` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-011` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-012` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-013` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-014` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-015` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-016` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-017` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-018` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-019` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-020` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-021` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-022` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-023` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-024` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-025` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-026` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-027` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-028` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-029` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-030` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-031` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-032` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-033` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-034` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-035` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-036` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-037` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211205-038` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-001` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-002` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-003` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-004` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-005` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-006` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-007` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-008` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-009` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-010` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-011` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-012` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-013` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-014` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-015` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-016` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-017` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211223_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211223_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261112_211223_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-021` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-022` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-023` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-024` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-025` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-026` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-027` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-028` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-029` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-030` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-031` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-032` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-033` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-034` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-035` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211229-036` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211238_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211238_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211238_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261112_211238_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-005` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-006` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-007` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-008` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-009` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-010` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-011` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-012` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-013` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-014` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-015` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-016` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211245_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211245_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211245_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-020` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-021` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-022` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-023` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-024` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-025` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-026` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-027` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-028` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-029` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-030` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-031` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-032` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211254-033` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211310_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-002` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-003` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-004` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-005` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-006` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-007` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-008` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-009` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-010` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-011` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-012` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-013` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-014` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-015` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-016` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-017` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-018` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-019` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-020` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211323_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211323_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211323_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211323_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-025` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-026` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-027` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211324-028` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-001` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-002` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-003` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-004` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211349_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211349_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211349_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-008` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-009` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-010` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-011` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-012` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-013` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-014` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-015` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-016` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-017` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-018` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-019` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211357_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211357_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211357_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211357_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-024` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-025` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-026` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211357-027` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-001` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-002` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-003` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-004` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-005` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-006` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-007` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-008` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-009` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-010` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-011` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-012` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-013` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-014` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-015` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-016` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211435_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211435_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211435_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211435_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-021` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-022` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-023` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211436-024` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-001` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-005` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-006` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-007` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-008` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-009` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-010` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-011` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-012` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-013` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211516_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211516_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211516_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211516_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-018` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-019` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-020` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211517-021` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211548_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211548_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211548_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211548_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-005` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-006` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-007` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-008` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211552_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211552_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211552_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-012` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-013` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-014` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-015` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211555_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211555_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211555_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211555_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-020` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-021` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-022` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211555-023` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211626_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211626_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-005` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-006` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-008` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-009` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-010` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_211634_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-012` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-013` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-014` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211634-015` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-001` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-008` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-011` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211721-012` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-001` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-008` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-011` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211816-012` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-001` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-008` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-011` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_211919-012` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-001` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-003` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-004` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-008` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-011` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212024-012` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-001` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-002` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212123-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_212223_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_212223_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261112_212223_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-005` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-006` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-007` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-009` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-010` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212225-011` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212329-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212435-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212542-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212643-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212739-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-004` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212836-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nbsp |
| `SCRAPED-2026_11_12_212937-001` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-002` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-003` | Bangla Wikipedia Land Law & Property Registry | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-004` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_212937-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213041_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213041_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213041_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213041_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213041-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213041-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213041-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213041-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213144_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213144_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213144_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261112_213144_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213144-005` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213144-006` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213144-007` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_12_213144-008` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
