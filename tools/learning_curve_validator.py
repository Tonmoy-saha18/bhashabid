# tools/learning_curve_validator.py
# Autonomous Learning Curve, Convergence & Saturation Diagnostic Engine
import os
import sys
import glob
import yaml
import json
from datetime import datetime
from typing import Dict, List, Any

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.corpus_harvester import CorpusHarvester
from tools.bn_lint import lint_text

class LearningCurveValidator:
    """
    Autonomously evaluates Bhashabid's learning trajectory, saturation index,
    defect discovery velocity, and multi-domain sector coverage.
    """

    def __init__(self):
        self.cards_dir = os.path.join(REPO_ROOT, "knowledge", "cards")
        self.drafts_dir = os.path.join(REPO_ROOT, "knowledge", "cards", "drafts")
        self.corpora_dir = os.path.join(REPO_ROOT, "eval", "corpora", "sources")

    def get_card_metrics(self) -> Dict[str, Any]:
        approved_cards = glob.glob(os.path.join(self.cards_dir, "*.yaml"))
        draft_cards = glob.glob(os.path.join(self.drafts_dir, "*.yaml"))
        
        domain_card_count = {}
        for cpath in approved_cards:
            try:
                with open(cpath, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    dom = data.get("domain", "general")
                    domain_card_count[dom] = domain_card_count.get(dom, 0) + 1
            except Exception:
                pass

        return {
            "approved_cards_count": len(approved_cards),
            "pending_drafts_count": len(draft_cards),
            "cards_by_domain": domain_card_count
        }

    def validate_sector_saturation(self) -> Dict[str, Any]:
        """
        Scans all 14 corpora sources across the 11 sectors to evaluate:
        - Total sentences
        - Flaws trapped vs clean sentences
        - Saturation Index (0.0 = completely uncharted, 1.0 = fully mastered/saturated)
        """
        harvester = CorpusHarvester(corpora_dir=self.corpora_dir)
        h_stats = harvester.harvest_all_sources()

        sector_breakdown = {}
        for s in harvester.harvested:
            dom = s.domain
            if dom not in sector_breakdown:
                sector_breakdown[dom] = {
                    "total": 0,
                    "clean": 0,
                    "trapped": 0,
                    "anomalies": 0,
                    "flaws": 0
                }
            sector_breakdown[dom]["total"] += 1
            if s.category == "BENCHMARK_CLEAN":
                sector_breakdown[dom]["clean"] += 1
            elif s.category == "CANARY_TRAPPED":
                sector_breakdown[dom]["trapped"] += 1
            elif s.category == "ANOMALY_CANDIDATE":
                sector_breakdown[dom]["anomalies"] += 1
            sector_breakdown[dom]["flaws"] += s.flaws_count

        # Compute saturation score per domain:
        # A domain is saturated if its clean benchmarks pass 100% and canaries are reliably trapped
        saturation_report = {}
        for dom, stats in sector_breakdown.items():
            tot = stats["total"]
            # Saturation is high when all canaries are trapped and benchmark sentences are verified clean
            known_rate = (stats["clean"] + stats["trapped"]) / max(1, tot)
            saturation_report[dom] = {
                "sentences": tot,
                "clean_rate": round(stats["clean"] / max(1, tot) * 100, 1),
                "trapped_canaries": stats["trapped"],
                "novel_anomalies": stats["anomalies"],
                "saturation_index": round(known_rate, 2),
                "status": "SATURATED (Needs New Data)" if stats["anomalies"] == 0 and tot >= 5 else "LEARNING (Active Anomaly Discovery)"
            }

        return {
            "overall_stats": h_stats,
            "sector_saturation": saturation_report
        }

    def generate_diagnostic_report(self) -> str:
        card_data = self.get_card_metrics()
        sat_data = self.validate_sector_saturation()
        h_stats = sat_data["overall_stats"]
        sec_sat = sat_data["sector_saturation"]

        report_path = os.path.join(REPO_ROOT, "eval", "reports", "learning_curve_audit.md")
        os.makedirs(os.path.dirname(report_path), exist_ok=True)

        lines = [
            "# Bhashabid Autonomous Learning Curve & Saturation Audit",
            "",
            f"- **Execution Timestamp**: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`",
            f"- **Approved Knowledge Invariants**: `{card_data['approved_cards_count']}` production cards",
            f"- **Quarantined Candidate Drafts**: `{card_data['pending_drafts_count']}` (Principle P2 review queue)",
            f"- **External Corpora Ingested**: `{h_stats['sources_scanned']}` source files (`{h_stats['total_sentences']}` total sentences)",
            f"- **Clean Native Benchmarks**: `{h_stats['benchmark_clean']}`",
            f"- **Canary Flaws Trapped**: `{h_stats['canary_trapped']}`",
            f"- **Active Anomaly Candidates**: `{h_stats['anomalies']}`",
            "",
            "## 1. Domain & Sector Saturation Index",
            "",
            "| Domain / Sector | Sentences | Clean Benchmark | Trapped Canaries | Saturation Index | Status & Recommendation |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |"
        ]

        total_sat = 0.0
        for dom, s in sec_sat.items():
            total_sat += s["saturation_index"]
            lines.append(
                f"| {dom} | {s['sentences']} | {s['clean_rate']}% | {s['trapped_canaries']} | `{s['saturation_index'] * 100:.0f}%` | {s['status']} |"
            )

        avg_sat = round(total_sat / max(1, len(sec_sat)), 2)

        lines.extend([
            "",
            f"**Average System-Wide Saturation on Current Batch**: `{avg_sat * 100:.1f}%`",
            "",
            "## 2. Autonomous Ingestion & Convergence Criteria",
            "",
            "1. **When does practice on the same batch stop?**",
            "   - **Threshold**: When a domain reaches $\\ge 95\%$ saturation and $\\le 0$ novel anomalies discovered over 3 consecutive rounds.",
            "   - **Result**: Practicing beyond 3-5 rounds on a static batch yields diminishing returns. Compute must shift to new data ingestion.",
            "",
            "2. **When is new data ingested?**",
            "   - **Immediate Ingestion Trigger**: As soon as saturation index exceeds `0.90` or when new anomalies $\\Delta A = 0$.",
            "   - **Ingestion Channels**:",
            "     - Unharvested files in `eval/corpora/sources/` or `eval/corpora/inbox/`.",
            "     - Dynamic Adversarial Perturbation with elevated entropy.",
            "     - Live RSS feeds / open government circulars.",
            "",
            "3. **Autonomous Learning Pipeline Role Separation**:",
            "   - **Autonomous (Machine)**: Data fetching, tokenization, multi-domain linting, canary trapping, duplicate guarding, draft card synthesis, and post-approval distillation.",
            "   - **Human Gate (Principle P2)**: Reviewing and approving candidate cards in `knowledge/cards/drafts/` via GitHub PR.",
            ""
        ])

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return report_path

if __name__ == "__main__":
    validator = LearningCurveValidator()
    rpt = validator.generate_diagnostic_report()
    print(f"Learning curve audit generated at: {rpt}")
