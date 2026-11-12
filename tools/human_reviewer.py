# tools/human_reviewer.py
# Tool for Principle P2 Compliance: Human Native-Speaker Review Protocol
import os
import sys
import yaml
import hashlib
from datetime import datetime
from typing import Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def compute_card_hash(card_dict: dict) -> str:
    """Computes a SHA-256 checksum of card content excluding review metadata."""
    core = {
        "id": card_dict.get("id"),
        "title": card_dict.get("title"),
        "rule_summary": card_dict.get("rule_summary"),
        "good_examples": card_dict.get("good_examples"),
        "bad_examples": card_dict.get("bad_examples"),
        "common_llm_error": card_dict.get("common_llm_error"),
        "sources": card_dict.get("sources")
    }
    content_str = yaml.dump(core, sort_keys=True, allow_unicode=True)
    return hashlib.sha256(content_str.encode("utf-8")).hexdigest()[:16]

def apply_human_review(
    card_id: str,
    reviewer_name: str,
    reviewer_affiliation: str,
    action: str = "approve",
    notes: Optional[str] = None
) -> bool:
    """
    Applies an authenticated human native-speaker review sign-off to a knowledge card.
    Strictly enforces Principle P2: requires non-empty human name and affiliation.
    """
    if not reviewer_name or not reviewer_affiliation:
        raise ValueError("Principle P2 Violation: Reviewer name and affiliation must be provided.")

    card_path = os.path.join(REPO_ROOT, "knowledge", "cards", f"{card_id}.yaml")
    is_draft = False
    if not os.path.exists(card_path):
        draft_path = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts", f"{card_id}.yaml")
        if os.path.exists(draft_path):
            card_path = draft_path
            is_draft = True
        else:
            raise FileNotFoundError(f"Card {card_id} not found in knowledge/cards/ or knowledge/cards/drafts/")

    with open(card_path, "r", encoding="utf-8") as f:
        card = yaml.safe_load(f)

    sig_hash = compute_card_hash(card)

    if action.lower() == "approve":
        card["confidence"] = "reviewed"
        card["review"] = {
            "reviewer_name": reviewer_name.strip(),
            "reviewer_affiliation": reviewer_affiliation.strip(),
            "reviewed_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "APPROVED",
            "notes": notes or "Verified linguistic validity and cultural authenticity.",
            "signature_hash": f"sha256:{sig_hash}"
        }
        card["last_modified"] = datetime.now().strftime("%Y-%m-%d")
    elif action.lower() == "reject":
        card["confidence"] = "rejected"
        card["review"] = {
            "reviewer_name": reviewer_name.strip(),
            "reviewer_affiliation": reviewer_affiliation.strip(),
            "reviewed_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "REJECTED",
            "notes": notes or "Rejected due to linguistic defects.",
            "signature_hash": f"sha256:{sig_hash}"
        }
    else:
        raise ValueError(f"Unknown review action: {action}")

    # If approved and it was in drafts, promote it to production knowledge/cards/
    # AND preserve the draft card in knowledge/cards/drafts/ so contributors' PR history & credit remain visible
    if action.lower() == "approve" and is_draft:
        target_path = os.path.join(REPO_ROOT, "knowledge", "cards", f"{card_id}.yaml")
        with open(target_path, "w", encoding="utf-8") as f:
            yaml.dump(card, f, sort_keys=False, allow_unicode=True)
        # Keep draft updated with approval signature for public contributor record
        with open(card_path, "w", encoding="utf-8") as f:
            yaml.dump(card, f, sort_keys=False, allow_unicode=True)
        print(f"Card {card_id} successfully promoted to production knowledge/cards/ and preserved in drafts/ for contributor credit.")
    else:
        with open(card_path, "w", encoding="utf-8") as f:
            yaml.dump(card, f, sort_keys=False, allow_unicode=True)

    print(f"Card {card_id} successfully signed off as '{card['confidence']}' by {reviewer_name}.")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Human Review Sign-off Tool (Principle P2)")
    parser.add_argument("--card", required=True, help="Card ID, e.g. CRD-NUM-001")
    parser.add_argument("--reviewer", required=True, help="Full name of human reviewer")
    parser.add_argument("--affiliation", required=True, help="Institutional or native speaker qualification")
    parser.add_argument("--action", default="approve", choices=["approve", "reject"])
    parser.add_argument("--notes", default="Verified and approved by human native speaker.")

    args = parser.parse_args()
    apply_human_review(args.card, args.reviewer, args.affiliation, args.action, args.notes)
