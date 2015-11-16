# -*- coding: utf-8 -*-

from decimal import Decimal, InvalidOperation


def main(a):
    params = str(a).split("(")
    args = check_args(params[1].split(","))
    if args == "Value Error":
        return "Value Error"
    if params[0] == "sum":
        return float(args[0] + args[1])
    elif params[0] == "sub":
        return float(args[0] - args[1])
    elif params[0] == "mul":
        return float(args[0] * args[1])
    elif params[0] == "div":
        try:
            return float(args[0] / args[1])
        except ZeroDivisionError:
            return "Zero Division Error"
    elif params[0] == "rev":
        try:
            return float(1 / args[0])
        except ZeroDivisionError:
            return "Zero Division Error"
    else:
        return "Operation error"


def check_args(args):
    i = 0
    for arg in args:
        try:
            args[i] = Decimal(arg.split(")")[0])
            i += 1
        except InvalidOperation:
            return "Value Error"
    return args
