# tools/learning_benchmark_ledger.py
# Cumulative Empirical Learning Ledger & Sector Benchmark Tracker
import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEDGER_PATH = os.path.join(REPO_ROOT, "state", "learning_benchmark_ledger.json")
REPORT_PATH = os.path.join(REPO_ROOT, "eval", "reports", "learning_ledger.md")

DEFAULT_SECTORS = [
    "Constitutional Law & Writs",
    "Macroeconomics & Banking",
    "Healthcare & Epidemiology",
    "Administrative Governance & Memos",
    "Creative Fiction & Dialogue",
    "Classical Poetry & Prosody",
    "Academic Research & Methodology",
    "Land Registry & Deeds",
    "Agronomy & Disaster Management",
    "ICT & Software Engineering",
    "Education & NCTB Pedagogy"
]

SECTOR_ALIASES = {
    "judicial": "Constitutional Law & Writs",
    "court": "Constitutional Law & Writs",
    "writ": "Constitutional Law & Writs",
    "law": "Constitutional Law & Writs",
    "constitution": "Constitutional Law & Writs",
    "tax": "Macroeconomics & Banking",
    "customs": "Macroeconomics & Banking",
    "finance": "Macroeconomics & Banking",
    "bank": "Macroeconomics & Banking",
    "economy": "Macroeconomics & Banking",
    "health": "Healthcare & Epidemiology",
    "medicine": "Healthcare & Epidemiology",
    "clinical": "Healthcare & Epidemiology",
    "admin": "Administrative Governance & Memos",
    "govern": "Administrative Governance & Memos",
    "memo": "Administrative Governance & Memos",
    "fiction": "Creative Fiction & Dialogue",
    "literature": "Creative Fiction & Dialogue",
    "dialogue": "Creative Fiction & Dialogue",
    "sports": "Creative Fiction & Dialogue",
    "poetry": "Classical Poetry & Prosody",
    "prosody": "Classical Poetry & Prosody",
    "payar": "Classical Poetry & Prosody",
    "research": "Academic Research & Methodology",
    "linguistics": "Academic Research & Methodology",
    "academic": "Academic Research & Methodology",
    "science": "Academic Research & Methodology",
    "land": "Land Registry & Deeds",
    "deed": "Land Registry & Deeds",
    "conveyanc": "Land Registry & Deeds",
    "agronomy": "Agronomy & Disaster Management",
    "disaster": "Agronomy & Disaster Management",
    "crop": "Agronomy & Disaster Management",
    "climate": "Agronomy & Disaster Management",
    "tech": "ICT & Software Engineering",
    "software": "ICT & Software Engineering",
    "computing": "ICT & Software Engineering",
    "ict": "ICT & Software Engineering",
    "education": "Education & NCTB Pedagogy",
    "pedagogy": "Education & NCTB Pedagogy",
    "nctb": "Education & NCTB Pedagogy",
    "textbook": "Education & NCTB Pedagogy"
}

def normalize_sector_name(sec_name: str) -> str:
    s = sec_name.lower().strip()
    for std_sec in DEFAULT_SECTORS:
        if std_sec.lower() in s or s in std_sec.lower():
            return std_sec
    for kw, target_sec in SECTOR_ALIASES.items():
        if kw in s:
            return target_sec
    return sec_name

