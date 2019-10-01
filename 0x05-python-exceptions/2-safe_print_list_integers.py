#!usr/bin/python3
def safe_print_list_integer(my_list=[], x = 0):
    printed = 0
    num = 0

    while n < x:
        try:
            print("{:d}".format(my_list[num]), end='')
        except (TypeError, ValueError):
            printed -= 1
        finally:
            printed += 1
            n += 1
    print('')

    return printed
