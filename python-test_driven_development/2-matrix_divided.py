#!/usr/bin/python3
"""Divide all elements of a matrix by a given number and round to 2 decimal
    places."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given number and round to 2 decimal
    places."""
    e = "matrix must be a matrix (array of arrays of integers/floats)"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row,list)
    for row in matrix):
        raise TypeError(e)
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(e)
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
