#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = list(a_dictionary.keys())
    sort.sort()
    for i in sort:
        print("{}: {}".format(i, a_dictionary[i]))