class LearningBenchmarkLedger:
    """
    Persistent research-grade audit ledger tracking Bhashabid's cumulative learning progression:
    - Total data volume practiced & learned across time
    - Sentence distribution across all 11 professional sectors
    - Empirical confidence & accuracy growth timeline
    - Fresh data ingestion history
    """

    def __init__(self, ledger_path: Optional[str] = None):
        self.ledger_path = ledger_path or LEDGER_PATH
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        data = {
            "version": "1.0.0",
            "first_initialized": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "cumulative_practice_sessions": 0,
            "cumulative_rounds_completed": 0,
            "cumulative_sentences_practiced": 0,
            "cumulative_checks_evaluated": 0,
            "cumulative_flaws_trapped": 0,
            "cumulative_fresh_batches_ingested": 0,
            "sector_sentence_distribution": {sec: 0 for sec in DEFAULT_SECTORS},
            "confidence_milestones": []
        }
        if os.path.exists(self.ledger_path):
            try:
                with open(self.ledger_path, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    data.update(loaded)
            except Exception:
                pass

        # Consolidate sector sentence distribution into the 11 canonical sectors
        consolidated = {sec: 0 for sec in DEFAULT_SECTORS}
        for sec, count in data.get("sector_sentence_distribution", {}).items():
            norm_sec = normalize_sector_name(sec)
            consolidated[norm_sec] = consolidated.get(norm_sec, 0) + count
        data["sector_sentence_distribution"] = consolidated
        return data

    def save(self):
        os.makedirs(os.path.dirname(self.ledger_path), exist_ok=True)
        self.data["last_updated"] = datetime.now().isoformat()
        with open(self.ledger_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def record_practice_session(
        self,
        rounds: int,
        total_checks: int,
        sentences_practiced: int,
        flaws_trapped: int,
        sector_counts: Optional[Dict[str, int]] = None
    ):
        self.data["cumulative_practice_sessions"] += 1
        self.data["cumulative_rounds_completed"] += rounds
        self.data["cumulative_checks_evaluated"] += total_checks
        self.data["cumulative_sentences_practiced"] += sentences_practiced
        self.data["cumulative_flaws_trapped"] += flaws_trapped

        if sector_counts:
            for sec, count in sector_counts.items():
                key = normalize_sector_name(sec)
                self.data["sector_sentence_distribution"][key] = (
                    self.data["sector_sentence_distribution"].get(key, 0) + count
                )

        self.save()

    def record_confidence_milestone(
        self,
        round_idx: int,
        saturation_score: float,
        clean_precision: float,
        batch_size: int,
        new_batch_ingested: Optional[str] = None
    ):
        milestone = {
            "timestamp": datetime.now().isoformat(),
            "round": round_idx,
            "saturation_score": round(saturation_score, 4),
            "clean_precision": round(clean_precision, 4),
            "batch_size": batch_size,
            "status": "CONFIDENT_BATCH_MASTERED",
            "new_batch_ingested": os.path.basename(new_batch_ingested) if new_batch_ingested else None
        }
        if new_batch_ingested:
            self.data["cumulative_fresh_batches_ingested"] += 1

        self.data["confidence_milestones"].append(milestone)
        self.save()

    def export_research_report(self, report_path: Optional[str] = None) -> str:
        report_path = report_path or REPORT_PATH
        os.makedirs(os.path.dirname(report_path), exist_ok=True)

        d = self.data
        total_sents = d["cumulative_sentences_practiced"]
        total_flaws = d["cumulative_flaws_trapped"]
        overall_prec = round((1.0 - (total_flaws / max(1, d["cumulative_checks_evaluated"]))) * 100, 2)

        lines = [
            "# Bhashabid Research Learning Ledger & Multi-Sector Benchmark",
            "",
            "> **Autonomous Supervised Learning Audit**: Empirical record of data volume practiced, sector coverage, confidence saturation, and accuracy growth over time.",
            "",
            "## 1. Executive Summary & Aggregate Metrics",
            "",
            f"- **Cumulative Practice Sessions**: `{d['cumulative_practice_sessions']}`",
            f"- **Cumulative Practice Rounds Completed**: `{d['cumulative_rounds_completed']}`",
            f"- **Total Sentences Practiced & Learned**: `{total_sents:,}`",
            f"- **Total Linguistic Checks Evaluated**: `{d['cumulative_checks_evaluated']:,}`",
            f"- **Total Anomalies / Flaws Trapped**: `{total_flaws:,}`",
            f"- **Fresh Live Batches Ingested on Saturation**: `{d['cumulative_fresh_batches_ingested']}`",
            f"- **System Overall Linguistic Precision**: `{overall_prec}%`",
            "",
            "## 2. All 11 Professional Sectors Coverage",
            "",
            "| # | Professional Sector | Cumulative Sentences Practiced | Coverage Status |",
            "| :-: | :--- | :---: | :---: |"
        ]

        sec_dist = d["sector_sentence_distribution"]
        for idx, sec in enumerate(DEFAULT_SECTORS, start=1):
            count = sec_dist.get(sec, 0)
            status = "✓ Fully Practiced" if count >= 100 else ("⚡ Actively Learning" if count > 0 else "○ Seed Baseline")
            lines.append(f"| {idx} | {sec} | {count:,} | {status} |")

        lines.extend([
            "",
            "## 3. Confidence Milestones & Learning Progression",
            "",
            "| Timestamp | Round | Saturation Score | Clean Precision | Action / Fresh Data Streamed |",
            "| :--- | :---: | :---: | :---: | :--- |"
        ])

        for m in d["confidence_milestones"][-15:]:
            act = f"Ingested `{m['new_batch_ingested']}`" if m.get("new_batch_ingested") else "Batch Confident (Mastered)"
            lines.append(
                f"| `{m['timestamp'][:19]}` | {m['round']} | `{m['saturation_score']*100:.1f}%` | `{m['clean_precision']*100:.1f}%` | {act} |"
            )

        if not d["confidence_milestones"]:
            lines.append("| *Awaiting first multi-round continuous practice milestone...* | - | - | - | - |")

        lines.extend([
            "",
            "---",
            f"*Generated by Bhashabid Autonomous Learning Protocol at `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`.*"
        ])

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return report_path
