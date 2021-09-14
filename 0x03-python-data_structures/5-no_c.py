#!/usr/bin/python
def no_c(my_string):
    new = my_string.translate({ord("c"): None})
    new = new.translate({ord("C"): None})
    return new
