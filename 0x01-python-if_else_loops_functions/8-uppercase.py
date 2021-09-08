#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            print('{:s}'.format(chr(ord(x) - 32)), end='')
        else:
            print('{:s}'.format(x), end='')
    print(''.format(), end='\n')
