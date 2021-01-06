#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """square initialize"""
    def __init__(self, size=0):
        self.size = size
    """property instance"""
    @property
    def size(self):
        return self.__size
    """setter size"""
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """function calculating area"""
    def area(self):
        return self.__size ** 2
