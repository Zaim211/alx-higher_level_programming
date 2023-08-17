#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    list_keys = list(new_dic.keys())

    for x in list_keys:
        new_dic[x] *= 2

    return (new_dic)
