#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0
    number = 0
    dic = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1}

    for char in reversed(roman_string):
        if dic[char] < number:
            total -= dic[char]
        else:
            total += dic[char]
        number = dic[char]
    return total
