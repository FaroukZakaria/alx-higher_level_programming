#!/usr/bin/python3
"""Class"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter (actual size)"""
        return (self.__size)
    """setter"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """get area"""
    def area(self):
        return (self.__size ** 2)
    """print square #"""
    def my_print(self):
        for i in range(self.__size + 1):
            print('#' * self.__size)
