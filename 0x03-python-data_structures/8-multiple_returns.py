#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    tupla = (len(sentence), sentence[0])
    return tupla
