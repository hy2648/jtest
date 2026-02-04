import unittest
import io
from contextlib import redirect_stdout
from gugudan import print_gugudan

class TestGugudan(unittest.TestCase):
    def test_print_gugudan(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print_gugudan()
        output = f.getvalue()

        # Check if all tables from 2 to 9 are present
        for i in range(2, 10):
            self.assertIn(f"--- {i}단 ---", output)
            for j in range(1, 10):
                self.assertIn(f"{i} x {j} = {i * j}", output)

if __name__ == "__main__":
    unittest.main()
