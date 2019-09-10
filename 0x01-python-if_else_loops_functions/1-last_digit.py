#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
str0 = "Last digit of"
str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"

if last_num > 5:
    print('{} {:d} is {:d} {}'.format(str0, number, last_num, str1))
elif last_num == 0:
    print('{} {:d} is {:d} {}'.format(str0, number, last_num, str2))
elif number < 0:
    print('{} {:d} is {:d} {}'.format(str0, number, (last_num * -1), str3))
else:
    print('{} {:d} is {:d} {}'.format(str0, number, last_num, str3))
