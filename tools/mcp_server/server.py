# Lightweight MCP Server for Bhashabid tools
import json
from ..bn_numbers import (
    number_to_bangla_words,
    decimal_to_bangla_words,
    format_lakh_crore,
    format_currency_words,
    to_ascii_digits
)
from ..bn_normalize import normalize
from ..bn_lint import lint_text

class BhashabidMCPServer:
    """
    Model Context Protocol (MCP) compatible server exposing Bhashabid deterministic tools:
    - convert_number: Converts digits to Bengali words and South Asian comma formats.
    - normalize_text: Canonicalizes Bengali text to NFC and standard orthography.
    - lint_text: Detects Guru-chandali, honorific clashes, and calques.
    """

    def __init__(self):
        self.tools = [
            {
                "name": "convert_number",
                "description": "Convert integers, floating-point decimals, fractions, ordinals, and currencies into standard Bengali words, fractions, ordinals, or South Asian lakh/crore comma grouping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {"description": "The number to convert (integer, float, or string like '89079490.7890' or '৮৯০৭৯৪৯০.৭৮৯০')."},
                        "format": {"type": "string", "enum": ["words", "grouped", "currency", "fraction", "ordinal", "date_ordinal"], "default": "words"}
                    },
                    "required": ["number"]
                }
            },
            {
                "name": "normalize_text",
                "description": "Normalize Bengali text: Unicode NFC, Dari punctuation, and Bangla Academy orthography.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The raw Bengali text to normalize."},
                        "profile": {"type": "string", "default": "bd_standard"}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "lint_text",
                "description": "Lint Bengali text for Guru-chandali (Sadhu-Cholito mixing), honorific clashes, and calques.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali text to lint."}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "prosody_scan",
                "description": "Scan Bengali verse for poetic metre (Payar, Matrabritta, Dalabritta) and verify caesura and rhyme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string", "description": "The Bengali verse line."},
                        "metre": {"type": "string", "enum": ["aksharbritta", "matrabritta", "dalabritta"], "default": "aksharbritta"},
                        "verify_payar": {"type": "boolean", "default": False}
                    },
                    "required": ["text"]
                }
            },
            {
                "name": "generate_writ_prayer",
                "description": "Generate Article 102 High Court constitutional writ prayers in statutory Bengali.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remedy": {"type": "string", "description": "Core remedy (e.g. detention, illegal order, public office)."},
                        "subject": {"type": "string", "description": "Subject matter of the grievance."},
                        "authority": {"type": "string", "description": "Respondent authority name."}
                    },
                    "required": ["remedy", "subject", "authority"]
                }
            }
        ]

    def list_tools(self) -> list[dict]:
        return self.tools

    def call_tool(self, name: str, arguments: dict) -> dict:
        if name == "convert_number":
            raw_val = str(arguments.get("number", 0)).strip()
            fmt = arguments.get("format", "words")
            val_ascii = to_ascii_digits(raw_val)
            if fmt == "grouped":
                res = format_lakh_crore(val_ascii)
                return {"result": res}
            elif fmt == "currency":
                res = format_currency_words(float(val_ascii))
                return {"result": res}
            elif fmt == "fraction":
                from ..bn_numbers import fraction_to_bangla_words
                res = fraction_to_bangla_words(float(val_ascii))
                return {"result": res}
            elif fmt == "ordinal":
                from ..bn_numbers import to_classical_ordinal
                res = to_classical_ordinal(int(val_ascii))
                return {"result": res}
            elif fmt == "date_ordinal":
                from ..bn_numbers import to_date_ordinal
                res = to_date_ordinal(int(val_ascii))
                return {"result": res}
            else:
                if "." in val_ascii:
                    res = decimal_to_bangla_words(val_ascii)
                else:
                    res = number_to_bangla_words(int(val_ascii))
                return {"result": res}

        elif name == "normalize_text":
            raw_text = arguments.get("text", "")
            profile = arguments.get("profile", "bd_standard")
            res = normalize(raw_text, profile=profile)
            return {"result": res}

        elif name == "lint_text":
            raw_text = arguments.get("text", "")
            issues = lint_text(raw_text)
            diagnostics = [
                {
                    "rule_id": issue.rule_id,
                    "message": issue.message,
                    "line": issue.line,
                    "col": issue.col,
                    "severity": issue.severity.value,
                    "matched": issue.matched_text,
                    "suggestion": issue.suggestion
                }
                for issue in issues
            ]
            return {"issues": diagnostics, "issue_count": len(diagnostics)}

        elif name == "prosody_scan":
            from ..bn_prosody import scan_line, verify_payar
            raw_text = arguments.get("text", "")
            metre = arguments.get("metre", "aksharbritta")
            if arguments.get("verify_payar", False):
                res = verify_payar(raw_text)
                return {
                    "is_valid_payar": res.is_valid_payar,
                    "part1_morae": res.part1_morae,
                    "part2_morae": res.part2_morae,
                    "total_morae": res.total_morae,
                    "explanation": res.explanation
                }
            else:
                res = scan_line(raw_text, metre_system=metre)
                return {
                    "metre_system": res.metre_system,
                    "total_morae": res.total_morae,
                    "total_syllables": res.total_syllables,
                    "open_syllables": res.open_syllables,
                    "closed_syllables": res.closed_syllables,
                    "word_mora_breakdown": res.word_mora_breakdown,
                    "scansion_notation": res.scansion_notation
                }

        elif name == "generate_writ_prayer":
            from ..bn_legal import determine_writ_type, generate_writ_prayer, CONSTITUTIONAL_PROVISIONS
            rem = arguments.get("remedy", "")
            subj = arguments.get("subject", "")
            auth = arguments.get("authority", "")
            wtype = determine_writ_type(rem)
            prayers = generate_writ_prayer(wtype, subj, auth)
            return {
                "writ_type": wtype.value,
                "constitutional_article": CONSTITUTIONAL_PROVISIONS.get(wtype, ""),
                "prayers": prayers
            }

        else:
            raise ValueError(f"Unknown tool: {name}")

    def run_stdio(self):
        """
        Runs standard JSON-RPC 2.0 stdio server loop for Model Context Protocol (MCP) clients
        (Claude Desktop, Cursor, Antigravity, Windsurf).
        """
        import sys
        for raw_line in sys.stdin:
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                msg = json.loads(raw_line)
                msg_id = msg.get("id")
                method = msg.get("method")
                params = msg.get("params", {})

                if method == "initialize":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {
                                "tools": {}
                            },
                            "serverInfo": {
                                "name": "bhashabid-mcp",
                                "version": "1.0.0"
                            }
                        }
                    }
                elif method in ("notifications/initialized", "initialized"):
                    continue
                elif method == "tools/list":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "tools": [
                                {
                                    "name": t["name"],
                                    "description": t["description"],
                                    "inputSchema": t["parameters"]
                                }
                                for t in self.list_tools()
                            ]
                        }
                    }
                elif method == "tools/call":
                    tool_name = params.get("name")
                    args = params.get("arguments", {})
                    out = self.call_tool(tool_name, args)
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps(out, ensure_ascii=False, indent=2)
                                }
                            ]
                        }
                    }
                elif method == "ping":
                    resp = {"jsonrpc": "2.0", "id": msg_id, "result": {}}
                else:
                    resp = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "error": {"code": -32601, "message": f"Method {method} not found"}
                    }
                sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
                sys.stdout.flush()
            except Exception as ex:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": msg.get("id") if "msg" in locals() else None,
                    "error": {"code": -32603, "message": str(ex)}
                }
                sys.stdout.write(json.dumps(err_resp, ensure_ascii=False) + "\n")
                sys.stdout.flush()

def main():
    srv = BhashabidMCPServer()
    srv.run_stdio()

if __name__ == "__main__":
    main()
