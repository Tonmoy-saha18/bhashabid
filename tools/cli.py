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

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)

if __name__ == "__main__":
    sys.exit(main())
