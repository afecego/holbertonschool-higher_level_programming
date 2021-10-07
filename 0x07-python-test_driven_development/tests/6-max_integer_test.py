#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test for max_integer values are correctly
    """
    def test_function(self):
        """
        Test lista when is using numbers
        """
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([-3, -5, -8]), -3)
        self.assertAlmostEqual(max_integer([-1, -2, 0]), 0)
        self.assertAlmostEqual(max_integer("ok"), "o")
        self.assertAlmostEqual(max_integer([1.3, 2.4, 2.5]), 2.5)

    def test_type_values(self):
        """
        Test errors in funtion
        """
        self.assertRaises(TypeError, max_integer, ["Hello", 2, 4])
        self.assertRaises(TypeError, max_integer, None)
