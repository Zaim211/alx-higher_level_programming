#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    max_value = my_list[0]

    for n in range(1, length):
        if my_list[n] > max_value:
            max_value = my_list[n]

    return (max_value)
