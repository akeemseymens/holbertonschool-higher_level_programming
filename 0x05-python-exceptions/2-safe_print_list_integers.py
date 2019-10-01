#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    num = 0

    while num < x:
        try:
            print("{:d}".format(my_list[num]), end='')
        except (TypeError, ValueError):
            printed -= 1
        finally:
            printed += 1
            num += 1
    print('')

    return printed
