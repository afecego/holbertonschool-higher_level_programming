#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
>>>text_indentation("Hello. world")
Hello
world"""


def text_indentation(text):
    """
    Return the indentation for ".", "?" and ":"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    status = 1
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(text[i])
            print()
            status = 1

        else:
            if status == 1:
                if text[i] == " ":
                    while (text[i] == " "):
                        i += 1
                print(text[i], end="")
                status = 0
            else:
                print(text[i], end="")
        i += 1
