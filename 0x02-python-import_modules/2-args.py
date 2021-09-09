#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    l = len(argv)

    print('{:d} argument{:}'.format(l - 1, '.' if l == 1 else
          (':' if l == 2 else 's:')))
    i = 1
    for arg in argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1
