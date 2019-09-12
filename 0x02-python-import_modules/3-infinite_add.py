#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = len(sys.argv)
    num = 0

    for i in range(1, args):
        num += int(sys.argv[i])
print(num)
