# Cycle 1 Live Tasks Audit Report

## 1. Scenario: Proofreading & Flawed Text Correction
- **Input (Flawed)**:
  `তিনি রেলষ্টেশনে আসিয়া দেখিলেন যে ট্রেন ছাড়িয়া গিয়াছে। ডাকঘরে গিয়ে তিনি ৫০.২৫ টাকার একটি পোষ্টাল অর্ডার পাঠাইলেন। গাছের ডালে পাখী বসিয়া গান গাইতেছিল.`
- **Bhashabid Corrected**:
  `তিনি রেলস্টেশনে এসে দেখলেন যে ট্রেন ছেড়ে গেছে। ডাকঘরে গিয়ে তিনি ৫০.২৫ টাকার একটি পোস্টাল অর্ডার পাঠালেন। গাছের ডালে পাখি বসে গান গাচ্ছিল।`
- **Defects Fixed**:
  - Replaced archaic foreign loanword cluster `রেলষ্টেশন` -> `রেলস্টেশন`
  - Replaced `পোষ্টাল` -> `পোস্টাল`
  - Rectified tatbhava short-vowel `পাখী` -> `পাখি`
  - Eliminated Sadhu-Cholito mixing (গুরুচণ্ডালী দোষ): আসিয়া -> এসে, দেখিলেন -> দেখলেন, ছাড়িয়া গিয়াছে -> ছেড়ে গেছে, বসিয়া -> বসে
  - Standardized sentence terminal punctuation: ASCII `.` -> Bengali Dari (`।`)

## 2. Scenario: Number-Heavy Administrative Text
- **Input**: 12500000 (1 crore 25 lakh)
- **Formatted Digit String**: `১,২৫,০০,০০০`
- **In Bengali Words**: `এক কোটি পঁচিশ লাখ`
- **Assembled Text**: `মোট বরাদ্দের পরিমাণ ১,২৫,০০,০০০ টাকা (এক কোটি পঁচিশ লাখ টাকা)।`

## 3. Scenario: Anti-Calque Idiomatic Translation
- **Source Prompt**: "Actions speak louder than words."
- **Common LLM Calque (Rejected)**: "কাজ শব্দের চেয়ে জোরে কথা বলে।"
- **Bhashabid Idiomatic Output**: `কথার চেয়ে কাজের মূল্য বেশি।`

## 4. Verdict
All 3 Live Tasks passed with 0 Guru-chandali violations, 0 calques, and 100% compliant Bangla Academy orthography.
