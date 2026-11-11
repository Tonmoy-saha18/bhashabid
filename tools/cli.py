# Bhashabid Developer CLI
import argparse
import sys
import os
import json

from .bn_numbers import (
    number_to_bangla_words,
    format_lakh_crore,
    format_currency_words,
    fraction_to_bangla_words,
    to_classical_ordinal,
    to_date_ordinal,
    StyleProfile
)
from .bn_normalize import normalize
from .bn_lint import lint_text

def resolve_text_or_file(text_arg: str) -> str:
    if os.path.isfile(text_arg):
        with open(text_arg, "r", encoding="utf-8") as f:
            return f.read()
    return text_arg

def handle_number(args):
    try:
        val_str = args.value.strip()
        if args.format == "grouped":
            print(format_lakh_crore(val_str))
        elif args.format == "currency":
            amount = float(val_str)
            print(format_currency_words(amount))
        elif args.format == "fraction":
            val = float(val_str)
            print(fraction_to_bangla_words(val))
        elif args.format == "ordinal":
            n = int(val_str)
            print(to_classical_ordinal(n))
        elif args.format == "date_ordinal":
            d = int(val_str)
            print(to_date_ordinal(d))
        else:
            profile = StyleProfile(hundred_style=args.hundred_style)
            if "." in val_str:
                from .bn_numbers.decimals import decimal_to_bangla_words
                print(decimal_to_bangla_words(val_str, profile=profile))
            else:
                n = int(val_str)
                print(number_to_bangla_words(n, profile=profile))
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

def handle_normalize(args):
    try:
        text = resolve_text_or_file(args.text)
        res = normalize(text, profile=args.profile)
        print(res)
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

def handle_prosody(args):
    try:
        from .bn_prosody import scan_line, verify_payar
        text = resolve_text_or_file(args.text)
        if args.verify_payar:
            res = verify_payar(text)
            print(f"পয়ার ছন্দ যাচাই: {'শুদ্ধ (VALID)' if res.is_valid_payar else 'ভগ্ন (INVALID)'}")
            print(f"পর্ব ১ (৮ মাত্রা): {res.part1_morae} | পর্ব ২ (৬ মাত্রা): {res.part2_morae} | মোট: {res.total_morae}")
            print(f"বিশ্লেষণ: {res.explanation}")
        else:
            res = scan_line(text, metre_system=args.metre)
            print(f"ছন্দোরীতি: {res.metre_system}")
            print(f"মোট মাত্রাসংখ্যা: {res.total_morae} | মোট দলসংখ্যা: {res.total_syllables} (মুক্তদল: {res.open_syllables}, রুদ্ধদল: {res.closed_syllables})")
            print(f"পর্ব বিন্যাস: {res.word_mora_breakdown}")
            print(f"ছন্দোলিপি সংকেত: {res.scansion_notation}")
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

def handle_writ(args):
    try:
        from .bn_legal import determine_writ_type, generate_writ_prayer, CONSTITUTIONAL_PROVISIONS
        wtype = determine_writ_type(args.remedy)
        prov = CONSTITUTIONAL_PROVISIONS.get(wtype, "")
        prayers = generate_writ_prayer(wtype, args.subject, args.authority)
        print(f"=== সাংবিধানিক রিট পরামর্শ (Article 102) ===")
        print(f"রিটের প্রকৃতি: {wtype.value}")
        print(f"সংবিধানিক অনুচ্ছেদ: {prov}")
        print(f"\nপ্রার্থিত প্রতিকার (Operative Prayers):")
        for idx, p in enumerate(prayers, start=1):
            print(f" {idx}. {p}")
        return 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

def handle_review(args):
    try:
        from .human_reviewer import apply_human_review
        apply_human_review(
            card_id=args.card,
            reviewer_name=args.reviewer,
            reviewer_affiliation=args.affiliation,
            action=args.action,
            notes=args.notes
        )
        return 0
    except Exception as e:
        sys.stderr.write(f"Review Error: {e}\n")
        return 1

def handle_practice(args):
    try:
        from .daily_practice_runner import run_practice_cycle
        run_practice_cycle(
            duration_minutes=args.duration_minutes,
            rounds=args.rounds,
            domain_filter=args.domain,
            continuous=args.continuous,
            auto_push=getattr(args, "push", False)
        )
        return 0
    except Exception as e:
        sys.stderr.write(f"Practice Runner Error: {e}\n")
        return 1

