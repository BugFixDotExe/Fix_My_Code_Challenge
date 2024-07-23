#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This script stirves to become a perfect Square calulator """


class Square():
    """The Square class"""
    def __init__(self, *args, **kwargs):
        """The constructor of the Square class
        Args:
            *args (a list of values)
            **kwargs (a keyworded dict)
        """
        self.width = 0
        self.height = 0

        if 'width' in kwargs and kwargs['width'] is not None:
            self.width = kwargs['width']
        if 'height' in kwargs and kwargs['height'] is not None:
            self.height = kwargs['height']

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimiter of the square """
        return 4 * (self.width)

    def __str__(self):
        """ A string representation of the square """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """ A runner for the script as long as it's not improted"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
