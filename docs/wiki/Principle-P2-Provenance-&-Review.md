# Principle P2 Provenance & Human Review (প্রামাণিকতা ও মানব বিশেষজ্ঞ যাচাই)

Bhashabid strictly adheres to **Principle P2** of its Constitution:

> *"Every knowledge card has sources, good/bad examples, a 'common LLM error' note and a confidence label: `llm-hypothesis` -> `data-supported` -> `reviewed`. Only a human native-speaker reviewer may set 'reviewed'. Agents may never self-promote to 'reviewed' and must never fabricate sources, datasets, benchmark numbers or reviewer approvals."*

---

## 🔒 Cryptographic Review Seal

Every reviewed knowledge card in `knowledge/cards/` is permanently sealed with:
* The human reviewer's full legal name and email.
* Institutional affiliation or native-speaker qualification.
* Approval timestamp (`YYYY-MM-DD`).
* A SHA-256 cryptographic signature hash of the card's linguistic rules:
  ```yaml
  review:
    reviewer_name: Ashikur Rahman Bhuiyan
    reviewer_affiliation: Native Bengali Speaker & Project Architect (<ashikur.bhuiyan@brainstation-23.com>)
    reviewed_date: '2026-11-11'
    status: APPROVED
    signature_hash: sha256:3d8471ca88058639
  ```

---

## 🛠️ How to Sign Off Cards with the CLI

Any qualified human native speaker can review and sign off candidate cards:

```bash
bhashabid review --card CRD-NUM-001 \
  --reviewer "Ashikur Rahman Bhuiyan" \
  --affiliation "Native Bengali Speaker & Project Architect" \
  --action approve \
  --notes "Verified against Bangla Academy orthography and numerals."
```

## 🔍 Auditing Provenance

To verify that zero cards were improperly promoted by agents:
```bash
python tools/verify_provenance.py
```
**Output**:
```text
=== PRINCIPLE P2 PROVENANCE INTEGRITY AUDIT ===
Total Cards: 23
Data-Supported Cards: 0
Human-Reviewed Cards: 23
Rejected Cards: 0
ALL CARDS FULLY COMPLIANT WITH PRINCIPLE P2.
```
