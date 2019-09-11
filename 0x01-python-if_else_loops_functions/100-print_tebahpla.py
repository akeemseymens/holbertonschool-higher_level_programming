#!/usr/bin/python3
for ltr in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(ltr - 32) if ltr % 2 != 0 else chr(ltr)), end="")
