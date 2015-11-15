# -*- coding: utf-8 -*-

from decimal import Decimal, InvalidOperation


def add(a, b):
    return float(a + b)


def sub(a, b):
    return float(a - b)


def mul(a, b):
    return float(a * b)


def div(a, b):
    try:
        return float(a / b)
    except ZeroDivisionError:
        return "Zero Division Error"


def rev(a):
    return div(1, a)


def calc(a, op, b=0):
    try:
        a = Decimal(str(a))
        b = Decimal(str(b))
    except InvalidOperation:
        return "Value Error"
    if(op == "add"):
        return add(a, b)
    elif(op == "sub"):
        return sub(a, b)
    elif(op == "mul"):
        return mul(a, b)
    elif(op == "div"):
        return div(a, b)
    elif(op == "rev"):
        return rev(a)
    else:
        return "Operation error"
