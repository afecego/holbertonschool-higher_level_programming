#!/usr/bin/python3
"""function that returns True if the object is exactly an
instance of the specified class"""


def is_same_class(obj, a_class):
    """return true if the object is the same"""
    result = isinstance(type(obj), a_class)
    if result is True:
        return True
    return False
