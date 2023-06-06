#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    return(copy[:n] + copy[n + 1:])

