#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Rectangle class test"""

    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove temporary files and directories"""
        rmtree(getcwd(), ignore_errors=True)

    def test_init(self):
        """Test the `init` method"""
        r = Rectangle(1, 1)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 1, 0, 0))
        self.assertIsInstance(r.id, int)

    def test_id(self):
        """Prints id"""
        r1 = Rectangle(4, 9)
        r2 = Rectangle(9, 4)
        r3 = Rectangle(3, 4, 9, 0, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 5)
        self.assertTrue(type(r3), Rectangle)

    def test_one_param(self):
        """Passing one parameter"""
        with self.assertRaises(TypeError):
            r = Rectangle(4)

    def test_all_param(self):
        """Passing all parameters"""
        r = Rectangle(1, 2, 3, 4, 5)

    def test_string(self):
        """Passing string"""
        s = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(str(self.r), s)
        r = Rectangle(1, 1, id=1)
        self.assertEqual(str(r), '[Rectangle] (1) 0/0 - 1/1')
        with self.assertRaises(TypeError):
            r = Rectangle(4, "string")
        with self.assertRaises(TypeError):
            r = Rectangle("string", 4)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_width_type(self):
        """Test for setting width attr"""
        with self.assertRaises(TypeError):
            Rectangle(1.0, 1)

    def test_no_param(self):
        """Passing nothing"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_extra_param(self):
        """Excess parameters"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 1)

    def test_float(self):
        """Float parameter"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1.2, 3, 4, 5)

    def test_NaN(self):
        """NaN parameter"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, float("nan"), 3, 4)

    def test_inf(self):
        """inf parameter"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, float("inf"), 3, 4)

    def test_unknown(self):
        """unknown parameter"""
        with self.assertRaises(NameError):
            r = Rectangle(a)

    def test_None(self):
        """None parameter"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, None, 3, 4)

    def test_negative(self):
        """Negative parameter"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_zero(self):
        """zero as a parameter"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_area(self):
        """Prints the area"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)


    def test_display(self):
        """Tests rectangle output"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(3, 3)
        r.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "###\n###\n###\n"

    def test_str(self):
        """Tests __str__"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(4, 9, 2, 1, 13)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (13) 2/1 - 4/9\n"
    def test_height_type(self):
        """Test for setting height attr"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1.0)

    def test_x_type(self):
        """Test for x attr"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, x=1.0)

    def test_display_x_y(self):
        """Tests rectangle with x and y"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(3, 2, 1, 0)
        r.display()
        r = Rectangle(1, 1)
        self.out = StringIO()
        sys.stdout = self.out
        r.display()
        self.assertEqual(self.out.getvalue(), '#\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Rectangle(2, 2)
        r.display()
        self.assertEqual(self.out.getvalue(), '##\n##\n')
        self.out = StringIO()
        sys.stdout = self.out
        r = Rectangle(1, 1, 1, 1)
        r.display()
        self.assertEqual(self.out.getvalue(), '\n #\n')
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ###\n ###\n"

    def test_update(self):
        """Test update"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        r.update(89, 2)
        r.update(89, 2, 3)
        r.update(89, 2, 3, 4)
        r.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5, 6, 7)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"

    def test_update_no_param(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r = Rectangle(10, 10, 10, 10)
        r.update()
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 10/10 - 10/10\n"

    def test_kwargs(self):
        """Test kwargs"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual((r.id, r.x, r.y, r.width, r.height), (2, 3, 4, 5, 6))
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_kwargs_extra_keys(self):
        """Test kwargs with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, banu=89)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_to_dict_rep(self):
        """Test dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {
            'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

    def test_to_dict_rep_update(self):
        """Testing dictionary update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/9 - 10/2\n")


if __name__ == '__main__':
    unittest.main()
