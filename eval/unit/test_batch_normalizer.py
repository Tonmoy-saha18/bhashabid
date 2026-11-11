# Unit Tests for Streaming Batch Normalizer
import unittest
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

# Import dynamically from pipeline
import importlib.util
batch_path = os.path.join(REPO_ROOT, "pipeline", "03_process", "batch_normalizer.py")
spec = importlib.util.spec_from_file_location("batch_normalizer", batch_path)
batch_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch_mod)
BatchNormalizer = batch_mod.BatchNormalizer

class TestBatchNormalizer(unittest.TestCase):

    def test_batch_processing(self):
        normalizer = BatchNormalizer(profile="bd_standard")
        lines = [
            "তিনি রেলষ্টেশনে গেলেন.",
            "গাছের ডালে পাখী ডাকে.",
            "পাই এর মান ৩.১৪ প্রায়."
        ]
        out, metrics = normalizer.process_stream(lines)

        self.assertEqual(metrics.total_lines, 3)
        self.assertEqual(metrics.total_changes, 3)
        self.assertGreater(metrics.words_per_second, 0)
        self.assertEqual(out[0], "তিনি রেলস্টেশনে গেলেন।")
        self.assertEqual(out[1], "গাছের ডালে পাখি ডাকে।")
        self.assertEqual(out[2], "পাই এর মান ৩.১৪ প্রায়।")

if __name__ == "__main__":
    unittest.main()