def handle_install_skill(args):
    try:
        from .skill_installer import install_skill
        msg = install_skill(target=args.target, workspace_dir=args.workspace, with_mcp=not getattr(args, "no_mcp", False))
        print(msg)
        return 0
    except Exception as e:
        sys.stderr.write(f"Skill Installer Error: {e}\n")
        return 1

def handle_install_mcp(args):
    try:
        from .skill_installer import install_mcp
        msg = install_mcp(target=args.target, workspace_dir=args.workspace)
        print(msg)
        return 0
    except Exception as e:
        sys.stderr.write(f"MCP Installer Error: {e}\n")
        return 1

def handle_mcp(args):
    try:
        from .mcp_server.server import BhashabidMCPServer
        srv = BhashabidMCPServer()
        srv.run_stdio()
        return 0
    except Exception as e:
        sys.stderr.write(f"MCP Server Error: {e}\n")
        return 1

def handle_harvest(args):
    try:
        from .corpus_harvester import CorpusHarvester
        harvester = CorpusHarvester(corpora_dir=args.dir)
        if args.file:
            results = harvester.harvest_file(args.file)
            print(f"Audited {len(results)} sentences from {args.file}")
        else:
            stats = harvester.harvest_all_sources()
            print("=" * 60)
            print("BHASHABID REAL-WORLD CORPUS HARVESTER & AUDITOR")
            print("=" * 60)
            print(f"Sources Scanned:       {stats['sources_scanned']}")
            print(f"Total Sentences:       {stats['total_sentences']}")
            print(f"Clean Benchmark:       {stats['benchmark_clean']} (100% Valid Native Bengali)")
            print(f"Canary Trapped:        {stats['canary_trapped']} (Flaws Caught)")
            print(f"Anomalies Flagged:     {stats['anomalies']}")
            print(f"Total Flaws Trapped:   {stats['flaws_detected']}")
            print("=" * 60)

        if args.report:
            out_p = harvester.export_summary_report(None if args.report == "default" else args.report)
            print(f"Audit report saved to: {out_p}")
        return 0
    except Exception as e:
        sys.stderr.write(f"Harvester Error: {e}\n")
        return 1

def handle_lint(args):
    try:
        text = resolve_text_or_file(args.text)
        issues = lint_text(text)
        if args.json:
            data = [
                {
                    "rule_id": i.rule_id,
                    "message": i.message,
                    "line": i.line,
                    "col": i.col,
                    "severity": i.severity.value,
                    "matched": i.matched_text,
                    "suggestion": i.suggestion
                }
                for i in issues
            ]
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            if not issues:
                print("✓ কোনো ব্যাকরণগত বা বানানজনিত ত্রুটি পাওয়া যায়নি (No issues found).")
            else:
                print(f"ত্রুটি পাওয়া গেছে ({len(issues)} issues found):")
                for i in issues:
                    print(f" - [{i.severity.value.upper()}] লাইন {i.line}, কলাম {i.col}: {i.message}")
                    if i.suggestion:
                        print(f"   পরামর্শ: {i.suggestion}")
        return 1 if any(i.severity.value == "error" for i in issues) else 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

