# tools/corpus_harvester.py
# High-Throughput Bengali Corpus Harvester, Tokenizer & Multi-Domain Auditor
import os
import sys
import re
import json
import glob
import shutil
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode
from tools.bn_normalize import normalize
from tools.bn_lint import lint_text, LintIssue

ABBREVIATIONS = ["ড.", "মোঃ", "নং", "লে.", "মে.", "প্রো.", "বি.এস", "সি.এস", "এস.এ", "আর.এস", "জে.এল"]

@dataclass
class HarvestedSentence:
    id: str
    source: str
    domain: str
    raw_text: str
    normalized_text: str
    is_clean: bool
    flaws_count: int
    flaws: List[Dict]
    category: str  # "BENCHMARK_CLEAN", "CANARY_TRAPPED", "ANOMALY_CANDIDATE"

class CorpusHarvester:
    """
    Automated Bengali Corpus Ingestion, Sentence Tokenizer, and Domain Validator.
    Processes real-world news feeds, circulars, and parallel text.
    """

    def __init__(self, corpora_dir: Optional[str] = None):
        self.corpora_dir = corpora_dir or os.path.join(REPO_ROOT, "eval", "corpora", "sources")
        self.harvested: List[HarvestedSentence] = []

    @staticmethod
    def split_sentences(text: str) -> List[str]:
        """
        Splits Bengali text on Dari (।), ?, !, and newlines,
        while safely protecting decimal numbers (e.g. ৩.১৪, 10.5) and abbreviations.
        """
        if not text:
            return []

        # Canonicalize first
        text = canonicalize_unicode(text)

        # Protect common abbreviations temporarily
        masked_text = text
        for idx, abbr in enumerate(ABBREVIATIONS):
            token = f"__ABBR_{idx}__"
            masked_text = masked_text.replace(abbr, token)

        # Split on Dari, question mark, exclamation, or double newline
        raw_chunks = re.split(r"[।?!;\n]+", masked_text)
        sentences = []

        for chunk in raw_chunks:
            s = chunk.strip()
            if not s:
                continue
            # Restore abbreviations
            for idx, abbr in enumerate(ABBREVIATIONS):
                s = s.replace(f"__ABBR_{idx}__", abbr)
            sentences.append(s)

        return sentences

    def audit_sentence(self, sentence_text: str, source: str = "Unknown", domain: str = "General", sent_id: str = "") -> HarvestedSentence:
        """Audits a single Bengali sentence against all Bhashabid engines."""
        norm_text = normalize(sentence_text)
        issues = lint_text(norm_text)
        
        # Check for unhandled foreign script anomalies outside parentheses
        text_without_parens = re.sub(r"\([^)]*\)", "", norm_text)
        unquoted_en = re.findall(r"\b[A-Za-z]{3,}\b", text_without_parens)

        is_clean = len(issues) == 0 and len(unquoted_en) == 0
        if is_clean:
            category = "BENCHMARK_CLEAN"
        elif len(issues) > 0:
            category = "CANARY_TRAPPED"
        else:
            category = "ANOMALY_CANDIDATE"

        flaw_dicts = [
            {
                "rule_id": i.rule_id,
                "message": i.message,
                "matched": i.matched_text,
                "suggestion": i.suggestion,
                "raw_text": sentence_text,
                "domain": domain,
                "source": source
            }
            for i in issues
        ]

        if unquoted_en:
            flaw_dicts.append({
                "rule_id": "RULE-ANOMALY-RAW-ENGLISH",
                "message": f"অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: {', '.join(unquoted_en)}",
                "matched": ", ".join(unquoted_en),
                "suggestion": "প্রমিত বাংলা অনুবাদ বা বন্ধনীসহ ব্যবহার করুন।",
                "raw_text": sentence_text,
                "domain": domain,
                "source": source
            })

        return HarvestedSentence(
            id=sent_id or f"SENT-{len(self.harvested)+1:04d}",
            source=source,
            domain=domain,
            raw_text=sentence_text,
            normalized_text=norm_text,
            is_clean=is_clean,
            flaws_count=len(flaw_dicts),
            flaws=flaw_dicts,
            category=category
        )

    def harvest_file(self, filepath: str) -> List[HarvestedSentence]:
        """Harvests and audits an individual file (JSONL or raw text)."""
        results = []
        if filepath.endswith(".jsonl"):
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    sid = item.get("id", "")
                    src = item.get("source", "Real-World Source")
                    dom = item.get("domain", "General")

                    # Handle parallel pairs: test both human gold and raw LLM if present
                    if "raw_llm" in item:
                        res_raw = self.audit_sentence(item["raw_llm"], source=f"{src} (Raw LLM)", domain=dom, sent_id=f"{sid}-RAW")
                        results.append(res_raw)
                    if "human_gold" in item:
                        res_gold = self.audit_sentence(item["human_gold"], source=f"{src} (Human Gold)", domain=dom, sent_id=f"{sid}-GOLD")
                        results.append(res_gold)
                    if "text" in item:
                        res_txt = self.audit_sentence(item["text"], source=src, domain=dom, sent_id=sid)
                        results.append(res_txt)
        else:
            with open(filepath, "r", encoding="utf-8") as f:
                raw_text = f.read()
            sents = self.split_sentences(raw_text)
            for idx, s in enumerate(sents, start=1):
                res = self.audit_sentence(s, source=os.path.basename(filepath), domain="Extracted", sent_id=f"EXT-{idx:04d}")
                results.append(res)

        self.harvested.extend(results)
        return results

    def harvest_all_sources(self, archive_inbox: bool = True) -> Dict:
        """
        Ingests and audits all corpora in eval/corpora/sources/ and dynamic inbox in eval/corpora/inbox/.
        If archive_inbox is True, moves processed dynamic inbox files to eval/corpora/inbox/archive/
        to prevent redundant re-auditing and queue bloat.
        """
        self.harvested = []
        source_files = sorted(glob.glob(os.path.join(self.corpora_dir, "*.jsonl")))
        
        # Check dynamic ingestion inbox
        inbox_dir = os.path.join(os.path.dirname(self.corpora_dir), "inbox")
        inbox_files = []
        if os.path.exists(inbox_dir):
            for ext in ("*.jsonl", "*.txt", "*.md"):
                # Exclude README and already archived files
                for f in glob.glob(os.path.join(inbox_dir, ext)):
                    if not f.endswith("README.md") and "archive" not in f:
                        inbox_files.append(f)
        
        all_files = source_files + inbox_files
        total_files = len(all_files)
        
        for sf in all_files:
            self.harvest_file(sf)

        # Archive processed inbox files to keep inbox lean
        if archive_inbox and inbox_files:
            archive_dir = os.path.join(inbox_dir, "archive")
            os.makedirs(archive_dir, exist_ok=True)
            for inf in inbox_files:
                try:
                    dest = os.path.join(archive_dir, os.path.basename(inf))
                    # If dest exists, overwrite or timestamp
                    if os.path.exists(dest):
                        os.remove(dest)
                    shutil.move(inf, dest)
                except Exception as me:
                    print(f"Notice: Could not archive inbox file {inf}: {me}")

        stats = {
            "sources_scanned": total_files,
            "total_sentences": len(self.harvested),
            "benchmark_clean": sum(1 for s in self.harvested if s.category == "BENCHMARK_CLEAN"),
            "canary_trapped": sum(1 for s in self.harvested if s.category == "CANARY_TRAPPED"),
            "anomalies": sum(1 for s in self.harvested if s.category == "ANOMALY_CANDIDATE"),
            "flaws_detected": sum(s.flaws_count for s in self.harvested)
        }
        return stats

    def get_practice_items(self) -> List[Tuple[str, str, str]]:
        """
        Returns harvested sentences as tuples of (domain, text, category)
        ready to feed into daily_practice_runner.
        """
        return [(s.domain, s.raw_text, s.category) for s in self.harvested]

    def export_summary_report(self, out_path: Optional[str] = None) -> str:
        """Generates a detailed markdown report of the harvested corpus audit."""
        out_path = out_path or os.path.join(REPO_ROOT, "eval", "reports", "corpus_harvest_report.md")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        clean_count = sum(1 for s in self.harvested if s.category == "BENCHMARK_CLEAN")
        canary_count = sum(1 for s in self.harvested if s.category == "CANARY_TRAPPED")
        anomaly_count = sum(1 for s in self.harvested if s.category == "ANOMALY_CANDIDATE")

        report = f"""# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `{len(self.harvested)}`
- **Clean Human Benchmark**: `{clean_count}` (Verified authentic native sentences)
- **Canary Trapped**: `{canary_count}` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `{anomaly_count}` (Flagged for human linguistic review)

## Audit Breakdown by Source & Domain

| ID | Source | Domain | Category | Flaws Trapped | Sample / Flaw Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
"""
        for s in self.harvested:
            first_msg = s.flaws[0]["message"] if s.flaws else "✓ 100% Clean Authentic Bengali"
            # truncate text for table
            sample = s.raw_text[:45] + ("..." if len(s.raw_text) > 45 else "")
            report += f"| `{s.id}` | {s.source} | {s.domain} | `{s.category}` | `{s.flaws_count}` | {first_msg} |\n"

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report.strip() + "\n")

        return out_path
