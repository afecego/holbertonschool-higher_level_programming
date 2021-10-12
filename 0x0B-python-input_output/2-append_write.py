#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
