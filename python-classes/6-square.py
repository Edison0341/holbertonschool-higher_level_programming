#!/usr/bin/python3
"""This is a square class"""


class Square:
    """Square class with a private size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size validation"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the character #,
            taking position into account"""

        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
