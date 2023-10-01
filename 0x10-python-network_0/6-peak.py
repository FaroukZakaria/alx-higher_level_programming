#!/usr/bin/python3
""" Finds peak in a list """


def find_peak(list_of_integers):
    """ finds peak """
    lst = None
    for i in range(len(list_of_integers)):
        if i == 0:
            lst = list_of_integers[i]
            i += 1
        if list_of_integers[i] >= list_of_integers[i - 1]:
            lst = list_of_integers[i]
        else:
            continue
    return (lst)
