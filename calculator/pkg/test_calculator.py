# pkg/test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("2 + 3"), 5.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5 - 2"), 3.0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("4 * 3"), 12.0)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("6 / 2"), 3.0)

    def test_precedence(self):
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14.0)
        self.assertEqual(self.calculator.evaluate("2 * 3 + 4"), 10.0)
        self.assertEqual(self.calculator.evaluate("10 / 2 - 1"), 4.0)
        self.assertEqual(self.calculator.evaluate("10 - 2 / 1"), 8.0)

    def test_multiple_operators(self):
         self.assertEqual(self.calculator.evaluate("2 + 3 * 4 / 2 - 1"), 7.0)

if __name__ == '__main__':
    unittest.main()