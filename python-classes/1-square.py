#!/usr/bin/python3
""" Square class to represent a sqaure"""


class Square:
    """ Define a square and its basic properties
    >>> sqaure_1 = Square()
    >>> sqaure_2 = Sqaure(87)
    """

    def _init_(self, size: int) -> None:
        """ _init_ the size with a params of int """
        self.__size = size
