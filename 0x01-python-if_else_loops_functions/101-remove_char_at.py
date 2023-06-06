#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    if n < 0:
        return(copy)
    return(copy[:n] + copy[n + 1:])

