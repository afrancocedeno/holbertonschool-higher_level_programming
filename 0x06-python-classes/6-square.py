"""Module"""


class Square:
    """Square class with its area"""
    def __init__(self, size=0, position=(0, 0)):
        """init function"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    def position(self):
        return self.__position

    @size.setter
    def size(self, new_size):
        if (isinstance(new_size, int) is not True):
            raise TypeError("size must be an integer")
        elif (new_size < 0):
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def position(self, new_position):
        for i in new_position:
            if (isinstance(new_position[i], int is not True)):
                raise TypeError('position must\
be a tuple of 2 positive integers')

    def area(self):
        """"""
        return (self.__size ** 2)

    def my_print(self):
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}{}".format(
                " " * self.__position[0],
                '#' * self.__size))
