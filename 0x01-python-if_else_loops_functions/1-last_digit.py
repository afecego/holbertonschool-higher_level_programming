#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    end = -1 * (abs(number) % 10)
else:
    end = number % 10

grather_five = 'Last digit of {:d} is {:d} and is greater than 5'
is_zero = 'Last digit of {:d} is {:d} and is 0'
less_six = 'Last digit of {:d} is {:d} and is less than 6 and not 0'

if end > 5:
    print(grather_five.format(number, end))
elif end == 0:
    print(is_zero.format(number, end))
else:
    print(less_six.format(number, end))
