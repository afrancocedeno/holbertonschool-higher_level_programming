#!/usr/bin/python3
"""List of available attributes and methods of an object

"""

attr_list = []


def lookup(obj):
    """function that get into objet attributes.

        This function use dir to extract all attributes
        if an object.

        dir() funciton is a builtin that returns a list of
        the attributes and methods of any object ( say funcitons,
        modules, strings, lists, dictionaries, etc.)

        Args:
            obj: input object to be extracted

        Returns:
            Returns a list of attrbutes

    """
    attr_list = dir(obj)
    return (attr_list)
