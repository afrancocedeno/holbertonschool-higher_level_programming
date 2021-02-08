"""This module demostrates and practices documentation in .py files"""


class Square:
    """This class defines a square object"""

    def __init__(self, size="0"):
        """
        __init__ is a special method that initializes everything inside
        it when an object is created with its class.

        print(size) is different from print(self.size)

        Args:
            size (int): Size of the square. (This is the appropiate
                docstring method)

            (self is an arguments itself, so it shouldn´t be included
            in this section but in this function I´m using 2 values:
            self: Is used to send the object itself to the function.
            size: the second parameter with the size of the square.)

        Returns:
            Type: can be a bool, int, string, among others.

            Bool: True if successful, False otherwise.

        """
        self.__size = size
