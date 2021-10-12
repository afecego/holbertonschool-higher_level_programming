#!/usr/bin/python3
"""function that returns True if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """True if the object is an instance of, or if the object
    is an instance of a class """
    if isinstance(obj, a_class):
        return True
    return False
