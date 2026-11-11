# Corpus Evaluation & Throughput Benchmark
import sys
import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import importlib.util
batch_path = os.path.join(REPO_ROOT, "pipeline", "03_process", "batch_normalizer.py")
spec = importlib.util.spec_from_file_location("batch_normalizer", batch_path)
batch_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(batch_mod)
BatchNormalizer = batch_mod.BatchNormalizer

SAMPLE_CORPUS = [
    "তিনি রেলষ্টেশনে আসিয়া দেখিলেন যে গাড়ি ছাড়িয়া দিয়াছে.",
    "ডাকঘরে গিয়ে ৫০.২৫ টাকার পোষ্টাল অর্ডার পাঠালেন.",
    "গাছের ডালে পাখী গান গায় এবং বনে হাতী হাঁটে.",
    "পাই এর মান ৩.১৪ প্রায়.",
    "আপনি অনুগ্রহ করে কাজটি আজ করেন."
] * 200 # 1000 lines synthetic benchmark

def run_corpus_benchmark():
    print("Running Corpus Pipeline Evaluation...")
    normalizer = BatchNormalizer(profile="bd_standard")
    _, metrics = normalizer.process_stream(SAMPLE_CORPUS)

    print("Corpus Evaluation Metrics:")
    print(f" - Lines Processed: {metrics.total_lines:,}")
    print(f" - Words Processed: {metrics.total_words:,}")
    print(f" - Total Changes: {metrics.total_changes:,}")
    print(f" - Time Elapsed: {metrics.elapsed_seconds:.4f}s")
    print(f" - Throughput: {metrics.words_per_second:,.1f} words/sec")
    return metrics

if __name__ == "__main__":
    run_corpus_benchmark()
