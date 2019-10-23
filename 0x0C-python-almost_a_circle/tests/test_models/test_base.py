#!/usr/bin/python3
"""Test for Base class"""
import unittest
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import contextlib
import os
import unittest
import sys
from io import StringIO


class TestBase(unittest.TestCase):
    """Test Base class"""
    def setUp(self):
        """Set up Base class tests."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tidy up after test methods."""
        pass

    def test_type(self):
        """Test type."""
        b1 = Base()
        self.assertTrue(type(b1) == Base)

    def test_id(self):
        """Prints id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_init_type(self):
        """Test the __init__ method"""
        types = (int, float, str, tuple, list, dict, set, bool)
        self.assertIsInstance(Base(), Base)
        self.assertIsInstance(Base(0), Base)
        for value in [t() for t in types] + [None, type]:
            self.assertIsInstance(Base(id=value), Base)

    def test_save_to_file_null(self):
        """Check if the file exists"""
        lo = None
        Base.save_to_file(lo)
        self.assertEqual(os.path.exists('Base.json'), True)

    def test_save_to_file_data_type(self):
        """test save to file is a string"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(type(data), str)

    def test_save_to_file_empty_contents(self):
        """test to read function for base.json"""
        op = None
        Base.save_to_file(op)
        with open("Base.json", mode='r') as f:
            data = f.read()
        self.assertEqual(data, '[]')

    def test_to_json_string(self):
        """test converstion of python object to a json string"""
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'a': 1}]), '[{"a": 1}]')

    def test_from_json_string(self):
        """test conversion of json string to python object"""
        obj = [{'a': 1}]
        json_string = Base.to_json_string(obj)
        self.assertEqual(Base.from_json_string(json_string), obj)

    def test_create(self):
        """instance with set attributes"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 3/5\n")
        self.assertTrue(type(r1) == Rectangle)

        output = StringIO()
        sys.stdout = output
        r1 = Square(3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (3) 0/0 - 3\n")
        self.assertTrue(type(r1) == Square)

    def test_create2(self):
        """instance with set attributes"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/0 - 3/5\n")

    def test_create3(self):
        """instance with set attributes"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_TypeError(self):
        """instance with TypeError"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)

    def test_create_TypeError_int(self):
        """instance with TypeError int"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(1, 2, 3)

    def test_create_TypeError_string(self):
        """instance with TypeError string"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r2 = Rectangle.create("string")

    def test_create_TypeError_string(self):
        """instance with TypeError string"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(NameError):
            r2 = Rectangle.create(**betty)

    def test_load_from_file(self):
        """list of instances"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        print(list_rectangles_output[0])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 2/8 - 10/7\n")

        output = StringIO()
        sys.stdout = output
        print(list_rectangles_output[1])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (2) 0/0 - 2/4\n")
        self.assertTrue(type(list_rectangles_output), list)

        output = StringIO()
        sys.stdout = output
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        print(list_squares_output[0])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (5) 0/0 - 5\n")

        output = StringIO()
        sys.stdout = output
        print(list_squares_output[1])
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Square] (6) 9/1 - 7\n")
        self.assertTrue(type(list_squares_output), list)


if __name__ == '__main__':
    unittest.main()
