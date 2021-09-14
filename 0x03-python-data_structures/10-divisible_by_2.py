#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        list = []
        for i in range(0, len(my_list) - 1):
            if my_list[i] % 2 == 0:
                list.append(1)
            else:
                list.append(0)
        return list
    else:
        return None
