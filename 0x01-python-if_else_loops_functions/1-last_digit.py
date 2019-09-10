#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = abs(number) % 10
if number < 0:
    last_num = -last_num
print("Last digit of {} is {} and is".format(number, last_num), end=" ")
if last_num > 5:
    print("greater than 5")
elif last_num == 0:
    print("0")
else:
    print("less than 6 and not 0")
