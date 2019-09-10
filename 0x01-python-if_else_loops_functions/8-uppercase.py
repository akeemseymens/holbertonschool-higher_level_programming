#!/usr/bin/python3
def uppercase(str):
    case = 0
    for ltr in str:
        if ord(ltr) >= ord('a') and ord(ltr) <= ord('z'):
            case = 32
        else:
            case = 0
        print('{:c}'.format(ord(ltr) - case), end="")
    print()
