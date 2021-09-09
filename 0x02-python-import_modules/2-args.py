#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    l = len(sys.argv)

    print('{:d} argument{:}'.format(l - 1, '.' if l == 1 else
          (':' if l == 2 else 's:')))
    i = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1
