# -*- coding: utf-8 -*-

import unittest
from calculator import calc


class CalculatorTestCase(unittest.TestCase):

    def test_bad_op(self):
        self.assertEqual(calc(1, "qwe", 1), "Operation error")

##############################################################

    def test_add_int(self):
        self.assertEqual(calc(2, "add", 3), 5.0)

    def test_add_float(self):
        self.assertEqual(calc(0.1, "add", 0.2), 0.3)

    def test_add_negative(self):
        self.assertEqual(calc(5, "add", -5), 0.0)

    def test_add_str(self):
        self.assertEqual(calc("bad arg", "add", 3), "Value Error")

    def test_add_both_negative(self):
        self.assertEqual(calc(-0.1, "add", -0.1), -0.2)

    def test_add_zero(self):
        self.assertEqual(calc(0, "add", 123), 123)

    def test_add_both_zero(self):
        self.assertEqual(calc(0, "add", 0), 0.0)

    def test_add_inf(self):
        self.assertEqual(calc(54, "add", 'inf'), float('inf'))

##############################################################

    def test_sub_int(self):
        self.assertEqual(calc(13, "sub", 9), 4)

    def test_sub_float(self):
        self.assertEqual(calc(0.3, "sub", 0.1), 0.2)

    def test_sub_negative(self):
        self.assertEqual(calc(5, "sub", -5), 10)

    def test_sub_str(self):
        self.assertEqual(calc("bad arg", "sub", 3), "Value Error")

    def test_sub_both_negative(self):
        self.assertEqual(calc(-0.1, "sub", -0.1), 0.0)

    def test_sub_zero(self):
        self.assertEqual(calc(0, "sub", 123), -123.0)

    def test_sub_both_zero(self):
        self.assertEqual(calc(0, "sub", 0), 0.0)

    def test_sub_inf(self):
        self.assertEqual(calc(54, "sub", 'inf'), float('-inf'))

##############################################################

    def test_mul_int(self):
        self.assertEqual(calc(2, "mul", 3), 6.0)

    def test_mul_float(self):
        self.assertEqual(calc(0.1, "mul", 0.2), 0.02)

    def test_mul_float_int(self):
        self.assertEqual(calc(0.1, "mul", 120), 12.0)

    def test_mul_negative(self):
        self.assertEqual(calc(5, "mul", -5), -25.0)

    def test_mul_str(self):
        self.assertEqual(calc("bad arg", "mul", 3), "Value Error")

    def test_mul_both_negative(self):
        self.assertEqual(calc(-1, "mul", -13), 13.0)

    def test_mul_unit(self):
        self.assertEqual(calc(1, "mul", 42), 42.0)

    def test_mul_zero(self):
        self.assertEqual(calc(0, "mul", 123), 0.0)

    def test_mul_both_zero(self):
        self.assertEqual(calc(0, "mul", 0), 0.0)

    def test_mul_inf(self):
        self.assertEqual(calc(54, "mul", 'inf'), float('inf'))

##############################################################

    def test_div_int(self):
        self.assertEqual(calc(3, "div", 2), 1.5)

    def test_div_float(self):
        self.assertEqual(calc(0.3, "div", 0.1), 3.0)

    def test_div_float_int(self):
        self.assertEqual(calc(0.1, "div", 10), 0.01)

    def test_div_int_float(self):
        self.assertEqual(calc(10, "div", 0.1), 100.0)

    def test_div_unit(self):
        self.assertEqual(calc(7, "div", 1), 7.0)

    def test_div_same_value(self):
        self.assertEqual(calc(5, "div", 5), 1.0)

    def test_div_negative(self):
        self.assertEqual(calc(10, "div", -5), -2.0)

    def test_div_str(self):
        self.assertEqual(calc("bad arg", "div", 3), "Value Error")

    def test_div_both_negative(self):
        self.assertEqual(calc(-6, "div", -2), 3.0)

    def test_div_zero_numerator(self):
        self.assertEqual(calc(0, "div", 123), 0.0)

    def test_div_zero_denominator(self):
        self.assertEqual(calc(49, "div", 0), "Zero Division Error")

##############################################################

    def test_rev_int(self):
        self.assertEqual(calc(5, "rev"), 0.2)

    def test_rev_float(self):
        self.assertEqual(calc(0.5, "rev"), 2.0)

    def test_rev_str(self):
        self.assertEqual(calc("bad arg", "rev"), "Value Error")

    def test_rev_negative(self):
        self.assertEqual(calc(-2, "rev"), -0.5)

    def test_rev_unit(self):
        self.assertEqual(calc(1, "rev"), 1)

    def test_rev_zero(self):
        self.assertEqual(calc(0, "rev"), "Zero Division Error")
