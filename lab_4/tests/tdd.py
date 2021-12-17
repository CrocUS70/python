import unittest
import sys, os

sys.path.append(os.getcwd())
from builder import *

class TestCost(unittest.TestCase):

    def test_cost(self):
        self.assertEqual(check_cost("ASUS TUF"), 100000)

if __name__ == "__main__":
    unittest.main()