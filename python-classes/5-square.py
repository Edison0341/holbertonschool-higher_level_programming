#!/usr/bin/python3
"""This is a square class"""


class Square:
    """Square class with a private size attribute"""

    def __init__(self, size=0):
        """Initialize a square with size validation"""

        self.size = size

    def area(self):
        """Calculate and return the area of the square"""

        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the character #"""

        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
