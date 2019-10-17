#!/usr/bin/python3
"""pascal triangle function"""


def printPascal(n):
    arr = []
    if n<= 0:
        return arr
    for line in range(1, n + 1):
        C = 1;
        pas = []
        for i in range(1, line + 1):
            arr.append(str(C))
            C = int(C * (line - i) / i)
       return pas
