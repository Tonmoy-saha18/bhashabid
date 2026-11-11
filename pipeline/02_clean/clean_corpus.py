# Pipeline Step 2: Clean corpus using bn_normalize
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from tools.bn_normalize import normalize

def clean_corpus_text(raw_text: str) -> str:
    """Applies Bhashabid normalizer to corpus samples."""
    return normalize(raw_text, profile="bd_standard")
