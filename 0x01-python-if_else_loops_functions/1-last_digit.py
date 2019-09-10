#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
str0 = "Last digit of"
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
str3 = "and is 0"
if last_num > 5:
    print('{0} {1:d} is {2:d} {3}'.format(str0, number, last_num, str1))
elif last_num < 6 and last_num > 0:
    print('{0} {1:d} is {2:d} {3}'.format(str0, number, last_num, str2))
else:
    print('{0} {1:d} is {2:d} {3}'.format(str0, number, last_num, str3))
