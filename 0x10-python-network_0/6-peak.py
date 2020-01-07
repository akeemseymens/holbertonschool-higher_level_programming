#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]

    i = 0
    j = len(list_of_integers) - 1

    while i < j:
        mid = (i + j) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            i = mid + 1
        elif list_of_integers[mid] <= list_of_integers[mid - 1]:
            j = mid - 1
        elif (list_of_integers[mid] >= list_of_integers[mid + 1] and
              list_of_integers[mid] >= list_of_integers[mid - 1]):
            return list_of_integers[mid]

    return list_of_integers[i]
