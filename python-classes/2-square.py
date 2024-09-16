#!/usr/bin/python3
"""This is a square class"""


class Square:
    """Square class with a private size attribute"""

    def __init__(self, size=0):
        """Initialize a square with size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
