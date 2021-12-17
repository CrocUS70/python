from builder import *
from unittest import TestCase
from unittest.mock import patch

class TestCost(TestCase):
    @patch('builder.sum_cost', return_value=150000)
    def test_sum_cost(self, x):
        self.assertEqual(sum_cost(0), 150000)