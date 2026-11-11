# tools/verify_provenance.py
# Audits knowledge cards against Principle P2 Provenance Integrity
import os
import glob
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def audit_provenance() -> dict:
    cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
    card_files = sorted(glob.glob(os.path.join(cards_dir, "*.yaml")))

    stats = {
        "total_cards": len(card_files),
        "data_supported": 0,
        "reviewed": 0,
        "rejected": 0,
        "p2_violations": []
    }

    for cf in card_files:
        with open(cf, "r", encoding="utf-8") as f:
            card = yaml.safe_load(f)
        
        cid = card.get("id")
        conf = card.get("confidence")

        if conf == "reviewed":
            stats["reviewed"] += 1
            rev = card.get("review")
            if not rev or not rev.get("reviewer_name") or not rev.get("reviewer_affiliation"):
                stats["p2_violations"].append(
                    f"{cid}: Marked 'reviewed' without authenticated human reviewer metadata."
                )
        elif conf == "data-supported":
            stats["data_supported"] += 1
        elif conf == "rejected":
            stats["rejected"] += 1
        else:
            stats["p2_violations"].append(
                f"{cid}: Unknown confidence tier '{conf}'."
            )

    return stats

if __name__ == "__main__":
    results = audit_provenance()
    print("=== PRINCIPLE P2 PROVENANCE INTEGRITY AUDIT ===")
    print(f"Total Cards: {results['total_cards']}")
    print(f"Data-Supported Cards: {results['data_supported']}")
    print(f"Human-Reviewed Cards: {results['reviewed']}")
    print(f"Rejected Cards: {results['rejected']}")
    if results["p2_violations"]:
        print(f"VIOLATIONS DETECTED ({len(results['p2_violations'])}):")
        for v in results["p2_violations"]:
            print(f"  ❌ {v}")
        exit(1)
    else:
        print("ALL CARDS FULLY COMPLIANT WITH PRINCIPLE P2.")
