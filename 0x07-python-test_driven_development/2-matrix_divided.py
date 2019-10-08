#!/usr/bin/python3
"""
This is  "matrix_divided" module

The matrix_divided module divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns the division of list elements in a matrix

    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
    of integers/floats")
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
    of integers/floats")
    if not all(isinstance(x, int) or isinstance(x, float):
               for y in matrix for x in y):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if matrix:
        size = len(matrix[0])
        if not all(len(x) == size for x in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in y] for y in matrix]
