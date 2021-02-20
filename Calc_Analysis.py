from math import *
import BasicMath
import sys


class FuncX:  # ax^(b) + c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a == 0 and self.c == 0:
            is_zero = True
        else:
            is_zero = False
        self.is_zero = is_zero
