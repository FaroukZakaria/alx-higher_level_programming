#!/usr/bin/python3
"""sss"""


def write_file(filename="", text=""):
    """sss"""
    with open(filename, 'w') as f:
        fp = f.write(text)
        return (fp)
