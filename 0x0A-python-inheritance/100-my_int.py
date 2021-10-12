#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """Have operators inverted"""
    def __eq__(self, other):
        return isinstance(other, MyInt)

    def __ne__(self, other):
        return not isinstance(other, MyInt)
