#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    f = open(filename, "r")
    with open(filename) as f:
        content = f.read()
        print(content)
