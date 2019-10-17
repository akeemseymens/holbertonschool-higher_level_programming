#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    """function of pascal"""
    arr = []
    if n <= 0:
        return arr
    for line in range(1, n + 1):
        C = 1
        pas = []
        for i in range(1, line + 1):
            pas.append(str(C))
            C = C * (line - i) // i
        arr.append(pas)
    return arr
