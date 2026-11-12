# tools/card_synthesizer.py
# Automated Knowledge Card Synthesizer & Error Clustering Engine
import os
import sys
import yaml
import glob
import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode

DRAFTS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts")
CARDS_DIR = os.path.join(REPO_ROOT, "knowledge", "cards")
REJECTED_DIR = os.path.join(REPO_ROOT, "knowledge", "cards", "rejected")

AUTHORITATIVE_DOMAIN_STANDARDS = {
    "Constitutional Law & Writs": [
        "Constitution of the People's Republic of Bangladesh (Article 102)",
        "Supreme Court of Bangladesh Judicial Precedents",
        "Bangla Academy Law Dictionary"
    ],
    "Macroeconomics & Banking": [
        "Bangladesh Bank Prudential Regulations & Monetary Policy",
        "Bangla Academy Financial & Economic Terminology",
        "The Business Standard Verified Macroeconomic Feed"
    ],
    "Healthcare & Epidemiology": [
        "Bangla Academy Medical Science Dictionary (চিকিৎসাবিজ্ঞান পরিভাষা)",
        "Directorate General of Health Services (DGHS) Bangladesh"
    ],
    "Administrative Governance & Memos": [
        "Secretariat Instructions (সচিবালয় নির্দেশমালা, জনপ্রশাসন মন্ত্রণালয়)",
        "Bangladesh Government Official Memo Standards"
    ],
    "Creative Fiction & Dialogue": [
        "Bangla Academy Standard Bengali Grammar (প্রমিত বাংলা ভাষার ব্যাকরণ)",
        "Bangla Academy Modern Bengali Dictionary (আধুনিক বাংলা অভিধান)"
    ],
    "Classical Poetry & Prosody": [
        "Rabindranath Tagore & Probodh Chandra Sen Bengali Prosody (ছন্দতত্ত্ব)",
        "Classical 14-Akshar Payar Metric Canon"
    ],
    "Academic Research & Methodology": [
        "Bangla Academy Linguistic Research Methodology Guidelines",
        "Linguistic Society of Bangladesh Peer-Reviewed Standards"
    ],
    "Land Registry & Deeds": [
        "Transfer of Property Act 1882 & Registration Act 1908",
        "Ministry of Land Official Saf-Kabala Deed Conveyancing Protocol"
    ],
    "Agronomy & Disaster Management": [
        "Ministry of Agriculture & Department of Agricultural Extension (DAE)",
        "Disaster Management Bureau Standing Orders on Disaster (SOD)"
    ],
    "ICT & Software Engineering": [
        "Bangladesh Computer Council (BCC) Bengali Computing & Unicode Standards",
        "Open-Source Bengali Localization Best Practices"
    ],
    "Education & NCTB Pedagogy": [
        "National Curriculum and Textbook Board (NCTB) Standard Bengali",
        "Ministry of Education Pedagogical Guidelines"
    ]
}

CANONICAL_DOMAIN_MAP = {
    "Judicial & High Court": "Constitutional Law & Writs",
    "Banking & Macroeconomics": "Macroeconomics & Banking",
    "Macroeconomic & Finance": "Macroeconomics & Banking",
    "Healthcare & Medicine": "Healthcare & Epidemiology",
    "Administrative Governance": "Administrative Governance & Memos",
    "Official Administrative": "Administrative Governance & Memos",
    "Poetic Prosody": "Classical Poetry & Prosody",
    "Land Conveyancing & Deeds": "Land Registry & Deeds",
    "Agronomy & Crop Protection": "Agronomy & Disaster Management",
    "Disaster Early Warning": "Agronomy & Disaster Management",
    "Education & Pedagogy": "Education & NCTB Pedagogy",
    "Science & Encyclopedic": "ICT & Software Engineering",
    "Corporate & Tech": "ICT & Software Engineering",
}

def get_domain_standards(domain: str) -> List[str]:
    canonical = CANONICAL_DOMAIN_MAP.get(domain, domain)
    return AUTHORITATIVE_DOMAIN_STANDARDS.get(
        canonical,
        ["Bangla Academy Standard Bengali Grammar", "Corpus Harvester Anomaly Detector"]
    )

