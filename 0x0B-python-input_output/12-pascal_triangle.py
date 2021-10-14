#!/usr/bin/python3
"""function that returns a list of lists of integers
representing the Pascal’s triangle"""


def pascal_triangle(n):
    """representing the Pascal’s triangle"""
    end = n - 1
    pascal = [[1]]

    if n < 0:
        return []

    for i in range(end):
        fila = [1]

        if len(pascal[i]) > 1:
            fila_prev = len(pascal[i]) - 1

            for j in range(fila_prev):
                suma = pascal[i][j] + pascal[i][j + 1]
                fila.append(suma)

        fila.append(1)
        pascal.append(fila)
    return pascal
