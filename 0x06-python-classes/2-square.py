#!/usr/bin/python3
"""Class"""
class Square:
    """Define square"""
    def __init__(self, size=0):
        """initialize size"""

        if isinstance(size, int) != True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
