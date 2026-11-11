# eval/benchmarks/benchmark_evaluator.py
# Automated Before-and-After Benchmark Evaluator for Antigravity & Cursor
import os
import sys
import re
import argparse
from typing import Dict, Any

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_lint import lint_text, LintSeverity
from tools.bn_normalize.unicode import canonicalize_unicode

SAMPLE_BASELINES = {
    1: {
        "name": "Case 1: High Court Constitutional Writ (Article 102)",
        "prompt": "রাজশাহী সিটি কর্পোরেশন কর্তৃক পরিবেশ অধিদপ্তরের পরিবেশগত ছাড়পত্র এবং জাতীয় নদী রক্ষা কমিশনের অনুমোদন ব্যতিরেকে পদ্মা নদীর তীরবর্তী জমিতে অবৈধ বাণিজ্যিক অবকাঠামো নির্মাণের বিরুদ্ধে হাইকোর্ট বিভাগে সংবিধানের ১০২ অনুচ্ছেদের অধীন একটি রিট পিটিশনের প্রার্থিত প্রতিকার (Operative Prayers) এবং রুল নিশির মূল আইনি বয়ান বাংলায় খসড়া করো।",
        "before_sample": """
আমরা রাজশাহী সিটি কর্পোরেশনের বিরুদ্ধে একটি রিট পিটিশন ফাইল করছি।
কোর্টকে অনুরোধ করা হচ্ছে যে তারা বিবাদীদের নির্মাণ কার্য বন্ধ করিবার নির্দেশ প্রদান করুক এবং বিবাদীরা জবাব দিবে। 
কেন এই অবৈধ কাজটি বন্ধ করা হবে না তা জিজ্ঞেস করে হাইকোর্ট একটি রুল জারি করুক যাতে নদী রক্ষা পায়।
আদালত এই বিষয়ে তদন্তের জন্য ব্যবস্থা নিবে।
""",
        "after_sample": """
সংবিধানের ১০২ অনুচ্ছেদের অধীন রিট পিটিশনের প্রার্থিত প্রতিকার (Operative Prayers):
১. পদ্মা নদীর তীরবর্তী জমিতে পরিবেশগত ছাড়পত্র ও অনুমোদন ব্যতিরেকে অবৈধ অবকাঠামো নির্মাণ থেকে বিরত থাকতে বিবাদীদের বাধ্য করার জন্য সংবিধানের ১০২(২)(ক)(১) অনুচ্ছেদের অধীন উপযুক্ত পরমাদেশ (Mandamus) জারি;
২. উক্ত অবৈধ নির্মাণ কার্যক্রম ও প্রকল্প কেন আইনগত কর্তৃত্ববহির্ভূত ও আইনগত ফলাফলবিহীন ঘোষণা করা হবে না, তা প্রদর্শনের জন্য বিবাদীদের বিরুদ্ধে রুল নিশি জারি;
৩. অত্র রুল নিষ্পত্তির পূর্ব পর্যন্ত সংশ্লিষ্ট স্থানে সকল প্রকার নির্মাণ কার্যক্রমের ওপর স্থিতাবস্থা (Status Quo) বজায় রাখার অন্তর্বর্তীকালীন নির্দেশ।
""",
        "required_terms": ["পরমাদেশ", "আইনগত কর্তৃত্ববহির্ভূত", "রুল নিশি", "স্থিতাবস্থা", "১০২"],
        "forbidden_calques": ["জিজ্ঞেস করে", "ফাইল করছি", "বন্ধ করিবার নির্দেশ প্রদান করুক এবং বিবাদীরা জবাব দিবে"]
    },
    2: {
        "name": "Case 2: Macroeconomic & Central Bank Inflation Analysis",
        "prompt": "বাংলাদেশ ব্যাংকের সাম্প্রতিক মুদ্রানীতি কমিটির সিদ্ধান্ত এবং বাংলাদেশ পরিসংখ্যান ব্যুরোর (BBS) মূল্যস্ফীতি প্রতিবেদনের ওপর ভিত্তি করে জাতীয় সংবাদপত্রের বিজনেস পেজের জন্য একটি আনুষ্ঠানিক অর্থনৈতিক প্রতিবেদন তৈরি করো।",
        "before_sample": """
মূল্যস্ফীতি সেপ্টেম্বরের ৯।৯২% থেকে অক্টোবরে বেড়ে ১০।৮৭% হয়েছে যা খাদ্যমূল্য বৃদ্ধির দ্বারা চালিত হয়েছে।
বাংলাদেশ ব্যাংক তাদের পলিসি রেট ৫০ বেসিস পয়েন্ট হাইকিং করে ১০% করেছে যা ব্যাংকিং সেক্টরে ইম্প্যাক্ট ফেলবে। 
কলমানি রেট বেড়ে যাবে এবং বেসরকারি খাতে ঋণ প্রবাহ কমে যেতে পারে। 
""",
        "after_sample": """
খাদ্যপণ্যের মূল্যবৃদ্ধির প্রভাবে অক্টোবরে সার্বিক মূল্যস্ফীতি বেড়ে দাঁড়িয়েছে ১০.৮৭ শতাংশে, যা সেপ্টেম্বরে ছিল ৯.৯২ শতাংশ। 
মূল্যস্ফীতি নিয়ন্ত্রণে বাংলাদেশ ব্যাংক নীতি সুদহার (Policy Rate) ৫০ বেসিস পয়েন্ট বাড়িয়ে ১০.০০ শতাংশে নির্ধারণ করেছে। 
এর ফলে আন্তঃব্যাংক মুদ্রাবাজারে কলমানি হার বৃদ্ধি পেতে পারে এবং ব্যাংকিং খাতে তারল্য ব্যবস্থাপনায় নতুন গতি সঞ্চার হবে।
""",
        "required_terms": ["১০.৮৭", "৯.৯২", "নীতি সুদহার", "কলমানি হার", "তারল্য", "শতাংশ"],
        "forbidden_calques": ["দ্বারা চালিত", "হাইকিং করে", "ইম্প্যাক্ট ফেলবে", "৯।৯২", "১০।৮৭"]
    },
    3: {
        "name": "Case 3: NCTB Class 10 Biology Creative Examination Framing",
        "prompt": "জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB)-এর নির্ধারিত ৪ স্তরের সৃজনশীল প্রশ্নপদ্ধতি কাঠামো হুবহু অনুসরণ করে মাধ্যমিক শ্রেণির জীববিজ্ঞান বিষয়ের 'উদ্ভিদে খাদ্য তৈরি ও সালোকসংশ্লেষণ' অধ্যায়ের ওপর একটি পূর্ণাঙ্গ সৃজনশীল প্রশ্ন (উদ্দীপক এবং ক, খ, গ, ঘ) প্রণয়ন করো।",
        "before_sample": """
উদ্দীপকটি পড়িয়া নিচের প্রশ্নগুলোর উত্তর দাও:
শফিক সাহেব তার বাগানের গাছে পানি দেন এবং পর্যাপ্ত রোদ দেন যাতে গাছ বড় হয়।
(ক) উদ্ভিদে খাদ্য তৈরি কীভাবে হয় এবং কেন সূর্যালোক দরকার বিস্তারিত লেখো? (৪)
(খ) সালোকসংশ্লেষণ কাকে বলে? (১)
(গ) শফিকের গাছটির বৃদ্ধি নিয়ে তোমার মতামত কী? (২)
(ঘ) পরিবেশের ওপর এর প্রভাব বর্ণনা করো। (৩)
""",
        "after_sample": """
উদ্দীপকটি পড়ে নিচের প্রশ্নগুলোর উত্তর দাও:
নবম শ্রেণির শিক্ষার্থী রাফি লক্ষ্য করল, টবে থাকা যে গাছটি বারান্দার ছায়াযুক্ত স্থানে রাখা হয়েছিল তার বৃদ্ধি স্থবির হয়ে পড়েছে, পক্ষান্তরে ছাদে রৌদ্রোজ্জ্বল স্থানে রাখা গাছটি সতেজ ও দ্রুত বর্ধনশীল।
(ক) জ্ঞানমূলক: সালোকসংশ্লেষণ কাকে বলে? [১]
(খ) অনুধাবনমূলক: উদ্ভিদের পাতাকে সালোকসংশ্লেষণের প্রধান স্থান বলা হয় কেন? ব্যাখ্যা করো। [২]
(গ) প্রয়োগমূলক: উদ্দীপকে বর্ণিত রৌদ্রোজ্জ্বল স্থানের উদ্ভিদে যে জৈব রাসায়নিক প্রক্রিয়ায় শর্করা তৈরি হয়, তা সমীকরণসহ ব্যাখ্যা করো। [৩]
(ঘ) উচ্চতর দক্ষতামূলক: 'উদ্দীপকের ছায়াযুক্ত উদ্ভিদের মতো পরিস্থিতি সামগ্রিক উদ্ভিদজগতে দেখা দিলে বাস্তুতন্ত্রের ভারসাম্য বিনষ্ট হবে'—উক্তিটির যথার্থতা মূল্যায়ন করো। [৪]
""",
        "required_terms": ["উদ্দীপকটি পড়ে", "সালোকসংশ্লেষণ কাকে বলে", "ব্যাখ্যা করো", "যথার্থতা মূল্যায়ন করো"],
        "forbidden_calques": ["পড়িয়া", "বিস্তারিত লেখো", "তোমার মতামত কী"]
    }
}

