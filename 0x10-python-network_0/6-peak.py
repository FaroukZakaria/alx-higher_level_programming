#!/usr/bin/python3
""" Finds peak in a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return (None)
    else:
        return (sorted(list_of_integers)[-1])
