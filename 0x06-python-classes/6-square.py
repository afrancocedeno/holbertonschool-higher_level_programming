#!/usr/bin/python3
"""class that define an square"""


class Square:
    """square Initialize"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((isinstance(value, tuple)) and len(value) == 2 and
                (value[0] >= 0 and value[1] >= 0) and
                (isinstance(value[0], int)) and (isinstance(value[1], int))):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """funciton that calculates the area of an square"""
    def area(self):
        return self.__size ** 2

    """function that prints square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for index_0 in range(self.__position[1]):
                print()
            for index_1 in range(self.__size):
                for index_2 in range(self.__position[0]):
                    print(" ", end="")
                for index_3 in range(self.__size):
                    print("#", end="")
                print()