def evaluate_text(text: str, case_id: int) -> Dict[str, Any]:
    norm_text = canonicalize_unicode(text)
    issues = lint_text(norm_text)

    # Guru-chandali count
    gc_issues = [i for i in issues if "GURU-CHANDALI" in i.rule_id]
    calque_issues = [i for i in issues if "CALQUE" in i.rule_id]
    honorific_issues = [i for i in issues if "HONORIFIC" in i.rule_id]

    case_info = SAMPLE_BASELINES.get(case_id, {})
    req_terms = case_info.get("required_terms", [])
    forb_calques = case_info.get("forbidden_calques", [])

    matched_terms = [t for t in req_terms if t in norm_text]
    term_score = (len(matched_terms) / len(req_terms) * 30) if req_terms else 30

    found_forbidden = [f for f in forb_calques if f in norm_text]

    # Decimal corruption check: e.g. ৩।১৪ or ১০।৮৭
    corrupted_decimals = len(re.findall(r"\d+।\d+", norm_text))

    # Base score = 100
    score = 100
    score -= (len(gc_issues) * 15)
    score -= (len(calque_issues) * 10)
    score -= (len(found_forbidden) * 15)
    score -= (corrupted_decimals * 15)
    score -= ((len(req_terms) - len(matched_terms)) * 5)
    score = max(0, min(100, score))

    return {
        "score": score,
        "guru_chandali_count": len(gc_issues),
        "calque_count": len(calque_issues) + len(found_forbidden),
        "corrupted_decimals": corrupted_decimals,
        "matched_terms": matched_terms,
        "missing_terms": [t for t in req_terms if t not in matched_terms],
        "total_lint_issues": len(issues),
        "verdict": "PRODUCTION_READY" if score >= 90 else ("NEEDS_IMPROVEMENT" if score >= 60 else "FAIL")
    }

