# test_calculator.py

import unittest
from task1 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- Addition Tests ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-3, -6), 3)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -2), 6)
        self.assertEqual(self.calc.multiply(-3, 2), -6)

    # --- Division Tests ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_divide_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # --- Edge Cases ---
    def test_large_numbers(self):
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(12345, 1), 12345)

    def test_divide_result_is_float(self):
        result = self.calc.divide(1, 2)
        self.assertIsInstance(result, float)

if __name__ == '__main__':
        unittest.main()
