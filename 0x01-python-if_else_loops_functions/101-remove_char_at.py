#!/usr/bin/python3
def remove_char_at(str, n):
    iter = 0
    rem = ""
    for i in str:
        if iter != n:
            rem += i
        iter += 1
    return rem
