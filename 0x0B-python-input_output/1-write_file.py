#!/usr/bin/python3
"""Write a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
