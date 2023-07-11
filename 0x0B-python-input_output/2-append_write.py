#!/usr/bin/python3
"""s"""


def append_write(filename="", text=""):
    """s"""
    with open(filename, 'a', encoding='utf-8') as f:
        fp = f.write(text)
        return (fp)
