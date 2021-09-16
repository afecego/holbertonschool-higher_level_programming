#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for iter in sorted(a_dictionary.keys()):
        print("{:}: {:}".format(iter, a_dictionary[iter]))
