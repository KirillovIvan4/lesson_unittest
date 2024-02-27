import unittest

from src.lesson_12_2_3 import divide

class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(50, 2), 25)
        self.assertEqual(divide(50, 10), 5)
        self.assertEqual(divide(50, 5), 10)
        self.assertEqual(divide(6.6, 2), 3.3)
        self.assertEqual(divide(100, 100), 1)


    def test_divide_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
