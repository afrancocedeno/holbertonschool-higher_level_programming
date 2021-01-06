#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """exceptions handling"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
    """function calculating area"""
    def area(self):
        return self.__size ** 2
