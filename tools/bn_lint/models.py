from dataclasses import dataclass
from enum import Enum

class LintSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

@dataclass
class LintIssue:
    rule_id: str
    message: str
    line: int
    col: int
    severity: LintSeverity
    matched_text: str
    suggestion: str | None = None
