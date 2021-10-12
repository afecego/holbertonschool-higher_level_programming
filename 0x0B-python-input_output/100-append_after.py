#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string"""
    acumul = ""
    with open(filename, "r") as f:
        for line in f:
            acumul += line
            if search_string in line:
                acumul += new_string
    with open(filename, "w") as f:
        f.write(acumul)
