#!/usr/bin/python3
"""Class"""


class Square:
    """Define square"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter (actual size)"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter (position)"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a "
                            "tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """get area"""
        return (self.__size ** 2)

    def my_print(self):
        """print #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
    def __str__(self):
        """str representation"""
        lines = []
        if self.size == 0:
            lines.append("")
        else:
            for i in range(self.__position[1]):
                lines.append("")
            for i in range(self.__size):
                lines.append(' ' * self.__position[0] + '#' * self.__size)
            return "\n".join(lines)
