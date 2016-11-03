import unittest
from clinic import calc

"""Unit tests"""
class TestTry1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.try_1(5,4,'add'), 9)

    def test_sub(self):
        self.assertEqual(calc.try_1(3,5, 'sub'), -2)

    def test_mul(self):
        self.assertEqual(calc.try_1(5, 3, 'mul'), 15)

    def test_div(self):
        self.assertEqual(calc.try_1(10, 3, 'div'), float(10/3))


