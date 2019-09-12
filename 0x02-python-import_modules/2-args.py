#!/usr/bin/python3

import sys
if __name__ == "__main__":
    args = len(sys.argv)
    if args == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(args - 1, "" if args == 2 else "s"))
        for i, j in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, j))
