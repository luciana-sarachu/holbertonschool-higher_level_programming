#!/usr/bin/python3


""" this class defines a square that has a Private instance attribute size"""


class Square:

    """ class Instantiation """
    def __init__(self, size):

        """size is private attribute"""

        self.__size = size
