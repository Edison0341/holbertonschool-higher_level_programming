#!/usr/bin/python3
"""some txt explaing class"""


class Rectangle:
    """some text for rectangle"""
    

    def __init__(self, width=0, height=0):
        """some other text for rectangle"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """txt"""

        return self.__width

    @width.setter
    def width(self, value):
        """txt"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """txt"""

        return self.__height

    @height.setter
    def height(self, value):
        """txt"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value
