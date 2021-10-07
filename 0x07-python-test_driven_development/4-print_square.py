#!/usr/bin/python3
"""Write a function that prints a square with the character #
>>>print_square(2)
##
##
"""


def print_square(size):
    """
    Return a square whit a size "size"
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
