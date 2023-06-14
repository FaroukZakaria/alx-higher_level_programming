#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    y = 0
    return(lambda x: x + y for x in unique)
