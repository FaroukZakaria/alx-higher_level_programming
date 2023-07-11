#!/usr/bin/python3
""" s """


def read_file(filename=""):
    """function"""
    with open(filename, 'r', encoding='utf-8') as f:
        fp = f.read()
        print(fp, end="")