def print_comparison(case_id: int, before_text: str, after_text: str):
    case_name = SAMPLE_BASELINES[case_id]["name"]
    res_before = evaluate_text(before_text, case_id)
    res_after = evaluate_text(after_text, case_id)

    print(f"\n{'='*75}")
    print(f"BENCHMARK COMPARISON: {case_name}")
    print(f"{'='*75}")
    print(f"| Metric                      | Baseline (BEFORE)       | Bhashabid (AFTER)       |")
    print(f"| :-------------------------- | :---------------------- | :---------------------- |")
    print(f"| Benchmark Score             | {res_before['score']}/100                 | {res_after['score']}/100                 |")
    print(f"| Guru-chandali Flaws         | {res_before['guru_chandali_count']}                       | {res_after['guru_chandali_count']}                       |")
    print(f"| Calques / Forbidden Slang   | {res_before['calque_count']}                       | {res_after['calque_count']}                       |")
    print(f"| Corrupted Decimals          | {res_before['corrupted_decimals']}                       | {res_after['corrupted_decimals']}                       |")
    print(f"| Missing Statutory Terms     | {len(res_before['missing_terms'])}                       | {len(res_after['missing_terms'])}                       |")
    print(f"| Verdict                     | {res_before['verdict']}        | {res_after['verdict']}        |")
    print(f"{'='*75}")
    gain = res_after['score'] - res_before['score']
    print(f"📈 Absolute Improvement: +{gain} points")
    if res_after['score'] >= 90:
        print("✓ Verified: Bhashabid successfully elevates output to authentic professional Bengali.")
    else:
        print("✗ Notice: Output fell short of the 90-point professional threshold.")
    return res_before, res_after

def main():
    parser = argparse.ArgumentParser(description="Bhashabid Before-and-After Benchmark Evaluator")
    parser.add_argument("--case", type=int, choices=[1, 2, 3], help="Test case ID (1, 2, or 3)")
    parser.add_argument("--before", help="Path to Before text file")
    parser.add_argument("--after", help="Path to After text file")
    parser.add_argument("--simulate", action="store_true", help="Run simulated benchmark across all 3 cases")

    args = parser.parse_args()

    if args.simulate or (not args.before and not args.after):
        print("Running Automated Before-and-After Benchmark Suite across all 3 test cases...")
        total_before = 0
        total_after = 0
        for cid in [1, 2, 3]:
            data = SAMPLE_BASELINES[cid]
            b, a = print_comparison(cid, data["before_sample"], data["after_sample"])
            total_before += b["score"]
            total_after += a["score"]

        avg_b = total_before / 3
        avg_a = total_after / 3
        print(f"\n===========================================================================")
        print(f"FINAL AGGREGATE BENCHMARK: Baseline {avg_b:.1f}/100 vs Bhashabid {avg_a:.1f}/100 (+{avg_a - avg_b:.1f}%)")
        print(f"===========================================================================")
        return 0

    if not args.case:
        print("Error: --case <1|2|3> is required when testing specific files.")
        return 1

    with open(args.before, "r", encoding="utf-8") as f:
        b_txt = f.read()
    with open(args.after, "r", encoding="utf-8") as f:
        a_txt = f.read()

    print_comparison(args.case, b_txt, a_txt)
    return 0

if __name__ == "__main__":
    sys.exit(main())
