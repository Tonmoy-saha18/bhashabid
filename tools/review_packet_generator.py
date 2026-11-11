# Tool for Agent A15 (Human Review Liaison)
import os
import glob
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def generate_review_packet() -> str:
    cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
    card_files = sorted(glob.glob(os.path.join(cards_dir, "*.yaml")))

    packet = """# Expert Linguistic Review Packet (Review Packet #001)

Prepared by: **Agent A15 (Human Review Liaison)**  
Target Reviewers: **Native Bengali Linguistic Experts**  
Standard: **Bangla Academy (Dhaka) & Paschimbanga Bangla Akademi (Kolkata)**  

> [!IMPORTANT]
> In accordance with Principle P2 of the Bhashabid Constitution, agents may NEVER mark knowledge cards as 'reviewed'. Only recorded, signed human native-speaker reviews may elevate card confidence from `data-supported` to `reviewed`.

---

## Instructions for Human Reviewers
1. Verify the linguistic validity of each rule summary, positive examples, and counter-examples.
2. Check for regional balance across Bangladesh standard and West Bengal conventions.
3. Provide sign-off handle, affiliation, and status: `APPROVED` | `NEEDS_REVISION` | `REJECTED`.

---

## Review Queue Cards

"""
    for idx, card_file in enumerate(card_files, start=1):
        with open(card_file, "r", encoding="utf-8") as f:
            card = yaml.safe_load(f)

        packet += f"### Card {idx}: [{card.get('id')}] {card.get('title')}\n"
        packet += f"- **Domain**: `{card.get('domain')}` | **Profile**: `{card.get('profile')}` | **Register**: `{card.get('register')}`\n"
        packet += f"- **Confidence Tier**: `{card.get('confidence')}` (Candidate for Human Review)\n"
        packet += f"- **Rule Summary**: {card.get('rule_summary')}\n\n"

        packet += "**Positive Examples (শুদ্ধ প্রয়োগ)**:\n"
        for ex in card.get("good_examples", []):
            packet += f"  - ✓ {ex}\n"

        packet += "\n**Negative Examples (ভ্রান্ত প্রয়োগ)**:\n"
        for ex in card.get("bad_examples", []):
            packet += f"  - ✗ {ex}\n"

        packet += f"\n**Common LLM Error**: {card.get('common_llm_error')}\n"
        packet += f"**Sources / Citations**: {', '.join(card.get('sources', []))}\n\n"

        packet += "**Human Reviewer Decision Box**:\n"
        packet += "- [ ] **APPROVED** (Elevate to `reviewed`)\n"
        packet += "- [ ] **REVISE** (Needs amendment)\n"
        packet += "- *Reviewer Handle / Name*: ____________________\n"
        packet += "- *Reviewer Notes*: ____________________\n\n"
        packet += "---\n\n"

    return packet

def write_packet():
    out_dir = os.path.join(REPO_ROOT, "docs", "review_queue")
    os.makedirs(out_dir, exist_ok=True)
    packet_path = os.path.join(out_dir, "packet_001_initial_cards.md")
    content = generate_review_packet()
    with open(packet_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated review packet: {packet_path}")

if __name__ == "__main__":
    write_packet()
