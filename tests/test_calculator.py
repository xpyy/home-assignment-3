# -*- coding: utf-8 -*-

import unittest
from calculator import main


class CalculatorTestCase(unittest.TestCase):

    def test_bad_op(self):
        self.assertEqual(main("qwr(13, 9)"), "Operation error")

##############################################################

    def test_add_int(self):
        self.assertEqual(main("sum(2, 3)"), 5.0)

    def test_add_float(self):
        self.assertEqual(main("sum(0.1, 0.2)"), 0.3)

    def test_add_negative(self):
        self.assertEqual(main("sum(5, -5)"), 0.0)

    def test_add_str(self):
        self.assertEqual(main("sum(wrsd, -1)"), "Value Error")

    def test_add_both_negative(self):
        self.assertEqual(main("sum(-0.1, -0.1)"), -0.2)

    def test_add_zero(self):
        self.assertEqual(main("sum(0, 123)"), 123)

    def test_add_both_zero(self):
        self.assertEqual(main("sum(0, 0)"), 0.0)

    def test_add_inf(self):
        self.assertEqual(main("sum(0, inf)"), float('inf'))

##############################################################

    def test_sub_int(self):
        self.assertEqual(main("sub(13, 9)"), 4)

    def test_sub_float(self):
        self.assertEqual(main("sub(0.3, 0.1)"), 0.2)

    def test_sub_negative(self):
        self.assertEqual(main("sub(5, -5)"), 10)

    def test_sub_str(self):
        self.assertEqual(main("sub(qwewq, 9)"), "Value Error")

    def test_sub_both_negative(self):
        self.assertEqual(main("sub(-0.1, -0.1)"), 0.0)

    def test_sub_zero(self):
        self.assertEqual(main("sub(0, 123)"), -123.0)

    def test_sub_both_zero(self):
        self.assertEqual(main("sub(0, 0)"), 0.0)

    def test_sub_inf(self):
        self.assertEqual(main("sub(532, inf)"), float('-inf'))

    def test_sub_same_value(self):
        self.assertEqual(main("sub(34, 34)"), 0.0)

# ##############################################################

    def test_mul_int(self):
        self.assertEqual(main("mul(2, 3)"), 6.0)

    def test_mul_float(self):
        self.assertEqual(main("mul(0.2, 0.1)"), 0.02)

    def test_mul_float_int(self):
        self.assertEqual(main("mul(120, 0.1)"), 12.0)

    def test_mul_negative(self):
        self.assertEqual(main("mul(5, -5)"), -25.0)

    def test_mul_str(self):
        self.assertEqual(main("mul(wqewqe, 3)"), "Value Error")

    def test_mul_both_negative(self):
        self.assertEqual(main("mul(-1, -13)"), 13.0)

    def test_mul_unit(self):
        self.assertEqual(main("mul(42, 1)"), 42.0)

    def test_mul_zero(self):
        self.assertEqual(main("mul(0, 3)"), 0.0)

    def test_mul_both_zero(self):
        self.assertEqual(main("mul(0, 0)"), 0.0)

    def test_mul_inf(self):
        self.assertEqual(main("mul(2, inf)"), float('inf'))

##############################################################

    def test_div_int(self):
        self.assertEqual(main("div(3, 2)"), 1.5)

    def test_div_float(self):
        self.assertEqual(main("div(0.3, 0.1)"), 3.0)

    def test_div_float_int(self):
        self.assertEqual(main("div(0.1, 10)"), 0.01)

    def test_div_int_float(self):
        self.assertEqual(main("div(10, 0.1)"), 100.0)

    def test_div_unit(self):
        self.assertEqual(main("div(7, 1)"), 7.0)

    def test_div_same_value(self):
        self.assertEqual(main("div(5, 5)"), 1.0)

    def test_div_negative(self):
        self.assertEqual(main("div(10, -5)"), -2.0)

    def test_div_str(self):
        self.assertEqual(main("div(saesad, 2)"), "Value Error")

    def test_div_both_negative(self):
        self.assertEqual(main("div(-6, -2)"), 3.0)

    def test_div_zero_numerator(self):
        self.assertEqual(main("div(0, 2)"), 0.0)

    def test_div_zero_denominator(self):
        self.assertEqual(main("div(3, 0)"), "Zero Division Error")

##############################################################

    def test_rev_int(self):
        self.assertEqual(main("rev(5)"), 0.2)

    def test_rev_float(self):
        self.assertEqual(main("rev(0.5)"), 2.0)

    def test_rev_str(self):
        self.assertEqual(main("rev(waras)"), "Value Error")

    def test_rev_negative(self):
        self.assertEqual(main("rev(-2)"), -0.5)

    def test_rev_unit(self):
        self.assertEqual(main("rev(1)"), 1)

    def test_rev_zero(self):
        self.assertEqual(main("rev(0)"), "Zero Division Error")

