# tools/audit_duplicates.py
import os
import glob
import yaml
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def audit_cards():
    cards_dir = REPO_ROOT / "knowledge" / "cards"
    drafts_dir = cards_dir / "drafts"

    all_cards = []
    for p in sorted(cards_dir.glob("*.yaml")):
        with open(p, encoding="utf-8") as f:
            d = yaml.safe_load(f)
            all_cards.append((str(p), d))

    for p in sorted(drafts_dir.glob("*.yaml")):
        with open(p, encoding="utf-8") as f:
            d = yaml.safe_load(f)
            all_cards.append((str(p), d))

    print(f"Total cards audited: {len(all_cards)}")

    # 1. Duplicate titles
    titles = defaultdict(list)
    for path, c in all_cards:
        t = (c.get("title") or "").strip().lower()
        titles[t].append(path)

    dup_titles = {t: paths for t, paths in titles.items() if len(paths) > 1}
    print(f"\n[Duplicate Titles]: {len(dup_titles)}")
    for t, paths in dup_titles.items():
        print(f"  - Title: \"{t}\"")
        for p in paths:
            print(f"      {Path(p).name}")

    # 2. Duplicate rule summaries
    summaries = defaultdict(list)
    for path, c in all_cards:
        s = (c.get("rule_summary") or "").strip()[:80].lower()
        summaries[s].append(path)

    dup_sums = {s: paths for s, paths in summaries.items() if len(paths) > 1}
    print(f"\n[Duplicate Rule Summaries]: {len(dup_sums)}")
    for s, paths in dup_sums.items():
        print(f"  - Summary: \"{s}...\"")
        for p in paths:
            print(f"      {Path(p).name}")

    # 3. Internal duplicate examples
    internal_dups = []
    for path, c in all_cards:
        bads = c.get("bad_examples") or []
        goods = c.get("good_examples") or []
        if len(bads) != len(set(bads)):
            internal_dups.append((Path(path).name, "bad_examples", bads))
        if len(goods) != len(set(goods)):
            internal_dups.append((Path(path).name, "good_examples", goods))

    print(f"\n[Internal Duplicate Examples]: {len(internal_dups)}")
    for p, field, items in internal_dups:
        print(f"  - {p} ({field}): {items}")

def audit_references():
    ref_dir = REPO_ROOT / "skills" / "bangla-expert" / "references"
    files = list(ref_dir.glob("*.md"))
    print(f"\nTotal reference guides audited: {len(files)}")
    
    # Check duplicate lines / duplicate sections
    seen_headers = defaultdict(list)
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            line_s = line.strip()
            if line_s.startswith("#"):
                seen_headers[line_s].append((f.name, idx + 1))
    
    dup_headers = {h: locs for h, locs in seen_headers.items() if len(locs) > 1}
    print(f"[Duplicate Headers across Reference Guides]: {len(dup_headers)}")
    for h, locs in dup_headers.items():
        print(f"  - Header: \"{h}\" in {locs}")

if __name__ == "__main__":
    audit_cards()
    audit_references()
