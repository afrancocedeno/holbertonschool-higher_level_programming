#!/usr/bin/python3
"""module"""


class Square:
    """class that defines a square with exception handling."""
    def __init__(self, size=0):
        """function
        if statemante variation:
            if (type(size) is not):
            if (not isinstance(size, int)):
            if (isinstance(size, int) != True):
        """
        if (isinstance(size, int) is not True):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