def main():
    parser = argparse.ArgumentParser(
        prog="bhashabid",
        description="Bhashabid (ভাষাবিদ) — Open-Source Bengali Linguistic Coprocessor CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to execute")

    # number
    p_num = subparsers.add_parser("number", help="Convert numbers to Bengali words or formatted digits")
    p_num.add_argument("value", help="Number value (e.g. 99, 1234567, 3.14, 50.25)")
    p_num.add_argument("--format", choices=["words", "grouped", "currency", "fraction", "ordinal", "date_ordinal"], default="words")
    p_num.add_argument("--hundred-style", choices=["শত", "শো", "শ"], default="শত")
    p_num.set_defaults(func=handle_number)

    # normalize
    p_norm = subparsers.add_parser("normalize", help="Normalize Unicode NFC, punctuation, and loanwords")
    p_norm.add_argument("text", help="Bengali text string or path to text file")
    p_norm.add_argument("--profile", default="bd_standard", choices=["bd_standard", "wb_standard"])
    p_norm.set_defaults(func=handle_normalize)

    # lint
    p_lint = subparsers.add_parser("lint", help="Lint Bengali text for Guru-chandali, honorifics, and calques")
    p_lint.add_argument("text", help="Bengali text string or path to text file")
    p_lint.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_lint.set_defaults(func=handle_lint)

    # prosody
    p_prosody = subparsers.add_parser("prosody", help="Analyze Bengali poetic metre, scansion, and Payar conformity")
    p_prosody.add_argument("text", help="Bengali verse line")
    p_prosody.add_argument("--metre", choices=["aksharbritta", "matrabritta", "dalabritta"], default="aksharbritta")
    p_prosody.add_argument("--verify-payar", action="store_true", help="Verify 14-akshar Payar metre (8+6)")
    p_prosody.set_defaults(func=handle_prosody)

    # writ
    p_writ = subparsers.add_parser("writ", help="Generate Article 102 High Court constitutional writ prayers")
    p_writ.add_argument("--remedy", required=True, help="Remedy sought (e.g. detention, illegal order, public office)")
    p_writ.add_argument("--subject", required=True, help="Subject matter of the grievance")
    p_writ.add_argument("--authority", required=True, help="Respondent authority name")
    p_writ.set_defaults(func=handle_writ)

    # review
    p_rev = subparsers.add_parser("review", help="Human native-speaker review sign-off tool (Principle P2)")
    p_rev.add_argument("--card", required=True, help="Card ID, e.g. CRD-NUM-001")
    p_rev.add_argument("--reviewer", required=True, help="Full name of human reviewer")
    p_rev.add_argument("--affiliation", required=True, help="Reviewer qualification or affiliation")
    p_rev.add_argument("--action", default="approve", choices=["approve", "reject"])
    p_rev.add_argument("--notes", default="Verified and approved by human native speaker.")
    p_rev.set_defaults(func=handle_review)

    # practice
    p_prac = subparsers.add_parser("practice", help="Run automated multi-domain practice and learning cycle")
    p_prac.add_argument("--rounds", type=int, default=1, help="Number of complete practice rounds (default: 1)")
    p_prac.add_argument("--duration-minutes", "--minutes", "-minutes", "-m", dest="duration_minutes", type=float, default=150.0, help="Window for continuous mode (default: 150 min)")
    p_prac.add_argument("--domain", default=None, help="Filter to specific domain")
    p_prac.add_argument("--continuous", action="store_true", help="Run continuously for duration-minutes (soak test mode)")
    p_prac.add_argument("--push", action="store_true", help="Automatically commit and push post-practice updates")
    p_prac.set_defaults(func=handle_practice)

    # install-skill
    p_ins = subparsers.add_parser("install-skill", help="Install Bhashabid skill with all references to Antigravity, Claude, or Cursor")
    p_ins.add_argument("--target", choices=["antigravity", "claude", "cursor", "all"], default="all", help="Target AI environment")
    p_ins.add_argument("--workspace", default=None, help="Target workspace path (default: current directory)")
    p_ins.add_argument("--no-mcp", action="store_true", help="Skip automatic MCP server configuration")
    p_ins.set_defaults(func=handle_install_skill)

    # install-mcp
    p_ins_mcp = subparsers.add_parser("install-mcp", help="Install Bhashabid Model Context Protocol (MCP) server configuration into Cursor, Claude, or Antigravity")
    p_ins_mcp.add_argument("--target", choices=["cursor", "claude", "antigravity", "all"], default="all", help="Target AI environment")
    p_ins_mcp.add_argument("--workspace", default=None, help="Target workspace path (default: current directory)")
    p_ins_mcp.set_defaults(func=handle_install_mcp)

    # mcp
    p_mcp = subparsers.add_parser("mcp", help="Run Model Context Protocol (MCP) JSON-RPC stdio server")
    p_mcp.set_defaults(func=handle_mcp)

    # harvest
    p_harv = subparsers.add_parser("harvest", help="Ingest and audit real-world corpora from news feeds, circulars, and textbooks")
    p_harv.add_argument("--dir", default=None, help="Directory containing .jsonl corpora (default: eval/corpora/sources)")
    p_harv.add_argument("--file", default=None, help="Specific file to harvest and audit")
    p_harv.add_argument("--report", nargs="?", const="default", default=None, help="Generate markdown audit report")
    p_harv.set_defaults(func=handle_harvest)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)

if __name__ == "__main__":
    sys.exit(main())
