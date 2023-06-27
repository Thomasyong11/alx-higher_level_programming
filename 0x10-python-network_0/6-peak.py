#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    length = len(list_of_integers)
    
    if length == 0:
        return None

    mid = length // 2

    if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (
        mid == length - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]
    ):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])


# Test cases
print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
