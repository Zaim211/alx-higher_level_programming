#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    n = int(length / 2)
    l = list_of_integers

    if n - 1 < 0 and n + 1 >= length:
        return l[n]
    elif n - 1 < 0:
        return l[n] if l[n] > l[n + 1] else l[n + 1]
    elif n + 1 >= length:
        return l[n] if l[n] > l[n - 1] else l[n - 1]

    if l[n - 1] < l[n] > l[n + 1]:
        return l[n]

    if l[n + 1] > l[n - 1]:
        return find_peak(l[n:])
    return find_peak(l[:n])
