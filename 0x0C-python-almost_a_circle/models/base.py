#!/usr/bin/python3
"""class module documentation example"""


class Base:
    """create an attribute for the class Base

    try as print(dir(Base))

    make the attribute private
    a = 0 -> is public
    _a = 0 -> is protected
    __a = 0 -> is private
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """id is an attribute of an instance not the class: self.id"""
        if id is not None:
            """ assign the public attribute id with this argument value """
            self.id = id
        else:
            """The __nb_objects is an attribute for the class

            __nb_objects +=1 --> is not correct

            """

            Base.__nb_objects += 1
            self.id = Base.__nb_objects
