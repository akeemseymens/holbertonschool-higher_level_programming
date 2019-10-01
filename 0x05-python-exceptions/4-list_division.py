#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    n = 0;

    while n < list_length:

        try:
            result = my_list_1[n] / my_list_2[n]

        except IndexError:
            result = 0
            pass
        except ZeroDivisionError:
            result = 0
            pass
        finally:
            new_list.append(result)
            n += 1

    return new_list
