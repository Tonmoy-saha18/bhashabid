# eval/unit/test_kill_switch.py
import unittest
import os
import tempfile

class TestKillSwitch(unittest.TestCase):
    def test_kill_switch_detection(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            stop_file = os.path.join(tmpdir, "STOP")
            self.assertFalse(os.path.exists(stop_file))
            
            # Helper function that mimics loop check
            def should_halt(dir_path: str) -> bool:
                return os.path.exists(os.path.join(dir_path, "STOP"))
                
            self.assertFalse(should_halt(tmpdir))
            
            # Create stop file
            with open(stop_file, "w") as f:
                f.write("HALT")
                
            self.assertTrue(should_halt(tmpdir))

if __name__ == "__main__":
    unittest.main()
