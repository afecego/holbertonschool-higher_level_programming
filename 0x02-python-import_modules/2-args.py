#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    n = len(argv) - 1
    print('{:d} argument{}{}'.format(n, 's' if n == 0 or
                                     n > 1 else '', '.' if n < 1 else ':'))
    t = 0
    for i in argv:
        if t > 0:
            print('{:d}: {:s}'.format(t, i))
        t += 1
