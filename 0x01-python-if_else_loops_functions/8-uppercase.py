#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            ord(i) -= 32
            print("{}".format(i))
        else:
            print("{}".format(i))
