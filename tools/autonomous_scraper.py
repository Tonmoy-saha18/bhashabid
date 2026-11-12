# tools/autonomous_scraper.py
# Zero-Dependency Autonomous Web & RSS Scraper for Bengali Corpora Ingestion
import os
import sys
import re
import html
import json
import time
import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize.unicode import canonicalize_unicode

# Authoritative live RSS and open API feeds covering all 11 professional sectors of Bhashabid
DEFAULT_FEEDS = [
    # Sector 1: Constitutional Law & Writs
    {
        "name": "BBC News Bangla (Judicial & Legal)",
        "url": "https://feeds.bbci.co.uk/bengali/rss.xml",
        "domain": "Constitutional Law & Writs",
        "sector": 1
    },
    # Sector 2: Macroeconomics & Banking
    {
        "name": "The Business Standard (TBS Bangla)",
        "url": "https://www.tbsnews.net/bangla/rss.xml",
        "domain": "Macroeconomics & Banking",
        "sector": 2
    },
    {
        "name": "Prothom Alo (National & Economy)",
        "url": "https://www.prothomalo.com/feed",
        "domain": "Macroeconomics & Banking",
        "sector": 2
    },
    # Sector 3: Healthcare & Clinical Epidemiology
    {
        "name": "Bangla Wikipedia Clinical Medicine & Epidemiology",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:চিকিৎসাবিজ্ঞান") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Healthcare & Epidemiology",
        "sector": 3,
        "is_json_api": True
    },
    # Sector 4: Administrative Governance & Memos
    {
        "name": "The Daily Star Bangla (Governance & Administration)",
        "url": "https://bangla.thedailystar.net/rss.xml",
        "domain": "Administrative Governance & Memos",
        "sector": 4
    },
    # Sector 5: Creative Fiction & Dialogue
    {
        "name": "Bangla Wikipedia Bengali Literature & Fiction",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:বাংলা_সাহিত্য") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Creative Fiction & Dialogue",
        "sector": 5,
        "is_json_api": True
    },
    # Sector 6: Classical Poetry & Payar Prosody
    {
        "name": "Bangla Wikipedia Poetry & Classical Verse",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:বাংলা_কবিতা") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Classical Poetry & Prosody",
        "sector": 6,
        "is_json_api": True
    },
    # Sector 7: Academic Research & Methodology
    {
        "name": "Bangla Wikipedia Linguistics & Academic Research",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:ভাষাবিজ্ঞান") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Academic Research & Methodology",
        "sector": 7,
        "is_json_api": True
    },
    # Sector 8: Land Registry & Deeds
    {
        "name": "Bangla Wikipedia Land Law & Property Registry",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:আইন") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Land Registry & Deeds",
        "sector": 8,
        "is_json_api": True
    },
    # Sector 9: Agronomy & Disaster Management
    {
        "name": "Deutsche Welle (DW Bangla - Climate & Disaster)",
        "url": "https://rss.dw.com/rdf/rss-ben-all",
        "domain": "Agronomy & Disaster Management",
        "sector": 9
    },
    {
        "name": "Bangla Wikipedia Agriculture & Agronomy",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:বাংলাদেশের_কৃষি") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Agronomy & Disaster Management",
        "sector": 9,
        "is_json_api": True
    },
    # Sector 10: ICT & Software Engineering
    {
        "name": "Bangla Wikipedia Information Technology & Computing",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:তথ্য_প্রযুক্তি") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "ICT & Software Engineering",
        "sector": 10,
        "is_json_api": True
    },
    # Sector 11: Education & NCTB Pedagogy
    {
        "name": "Bangla Wikipedia Education & Pedagogy",
        "url": "https://bn.wikipedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=" + urllib.parse.quote("Category:শিক্ষা") + "&gcmnamespace=0&gcmlimit=4&prop=extracts&exintro=1&explaintext=1&format=json",
        "domain": "Education & NCTB Pedagogy",
        "sector": 11,
        "is_json_api": True
    }
]

USER_AGENT = "Bhashabid-Bot/2.0 (Open-Source Bengali Linguistic Coprocessor; https://github.com/ashik1291/bhashabid)"

