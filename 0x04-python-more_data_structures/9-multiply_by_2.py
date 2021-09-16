#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_2 = a_dictionary.copy()
    for i, j in dictionary_2.item():
        dictionary_2[i] = j * 2
    return dictionary_2
