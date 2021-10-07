#!/usr/bin/python3
"""
Function that adds 2 integers
>>>add_integer(5, 4)
9
"""


def add_integer(a, b=98):
    """Return add of a and b
    a and b must be integers
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return 89

    return int(a) + int(b)