class AutonomousScraper:
    """
    Autonomous, zero-dependency web & RSS crawler for continuous real-world
    Bengali linguistic corpora harvesting without manual folder drops.
    """

    def __init__(self, feeds: Optional[List[Dict]] = None, timeout: int = 10):
        self.feeds = feeds or DEFAULT_FEEDS
        self.timeout = timeout
        self.inbox_dir = os.path.join(REPO_ROOT, "eval", "corpora", "inbox")
        os.makedirs(self.inbox_dir, exist_ok=True)

    @staticmethod
    def sanitize_article_text(text: str) -> str:
        """Strips HTML tags, decodes entities, and removes CMS metadata headers/footers."""
        if not text:
            return ""
        clean = re.sub(r"<[^>]+>", " ", text)
        clean = html.unescape(clean)
        # Strip common CMS metadata footers
        clean = re.split(r"\b(?:Byline|News type|Publish date|Featured image|Standfirst|URL category|Tags):", clean, flags=re.IGNORECASE)[0]
        # Remove photo captions like 'ছবি: ... /টিবিএস'
        clean = re.sub(r"ছবি\s*[:;]\s*[^/\"]+/[^\s\"]+\s*\"?>?", "", clean)
        return " ".join(clean.split())

    def fetch_feed_data(self, feed: Dict) -> List[Dict]:
        """Fetches and parses a single RSS or API feed with network resilience."""
        url = feed["url"]
        name = feed["name"]
        domain = feed["domain"]
        items = []

        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/xml, application/json, text/xml;q=0.9, */*;q=0.8"
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                content_bytes = response.read()

            if feed.get("is_json_api"):
                # Handle Wikipedia / JSON API with rich article extracts
                try:
                    data = json.loads(content_bytes.decode("utf-8", errors="ignore"))
                    pages = data.get("query", {}).get("pages", {})
                    for pid, pdata in pages.items():
                        title = pdata.get("title", "")
                        extract = self.sanitize_article_text(pdata.get("extract", ""))
                        combined = f"{title}. {extract}" if extract else title
                        if combined and re.search(r"[\u0980-\u09FF]", combined):
                            # Split into substantial sentences
                            sentences = [s.strip() for s in re.split(r"[।\n]+", combined) if len(s.strip()) > 15]
                            for s in sentences[:3]:
                                items.append({
                                    "source": name,
                                    "domain": domain,
                                    "text": canonicalize_unicode(s),
                                    "notes": f"Scraped lead sentence from {name} ('{title}')"
                                })
                except Exception as je:
                    print(f"Notice: JSON API parse note for {name}: {je}")
            else:
                # Handle RSS XML with pre-cleaning for stray ampersands
                raw_text = content_bytes.decode("utf-8", errors="ignore")
                clean_xml = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;", raw_text)
                root = ET.fromstring(clean_xml.encode("utf-8"))
                channel = root.find("channel")
                raw_items = []
                if channel is not None:
                    raw_items = channel.findall("item")
                if not raw_items:
                    raw_items = root.findall(".//item")
                if not raw_items:
                    raw_items = root.findall(".//{http://purl.org/rss/1.0/}item")

                for it in raw_items[:10]:
                    title_elem = it.find("title") or it.find("{http://purl.org/rss/1.0/}title")
                    desc_elem = it.find("description") or it.find("{http://purl.org/rss/1.0/}description")
                    content_elem = it.find("{http://purl.org/rss/1.0/modules/content/}encoded")

                    title_text = self.sanitize_article_text(title_elem.text if title_elem is not None else "")
                    body_text = self.sanitize_article_text(content_elem.text if content_elem is not None and content_elem.text else (desc_elem.text if desc_elem is not None else ""))

                    combined = f"{title_text} {body_text}".strip()
                    # Only accept items containing actual Bengali graphemes
                    if re.search(r"[\u0980-\u09FF]", combined):
                        # Split into clean, non-trivial sentences (> 15 chars)
                        sentences = [s.strip() for s in re.split(r"[।\n]+", combined) if len(s.strip()) > 15]
                        for s in sentences[:2]:
                            items.append({
                                "source": name,
                                "domain": domain,
                                "text": canonicalize_unicode(s),
                                "notes": f"Live RSS lead reporting from {name}"
                            })

        except urllib.error.URLError as ue:
            print(f"[Scraper Offline Notice] Could not reach {name} ({ue.reason}). Skipping feed.")
        except Exception as ex:
            print(f"[Scraper Notice] Handled feed exception for {name}: {ex}")

        return items

    def scrape_all_feeds(self, max_items_per_feed: int = 5) -> List[Dict]:
        """Scrapes all configured feeds and extracts Bengali text snippets."""
        all_scraped = []
        print(f"\n[Autonomous Scraper] Polling {len(self.feeds)} authoritative Bengali feeds...")
        
        for feed in self.feeds:
            feed_items = self.fetch_feed_data(feed)
            if feed_items:
                selected = feed_items[:max_items_per_feed]
                all_scraped.extend(selected)
                print(f"  ✓ {feed['name']}: Ingested {len(selected)} live articles ({feed['domain']})")

        return all_scraped

    def scrape_and_save_to_inbox(self, max_items_per_feed: int = 5) -> Optional[str]:
        """
        Scrapes live feeds and persists them into eval/corpora/inbox/
        as a clean JSONL batch for the autonomous learning loop.
        """
        scraped_items = self.scrape_all_feeds(max_items_per_feed=max_items_per_feed)
        if not scraped_items:
            print("[Autonomous Scraper] No live items scraped (network offline or feeds unreachable).")
            return None

        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        filename = f"scraped_batch_{timestamp}.jsonl"
        filepath = os.path.join(self.inbox_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            for idx, item in enumerate(scraped_items, start=1):
                record = {
                    "id": f"SCRAPED-{timestamp}-{idx:03d}",
                    "source": item["source"],
                    "domain": item["domain"],
                    "text": item["text"],
                    "label": "LIVE_HARVESTED_CANDIDATE",
                    "notes": item["notes"]
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        print(f"✓ Saved {len(scraped_items)} fresh scraped sentences to inbox: {filepath}")
        return filepath

    def execute_saturation_hook(self) -> Optional[str]:
        """
        Invoked by daily_practice_runner when batch saturation is detected.
        Pulls fresh data automatically without manual folder drops.
        """
        print("\n" + "=" * 70)
        print("AUTONOMOUS SATURATION HOOK TRIGGERED: FETCHING FRESH DATA")
        print("=" * 70)
        return self.scrape_and_save_to_inbox(max_items_per_feed=3)

if __name__ == "__main__":
    scraper = AutonomousScraper()
    out = scraper.scrape_and_save_to_inbox(max_items_per_feed=3)
    if out:
        print(f"Autonomous scraping completed successfully: {out}")
    else:
        print("Autonomous scraping ended without new batch.")
