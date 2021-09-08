#!/usr/bin/python3
def uppercase(str):
    for x in str:
        print('{:s}'.format(chr(ord(x) - 32) if ord(x) >= ord('a') and
                            ord(x) <= ord('z') else x), end="")
    print(''.format(), end='\n')
