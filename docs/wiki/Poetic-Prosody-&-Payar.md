# Poetic Prosody & Payar Verification (বাংলা ছন্দবিজ্ঞান ও পয়ার)

Bhashabid provides a deterministic phonological prosody engine (`tools/bn_prosody`) that decomposes Bengali lines into phonetic syllables (*দল*) and calculates morae according to the classical metres.

---

## 🎼 The Three Classical Metres

1. **দলবৃত্ত / স্বরবৃত্ত (Dalabritta / Svarabritta)**:
   - মুক্তদল = ১ মাত্রা, রুদ্ধদল = ১ মাত্রা.
   - Pacing: ৪+৪+৪+২ দ্রুত লয় (ছড়া, লোকসংগীত).
   - Example: `বৃষ্টি পড়ে টাপুর টুপুর নদে এল বান`

2. **মাত্রাবৃত্ত / কলাবৃত্ত (Matrabritta / Kalabritta)**:
   - মুক্তদল = ১ মাত্রা, রুদ্ধদল = ২ মাত্রা.
   - Pacing: ৬+৬+২ বা ৫+৫+২ ধীর/মধ্যম লয়.

3. **অক্ষরবৃত্ত / পয়ার (Aksharbritta / Payar)**:
   - প্রতিটি অক্ষর = ১ একক (মৌলিক পর্ব ৮ মাত্রা + প্রান্তিক পর্ব ৬ মাত্রা = ১৪ মাত্রা).
   - মধ্যযতি (Caesura) ৮ মাত্রার পর অবস্থান করে.
   - Example:
     ```text
     কাশীদাস কহে সাধু শুনে পুণ্যবান।
     মহাভারত কথা অমৃত সমান॥
     ```

---

## 🔍 Verification with the CLI

```bash
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar
```

**Output**:
```text
পয়ার ছন্দ যাচাই: শুদ্ধ (VALID)
পর্ব ১ (৮ মাত্রা): 8 | পর্ব ২ (৬ মাত্রা): 6 | মোট: 14
বিশ্লেষণ: শুদ্ধ পয়ার ছন্দ: ৮+৬=১৪ মাত্রার পর্ব ও মধ্যযতি যথাযথভাবে বিন্যস্ত।
```
