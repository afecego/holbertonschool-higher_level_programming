#!/usr/bin/python3
"""Funtion that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """must be an list of lists of integers or floats"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for j in row:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_c = []
    for x in range(len(m_a)):
        m_c.append([])
        for y in range(len(m_b[0])):
            m_c[x].append(0)

    for x in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                m_c[x][j] += m_a[x][k] * m_b[k][j]
    return m_c
