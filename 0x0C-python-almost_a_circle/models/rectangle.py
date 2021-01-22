#!/usr/bin/python3

"""Class Rectangle inherits from Base
    getter setter attributes manipulation
"""


class Rectangle(Base):

    # Class constructor

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # using getter
    @property
    # create a method for first variable to acces (get) the width value inside the class
    def width(self):
        return (self.__width)
    # change (set) the value of the variable 
    @width.setter
