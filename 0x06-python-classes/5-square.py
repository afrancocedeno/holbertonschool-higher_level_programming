#!/usr/bin/python3
"""class that defines an square and print"""


class Square:
    """Square initialize"""
    def __init__(self, size=0):
        self.size = size
    """getter size"""
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
    """function calculating area of square"""
    def area(self):
        return self.__size ** 2
    """funciton that prints square"""
    def my_print(self):
        for side in range(self.__size):
            print("#" * self.__size)
        if self.__size is 0:
            print()
