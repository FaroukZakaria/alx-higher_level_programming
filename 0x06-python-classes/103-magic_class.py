#!/usr/bin/python3
"""class"""


import math


class MagicClass:
    """definition"""
    def __init__(self, radius=0):
        """radius"""
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        else:
            self.__radius = radius
            return

    def area(self, radius):
        """area"""
        return (self.__radius ** 2 * math(pi))

    def circumference:
        """circumference"""
        return (2 * math(pi) * self.__radius)
