#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TextMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertIs(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([0]), 0)

    def test_increasing_list(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_decreasing_list(self):
        self.assertEqual(max_integer([2, 1]), 2)

    def test_list_with_negatives(self):
        self.assertEqual(max_integer([2, -1, 1]), 2)

    def test_list_only_negatives(self):
        self.assertEqual(max_integer([-2, -1, -3]), -1)

    def test_bad_parameter_type(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([], [])

    def test_no_parameters(self):
        self.assertIs(max_integer(), None)

    def test_list_with_floats(self):
        self.assertEqual(max_integer([1, 1.5]), 1.5)
