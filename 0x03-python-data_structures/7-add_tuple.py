#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a = 0
    else:
        a = tuple_a[0]
    if len(tuple_a) < 2:
        aa = 0
    else:
        aa = tuple_a[1]
    if len(tuple_b) == 0:
        b = 0
    else:
        b = tuple_b[0]
    if len(tuple_b) < 2:
        bb = 0
    else:
        bb = tuple_b[1]
    new_tuple = ((a + b), (aa + bb))
    return(new_tuple)
