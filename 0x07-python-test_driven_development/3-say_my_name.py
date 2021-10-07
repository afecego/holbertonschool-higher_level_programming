#!/usr/bin/python3
"""
Write a function that prints: My name is <first name> <last name>
>>>say_my_name(Adrian, Ceron)
Adrian Ceron
"""


def say_my_name(first_name, last_name=""):
    """
    Return the first name and last name, and must be type string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
