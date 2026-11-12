# tools/card_synthesizer.py
# Automated Knowledge Card Synthesizer & Error Clustering Engine
import os
import sys
import yaml
import glob
import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode

DRAFTS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts")
CARDS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards")

class CardSynthesizer:
    """
    Automated Knowledge Card Synthesizer.
    Takes anomalies, unhandled translation calques, or domain traps harvested from real text,
    clusters recurring failure patterns, and drafts structured candidate knowledge cards for human review.
    """

    def __init__(self, drafts_dir: Optional[str] = None):
        self.drafts_dir = drafts_dir or DRAFTS_DIR
        os.makedirs(self.drafts_dir, exist_ok=True)

    @staticmethod
    def get_existing_card_ids() -> set:
        existing = set()
        for f in glob.glob(os.path.join(CARDS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        for f in glob.glob(os.path.join(DRAFTS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        return existing

    @staticmethod
    def get_next_draft_id() -> str:
        existing = CardSynthesizer.get_existing_card_ids()
        num = 1
        while f"CRD-DFT-{num:03d}" in existing:
            num += 1
        return f"CRD-DFT-{num:03d}"

    def synthesize_draft_from_anomaly(
        self,
        title: str,
        domain: str,
        register: str,
        rule_summary: str,
        bad_examples: List[str],
        good_examples: List[str],
        common_llm_error: str,
        sources: List[str],
        draft_id: Optional[str] = None
    ) -> str:
        cid = draft_id or self.get_next_draft_id()
        card_data = {
            "id": cid,
            "title": title,
            "domain": domain,
            "profile": "bd_standard",
            "register": register,
            "rule_summary": rule_summary,
            "good_examples": good_examples,
            "bad_examples": bad_examples,
            "common_llm_error": common_llm_error,
            "sources": sources,
            "confidence": "candidate",
            "created_date": "2026-11-12",
            "last_modified": "2026-11-12",
            "review": {
                "reviewer_name": None,
                "reviewer_affiliation": None,
                "reviewed_date": None,
                "status": "PENDING_HUMAN_REVIEW",
                "notes": "Candidate card synthesized by Bhashabid Autonomous Learning Loop. Pending human native-speaker sign-off.",
                "signature_hash": None
            }
        }

        out_path = os.path.join(self.drafts_dir, f"{cid}.yaml")
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.dump(card_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

        return out_path

    def cluster_and_synthesize_anomalies(self, anomalies: List[Dict]) -> List[str]:
        """
        Clusters a list of harvested anomalies and generates draft cards.
        """
        created = []
        # Group by failure signature or pattern
        clusters: Dict[str, List[Dict]] = {}
        for a in anomalies:
            sig = a.get("rule_id", "ANOMALY-GENERAL")
            if sig not in clusters:
                clusters[sig] = []
            clusters[sig].append(a)

        for sig, items in clusters.items():
            if len(items) >= 1:
                first = items[0]
                matched = first.get("matched", first.get("raw_text", "Unknown"))
                suggestion = first.get("suggestion", "")
                
                cid = self.get_next_draft_id()
                title = f"Candidate Rule for Pattern: {matched[:40]}"
                domain = first.get("domain", "translation")
                reg = "formal"
                rule_sum = f"Automatically flagged pattern '{matched}' requires naturalization to '{suggestion}'."
                bads = [it.get("raw_text", matched) for it in items[:3]]
                goods = [it.get("suggestion", "") for it in items[:3] if it.get("suggestion")]
                if not goods:
                    goods = ["প্রমিত চলিত রীতিতে স্বাভাবিকভাবে পুনর্লিখন করুন।"]

                p = self.synthesize_draft_from_anomaly(
                    title=title,
                    domain=domain,
                    register=reg,
                    rule_summary=rule_sum,
                    bad_examples=bads,
                    good_examples=goods,
                    common_llm_error=f"LLMs emit literal calques or non-standard syntax for '{matched}'.",
                    sources=["Corpus Harvester Anomaly Detector", "Bangla Academy Corpus"],
                    draft_id=cid
                )
                created.append(p)

        return created
