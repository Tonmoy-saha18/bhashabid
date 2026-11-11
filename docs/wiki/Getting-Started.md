# Getting Started with Bhashabid (ভাষাবিদ)

Bhashabid can be installed and used in multiple workflows depending on your environment.

---

## 1. Quick Installation (Python >= 3.10)

```bash
# Clone the repository
git clone https://github.com/ashik1291/bhashabid.git
cd bhashabid

# Install locally in editable mode
pip install -e .
```

To install directly from GitHub without cloning:
```bash
pip install git+https://github.com/ashik1291/bhashabid.git
```

---

## 2. Command Line Interface (CLI)

The `bhashabid` executable provides instant terminal access to all linguistic engines:

### Install Skill with all References in 1 Command
```bash
# Automatically install SKILL.md and all 8 reference guides to Antigravity, Claude, or Cursor
bhashabid install-skill --target all
```

### Numeral & Currency Conversion
```bash
bhashabid number 99
# Output: নিরানব্বই

bhashabid number 1234567 --format grouped
# Output: ১২,৩৪,৫৬৭

bhashabid number 55000.75 --format currency
# Output: পঞ্চান্ন হাজার টাকা পঁচাত্তর পয়সা
```

### Orthography Normalization
```bash
bhashabid normalize "ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন."
# Output: ডাক্তার সাহেব ৩.১৪ গ্রাম ওষুধ দিলেন।
```

### Real-Time Grammar & Calque Linting
```bash
bhashabid lint "তুমি সিদ্ধান্ত নেন এবং এটি বিদ্যুৎ দ্বারা চালিত."
```

### Poetic Prosody & Payar Verification
```bash
bhashabid prosody "কাশীদাস কহে সাধু শুনে পুণ্যবান" --verify-payar
# Output:
# পয়ার ছন্দ যাচাই: শুদ্ধ (VALID)
# পর্ব ১ (৮ মাত্রা): 8 | পর্ব ২ (৬ মাত্রা): 6 | মোট: 14
```

### High Court Writ Guidance
```bash
bhashabid writ --remedy "detention" --subject "জনাব করিম" --authority "স্বরাষ্ট্র সচিব"
```

---

## 3. Python SDK Usage

```python
from tools.bn_numbers import number_to_bangla_words, format_lakh_crore
from tools.bn_normalize import normalize
from tools.bn_lint import lint_text
from tools.bn_prosody import verify_payar
from tools.bn_legal import determine_writ_type, generate_writ_prayer

# 1. Number words
print(number_to_bangla_words(75))  # "পঁচাত্তর"

# 2. Text normalization (Bangla Academy standards + Dari)
clean_text = normalize("তিনি স্টেশন থেকে বাড়ি ফিরলেন.")
print(clean_text)  # "তিনি স্টেশন থেকে বাড়ি ফিরলেন।"

# 3. Linter diagnostics
issues = lint_text("তুমি সিদ্ধান্ত নেন")
for issue in issues:
    print(issue.message, "->", issue.suggestion)
```
