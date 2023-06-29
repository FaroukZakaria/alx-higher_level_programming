#!/usr/bin/python3
"""Class"""


class Square:
    """Define square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter (actual size)"""
        return (self.__size)

    def position(self):
        """getter (position)"""
        return (self.__size)
    """setter"""
    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        if isinstance(value, tuple) and all(isinstance(i, int) for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    """get area"""
    def area(self):
        return (self.__size ** 2)
    """print square #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print(' ' * self.__position[1])
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
