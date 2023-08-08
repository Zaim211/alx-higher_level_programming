#!/usr/bin/python3
def uppercase(str):
    ascii_num = ord(str)
    if ascii_num <= 65 and ascii_num >= 90:
        return True
    return False
