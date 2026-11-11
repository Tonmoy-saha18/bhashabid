import time
from dataclasses import dataclass
from typing import Iterable
from tools.bn_normalize import normalize
from tools.bn_normalize.profiles import get_profile, DialectProfile

@dataclass
class BatchMetrics:
    total_lines: int
    total_words: int
    total_chars: int
    total_changes: int
    elapsed_seconds: float
    words_per_second: float

class BatchNormalizer:
    """
    High-performance streaming batch normalizer for large Bengali text corpora.
    Applies Unicode canonicalization, orthography standardization, and Dari punctuation.
    """

    def __init__(self, profile: str | DialectProfile = "bd_standard"):
        self.profile = get_profile(profile)

    def process_stream(self, lines: Iterable[str]) -> tuple[list[str], BatchMetrics]:
        start_time = time.perf_counter()

        output_lines = []
        total_words = 0
        total_chars = 0
        total_changes = 0

        for line in lines:
            line_str = line.rstrip("\r\n")
            words_in_line = len(line_str.split())
            total_words += words_in_line
            total_chars += len(line_str)

            normalized = normalize(line_str, profile=self.profile.name)
            if normalized != line_str:
                total_changes += 1

            output_lines.append(normalized)

        elapsed = time.perf_counter() - start_time
        if elapsed <= 0:
            elapsed = 0.00001

        metrics = BatchMetrics(
            total_lines=len(output_lines),
            total_words=total_words,
            total_chars=total_chars,
            total_changes=total_changes,
            elapsed_seconds=elapsed,
            words_per_second=total_words / elapsed
        )

        return output_lines, metrics
