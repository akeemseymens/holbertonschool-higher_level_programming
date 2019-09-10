#!/usr/bin/python3
for num in range(99):
    if num <= 9:
        print(0, end='')
    print("{}".format(num), end=", " if num < 98 else ', {}\n'.format(99))
