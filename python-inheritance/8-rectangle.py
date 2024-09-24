#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """Represents the base class for geometry-related operations"""

    def area(self):
        """Error indicatin that the area method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
