#!/usr/bin/python3
"""Module"""


class Square:
    """Square class with its area"""
    def __init__(self, size=0):
        """init function"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if (isinstance(new_size, int) is not True):
            raise TypeError("size must be an integer")
        elif (new_size < 0):
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """"""
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.size):
                print('#', end="")
            print()
