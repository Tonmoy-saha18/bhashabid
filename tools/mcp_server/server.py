# Lightweight MCP Server for Bhashabid tools
import json
from ..bn_numbers import number_to_bangla_words, format_lakh_crore
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
                "description": "Convert numbers to standard Bengali words, fractions, and South Asian grouping.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {"type": "integer", "description": "The number to convert."},
                        "format": {"type": "string", "enum": ["words", "grouped"], "default": "words"}
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
            }
        ]

    def list_tools(self) -> list[dict]:
        return self.tools

    def call_tool(self, name: str, arguments: dict) -> dict:
        if name == "convert_number":
            num = arguments.get("number", 0)
            fmt = arguments.get("format", "words")
            if fmt == "grouped":
                res = format_lakh_crore(num)
                return {"result": res}
            else:
                res = number_to_bangla_words(num)
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

        else:
            raise ValueError(f"Unknown tool: {name}")