class CardSynthesizer:
    """
    Automated Knowledge Card Synthesizer.
    Takes anomalies, unhandled translation calques, or domain traps harvested from real text,
    clusters recurring failure patterns, and drafts structured candidate knowledge cards for human review.
    """

    def __init__(self, drafts_dir: Optional[str] = None):
        self.drafts_dir = drafts_dir or DRAFTS_DIR
        os.makedirs(self.drafts_dir, exist_ok=True)
        os.makedirs(REJECTED_DIR, exist_ok=True)

    @staticmethod
    def get_existing_card_ids() -> set:
        existing = set()
        for f in glob.glob(os.path.join(CARDS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        for f in glob.glob(os.path.join(DRAFTS_DIR, "*.yaml")):
            stem = Path(f).stem
            existing.add(stem)
        for f in glob.glob(os.path.join(REJECTED_DIR, "*.yaml")):
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

    @staticmethod
    def find_existing_card_by_pattern(pattern: str, title: str) -> Optional[Tuple[str, Dict, str]]:
        """
        Duplicate Guard: Checks if a linguistic pattern or title is already covered
        in production cards (knowledge/cards/*.yaml), rejected cards (knowledge/cards/rejected/*.yaml),
        or existing drafts (knowledge/cards/drafts/*.yaml).
        Returns (filepath, card_dict, category) where category is 'production', 'rejected', or 'draft'.
        """
        norm_pattern = pattern.strip().lower()
        norm_title = title.strip().lower()

        # 1. Check production cards
        for f in glob.glob(os.path.join(CARDS_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                c_title = (c.get("title") or "").strip().lower()
                c_summary = (c.get("rule_summary") or "").strip().lower()
                if norm_pattern in c_title or norm_pattern in c_summary or norm_title == c_title:
                    return (f, c, "production")
            except Exception:
                continue

        # 2. Check rejected cards (prevent re-synthesizing noise rejected by human reviewers)
        for f in glob.glob(os.path.join(REJECTED_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                c_title = (c.get("title") or "").strip().lower()
                c_summary = (c.get("rule_summary") or "").strip().lower()
                if norm_pattern in c_title or norm_pattern in c_summary or norm_title == c_title:
                    return (f, c, "rejected")
            except Exception:
                continue

        # 3. Check existing draft cards
        for f in glob.glob(os.path.join(DRAFTS_DIR, "*.yaml")):
            try:
                with open(f, "r", encoding="utf-8") as yf:
                    c = yaml.safe_load(yf)
                if not c or not isinstance(c, dict):
                    continue
                c_title = (c.get("title") or "").strip().lower()
                c_summary = (c.get("rule_summary") or "").strip().lower()
                if norm_pattern in c_title or norm_pattern in c_summary or norm_title == c_title:
                    return (f, c, "draft")
            except Exception:
                continue

        return None

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
        # Internal deduplication of examples
        bads = list(dict.fromkeys([b.strip() for b in bad_examples if b and b.strip()]))
        goods = list(dict.fromkeys([g.strip() for g in good_examples if g and g.strip()]))

        cid = draft_id or self.get_next_draft_id()
        card_data = {
            "id": cid,
            "title": title,
            "domain": domain,
            "profile": "bd_standard",
            "register": register,
            "rule_summary": rule_summary,
            "good_examples": goods,
            "bad_examples": bads,
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
        Applies strict Duplicate Guard to prevent redundant card creation.
        """
        created = []
        clusters: Dict[str, List[Dict]] = {}
        for a in anomalies:
            rule_id = a.get("rule_id", "ANOMALY-GENERAL")
            matched = (a.get("matched") or a.get("raw_text") or "general").strip()
            # Group by rule_id and leading lexical token signature so distinct calques stay separated
            tokens = matched.split()
            lex_sig = " ".join(tokens[:3]) if tokens else matched
            sig = f"{rule_id}::{lex_sig}"
            if sig not in clusters:
                clusters[sig] = []
            clusters[sig].append(a)

        for sig, items in clusters.items():
            if len(items) >= 1:
                first = items[0]
                matched = first.get("matched", first.get("raw_text", "Unknown"))
                suggestion = first.get("suggestion", "")
                domain = first.get("domain", "translation")
                
                title = f"Candidate Rule for Pattern: {matched[:40]}"
                
                # DUPLICATE GUARD CHECK
                existing = self.find_existing_card_by_pattern(matched, title)
                if existing:
                    filepath, card_data, category = existing
                    if category in ["production", "rejected"]:
                        # Already covered by production or rejected by human review; skip completely
                        continue
                    else:
                        # Merge new unique examples into existing draft card
                        updated = False
                        cur_bads = card_data.get("bad_examples", []) or []
                        cur_goods = card_data.get("good_examples", []) or []
                        cur_sources = card_data.get("sources", []) or []

                        # If card was generic translation and a specific domain is detected, upgrade domain
                        if card_data.get("domain") in ["translation", "general"] and domain not in ["translation", "general"]:
                            card_data["domain"] = domain
                            updated = True

                        for it in items:
                            raw = (it.get("raw_text") or "").strip()
                            sug = (it.get("suggestion") or "").strip()
                            if raw and raw not in cur_bads and len(cur_bads) < 5:
                                cur_bads.append(raw)
                                updated = True
                            if sug and sug not in cur_goods and len(cur_goods) < 5:
                                cur_goods.append(sug)
                                updated = True

                        # Enrich with authoritative domain standards if missing
                        domain_standards = get_domain_standards(card_data.get("domain", domain))
                        for std in domain_standards:
                            if std not in cur_sources:
                                cur_sources.append(std)
                                updated = True

                        if updated:
                            card_data["bad_examples"] = cur_bads
                            card_data["good_examples"] = cur_goods
                            card_data["sources"] = cur_sources
                            card_data["last_modified"] = datetime.now().strftime("%Y-%m-%d")
                            with open(filepath, "w", encoding="utf-8") as yf:
                                yaml.dump(card_data, yf, allow_unicode=True, sort_keys=False)
                        created.append(filepath)
                        continue

                cid = self.get_next_draft_id()
                reg = "formal"
                rule_sum = f"Automatically flagged pattern '{matched}' requires naturalization to active causal phrasing (e.g. '{suggestion}')."
                bads = [it.get("raw_text", matched) for it in items[:3]]
                goods = [it.get("suggestion", "") for it in items[:3] if it.get("suggestion")]
                if not goods:
                    goods = ["প্রমিত চলিত রীতিতে স্বাভাবিকভাবে পুনর্লিখন করুন।"]

                domain_standards = get_domain_standards(domain)
                verified_sources = [
                    f"Corpus Harvest Provenance: {first.get('source', 'Authoritative Bengali Corpus')}",
                    "Principle P2 Human Provenance Audit Gate"
                ] + domain_standards

                p = self.synthesize_draft_from_anomaly(
                    title=title,
                    domain=domain,
                    register=reg,
                    rule_summary=rule_sum,
                    bad_examples=bads,
                    good_examples=goods,
                    common_llm_error=f"LLMs emit literal calques or non-standard syntax for '{matched}'.",
                    sources=verified_sources,
                    draft_id=cid
                )
                created.append(p)

        return created
