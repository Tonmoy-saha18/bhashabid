# 🏛️ Centralized Linguistic Review Hub & GitHub PR Workflow

Welcome to the Bhashabid (ভাষাবিদ) Linguistic Review Hub. In accordance with **Principle P2 (Human Provenance)** of the Bhashabid Constitution, AI models are strictly forbidden from self-approving production rules. All rules deployed into AI agents must be authenticated by human native speakers.

This repository enables contributors, linguists, and researchers worldwide to participate in linguistic review directly through **GitHub Pull Requests (PRs)**.

---

## 🧭 How the Community Review Flow Works

```
1. Contributor / Linguist finds a candidate card in `knowledge/cards/drafts/`
                            │
                            ▼
2. Opens a GitHub PR to review, edit, or sign off on the card
                            │
                            ▼
3. Project Maintainer (@ashik1291) reviews and merges the PR
```

---

## 📋 How to Review a Card via GitHub PR

### Step 1: Browse Pending Candidate Cards
Open the central dashboard:
👉 **[`docs/review_queue/packet_001_initial_cards.md`](packet_001_initial_cards.md)**  
Look at the **`## 📥 Pending Candidate Queue`** at the top, or inspect raw files in **[`knowledge/cards/drafts/`](../../knowledge/cards/drafts/)**.

### Step 2: Choose Your Review Action

#### Option A: Submit Sign-Off via Pull Request
Fork the repository, edit the draft file (e.g. `knowledge/cards/drafts/CRD-DFT-001.yaml`), and update the `review` section:

```yaml
review:
  reviewer_name: "Your Full Name"
  reviewer_affiliation: "Your Title / Native Speaker / Organization"
  reviewed_date: "YYYY-MM-DD"
  status: APPROVED               # Options: APPROVED, REJECTED, NEEDS_REVISION
  notes: "Verified against Bangla Academy Promito standards. Examples validated."
  signature_hash: null           # Will be computed during distillation
```

#### Option B: Propose Changes or Corrections
If a rule or example is inaccurate, edit the `rule_summary`, `good_examples`, or `bad_examples` directly in the YAML file and submit your PR.

### Step 3: Open the Pull Request
Submit the PR with the title:
`review(card): approve/revise CRD-DFT-xxx - [Card Topic]`
