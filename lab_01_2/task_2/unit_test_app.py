"""
This program will test the changer module

    Method              Assertion
assertEqual(a, b):	    [a] == [b]
assertNotEqual(a, b):	[a] != [b]
assertTrue(a):	        bool(a) is True
assertFalse(a):	        bool(a) is False
assertIsNone(a):        [a] is None
assertIsNotNone(a):	    [a] is not None
assertIn(a, b):	        [a] in [b]
assertNotIn(a, b):	    [a] not in [b]
"""
import unittest
from lab_02.task_2 import task2


class TestSentences(unittest.TestCase):
    def test_01(self):
        test_01 = task2.Rational(2, 4)
        self.assertEqual(test_01.fractionalForm(), "2/4")
        self.assertEqual(test_01.floatingPointForm(), "0.5")

    def test_02(self):
        test_02 = task2.Rational(2, 2)
        self.assertEqual(test_02.fractionalForm(), "2/2")
        self.assertEqual(test_02.floatingPointForm(), "1.0")

    def test_03(self):
        test_03 = task2.Rational(3, 9)
        self.assertEqual(test_03.fractionalForm(), "3/9")
        self.assertEqual(test_03.floatingPointForm(), "0.333")

    def test_04(self):
        test_04 = task2.Rational(1, 1)
        self.assertEqual(test_04.fractionalForm(), "1/1")
        self.assertEqual(test_04.floatingPointForm(), "1.0")

    def test_05(self):
        test_05 = task2.Rational(10, 1)
        self.assertEqual(test_05.fractionalForm(), "10/1")
        self.assertEqual(test_05.floatingPointForm(), "10.0")

    def test_06(self):
        test_06 = task2.Rational(2.5, 2)
        self.assertEqual(test_06.fractionalForm(), "2.5/2")
        self.assertEqual(test_06.floatingPointForm(), "1.25")

    def test_07(self):
        test_07 = task2.Rational(2, 2.5)
        self.assertEqual(test_07.fractionalForm(), "2/2.5")
        self.assertEqual(test_07.floatingPointForm(), "0.8")

    def test_08(self):
        test_08 = task2.Rational(2.5, 3)
        self.assertEqual(test_08.fractionalForm(), "2.5/3")
        self.assertEqual(test_08.floatingPointForm(), "0.833")

    def test_09(self):
        test_09 = task2.Rational(21, 3)
        self.assertEqual(test_09.fractionalForm(), "21/3")
        self.assertEqual(test_09.floatingPointForm(), "7.0")

    def test_10(self):
        test_10 = task2.Rational(10, 1000)
        self.assertEqual(test_10.fractionalForm(), "10/1000")
        self.assertEqual(test_10.floatingPointForm(), "0.01")


if __name__ == "__main__":
    unittest.main()
