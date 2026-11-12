# eval/unit/test_before_after_benchmark.py
import unittest
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from eval.benchmarks.benchmark_evaluator import evaluate_text, SAMPLE_BASELINES

class TestBeforeAfterBenchmark(unittest.TestCase):

    def test_case1_evaluation(self):
        c1 = SAMPLE_BASELINES[1]
        res_before = evaluate_text(c1["before_sample"], 1)
        res_after = evaluate_text(c1["after_sample"], 1)

        self.assertLess(res_before["score"], 60)
        self.assertGreaterEqual(res_after["score"], 90)
        self.assertEqual(res_after["guru_chandali_count"], 0)

    def test_case2_evaluation(self):
        c2 = SAMPLE_BASELINES[2]
        res_before = evaluate_text(c2["before_sample"], 2)
        res_after = evaluate_text(c2["after_sample"], 2)

        self.assertGreater(res_before["corrupted_decimals"], 0)
        self.assertEqual(res_after["corrupted_decimals"], 0)
        self.assertGreaterEqual(res_after["score"], 95)

    def test_case3_evaluation(self):
        c3 = SAMPLE_BASELINES[3]
        res_before = evaluate_text(c3["before_sample"], 3)
        res_after = evaluate_text(c3["after_sample"], 3)

        self.assertGreater(res_before["guru_chandali_count"], 0)
        self.assertEqual(res_after["guru_chandali_count"], 0)
        self.assertGreaterEqual(res_after["score"], 95)

    def test_case4_land_registry_evaluation(self):
        c4 = SAMPLE_BASELINES[4]
        res_before = evaluate_text(c4["before_sample"], 4)
        res_after = evaluate_text(c4["after_sample"], 4)

        self.assertLess(res_before["score"], 50)
        self.assertGreaterEqual(res_after["score"], 95)
        self.assertEqual(res_after["calque_count"], 0)

    def test_case5_healthcare_clinical_evaluation(self):
        c5 = SAMPLE_BASELINES[5]
        res_before = evaluate_text(c5["before_sample"], 5)
        res_after = evaluate_text(c5["after_sample"], 5)

        self.assertGreater(res_before["corrupted_decimals"], 0)
        self.assertEqual(res_after["corrupted_decimals"], 0)
        self.assertGreaterEqual(res_after["score"], 95)
        self.assertEqual(res_after["calque_count"], 0)

if __name__ == "__main__":
    unittest.main()
