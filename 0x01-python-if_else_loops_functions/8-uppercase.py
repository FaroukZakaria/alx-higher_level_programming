#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i > 96 and i < 123:
            i -= 32
            print("{}".format(i))
        else:
            print("{}".format(i))
