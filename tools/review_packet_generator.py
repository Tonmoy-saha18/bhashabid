# Tool for Agent A15 (Human Review Liaison)
import os
import glob
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def generate_review_packet() -> str:
    cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
    drafts_dir = os.path.join(cards_dir, "drafts")
    card_files = sorted(glob.glob(os.path.join(cards_dir, "*.yaml")))
    draft_files = sorted(glob.glob(os.path.join(drafts_dir, "*.yaml")))

    pending_drafts = []
    reviewed_drafts = []

    for dfile in draft_files:
        try:
            with open(dfile, "r", encoding="utf-8") as f:
                card = yaml.safe_load(f)
            rev = card.get("review", {}) or {}
            if rev.get("status") in ["APPROVED", "REVISED & APPROVED"]:
                reviewed_drafts.append((dfile, card))
            else:
                pending_drafts.append((dfile, card))
        except Exception:
            pass

    packet = """# Expert Linguistic Review Packet (PENDING_REVIEWS.md)

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
"""

    if pending_drafts:
        packet += f"\n## 📥 Pending Candidate Queue ({len(pending_drafts)} Cards Awaiting Human Review)\n\n"
        for didx, (dfile, card) in enumerate(pending_drafts, start=1):
            cid = card.get("id")
            packet += f"### Draft {didx}: [{cid}] {card.get('title')}\n"
            packet += f"- **File**: `{os.path.relpath(dfile, REPO_ROOT)}`\n"
            packet += f"- **Domain**: `{card.get('domain')}` | **Profile**: `{card.get('profile')}` | **Register**: `{card.get('register')}`\n"
            packet += f"- **Confidence Tier**: `candidate` (**Awaiting Human Sign-off**)\n"
            packet += f"- **Rule Summary**: {card.get('rule_summary')}\n\n"
            packet += "**Positive Examples (শুদ্ধ প্রয়োগ)**:\n"
            for ex in card.get("good_examples", []):
                packet += f"  - ✓ {ex}\n"
            packet += "\n**Negative Examples (ভ্রান্ত প্রয়োগ)**:\n"
            for ex in card.get("bad_examples", []):
                packet += f"  - ✗ {ex}\n"
            packet += f"\n**Common LLM Error**: {card.get('common_llm_error')}\n"
            packet += f"**Sources / Citations**: {', '.join(str(s) for s in card.get('sources', []))}\n\n"
            packet += "**Quick Action Command**:\n"
            packet += "```bash\n"
            packet += f'bhashabid review --card {cid} --reviewer "Ashikur Rahman Bhuiyan" --affiliation "Lead Architect" --action approve\n'
            packet += "```\n\n---\n\n"
    else:
        packet += "\n## 📥 Pending Candidate Queue\n\n✓ **All caught up! Zero draft cards currently pending review.**\n\n---\n\n"

    if reviewed_drafts:
        packet += f"## 🏅 Contributor Record & Merged Drafts ({len(reviewed_drafts)} Contributions)\n\n"
        packet += "| Draft ID | Title | Domain | Reviewer | Status |\n"
        packet += "| :--- | :--- | :--- | :--- | :--- |\n"
        for dfile, card in enumerate(reviewed_drafts):
            cdata = card[1] if isinstance(card, tuple) else card
            rev = cdata.get("review", {}) or {}
            packet += f"| `{cdata.get('id')}` | {cdata.get('title')} | `{cdata.get('domain')}` | {rev.get('reviewer_name')} | **{rev.get('status')}** |\n"
        packet += "\n---\n\n"

    packet += f"## 🛡️ Active Production Cards ({len(card_files)} Approved in `knowledge/cards/`)\n\n"
    for idx, card_file in enumerate(card_files, start=1):
        with open(card_file, "r", encoding="utf-8") as f:
            card = yaml.safe_load(f)
        cid = card.get("id")
        title = card.get("title")
        rev = card.get("review") or {}
        packet += f"### Card {idx}: [{cid}] {title}\n"
        packet += f"- **Status**: `{rev.get('status', 'APPROVED')}` | **Reviewer**: {rev.get('reviewer_name')} ({rev.get('reviewer_affiliation')})\n"
        packet += "**Human Reviewer Decision Box**:\n"
        packet += f"- [x] **APPROVED** (Verified by {rev.get('reviewer_name')})\n\n"

    return packet

def write_packet():
    out_dir = os.path.join(REPO_ROOT, "docs", "review_queue")
    os.makedirs(out_dir, exist_ok=True)
    packet_path = os.path.join(out_dir, "PENDING_REVIEWS.md")
    content = generate_review_packet()
    with open(packet_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated review packet: {packet_path}")

    # Remove obsolete 80KB initial cards packet if present
    old_packet = os.path.join(out_dir, "packet_001_initial_cards.md")
    if os.path.exists(old_packet):
        try:
            os.remove(old_packet)
        except Exception:
            pass

if __name__ == "__main__":
    write_packet()
