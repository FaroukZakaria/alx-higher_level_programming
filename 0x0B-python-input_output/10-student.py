#!/usr/bin/python3
"""S"""


class Student:
    """S"""
    def __init__(self, first_name, last_name, age):
        """S"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """S"""
        if (isinstance(attrs, list) is True and
                all(isinstance(i, str) is True for i in attrs)):
            for j in attrs:
                if hasattr(self, j) is True:
                    getattr(self, j)
                return (j)
        return (self.__dict__)
