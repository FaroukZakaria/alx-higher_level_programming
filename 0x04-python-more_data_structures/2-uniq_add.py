#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = list(set(my_list))
    i = 0
    return(lambda x: i + x for x in unique)
