#!/usr/bin/python3
"""
Funtion that divide all elements of a matrix with
>>>matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Matrix must be a list of lists of integers or floats
    Each row of the matrix must be of the same size"""

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mess = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if type(row) is not list:
            raise TypeError(mess)

        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mess)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    result = [[round((i / div), 2) for i in row] for row in matrix]
    return result
