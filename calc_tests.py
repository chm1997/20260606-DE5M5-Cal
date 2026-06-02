import unittest
from calc import Calculator

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(8, 2)
        return super().setUp()

    def test_sum(self):
        self.assertEqual(self.calculator.get_sum(), 10, "The answer was not 10")
    
    def test_sub(self):
        self.assertEqual(self.calculator.get_sub(), 9, "The answer was not 10")
    
    def test_mult(self):
        self.assertEqual(self.calculator.get_mult(), 16, "The answer was not 10")
    
    def test_div(self):
        self.assertEqual(self.calculator.get_div(), 4, "The answer was not 4")

unittest.main()