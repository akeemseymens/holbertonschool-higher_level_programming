#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed = 0
        while printed < x:
            print(my_list[printed], end='')
            printed += 1
        print()
    except:
        print()
    return printed
