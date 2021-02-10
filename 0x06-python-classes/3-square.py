#!/usr/bin/python3
"""Module"""


class Square:
    """Square class with its area"""
    def __init__(self, size=0):
        """init function"""
        if (isinstance(size, int) is not True):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """private attribute __size to prevent error:
        > output errot without protection attribute
            Square' object has no attribute 'size'
        Further solution:
            return (self.__size * self.__size)
            return (self.__size ** 2)

        """

        return self.__size * self.__size
