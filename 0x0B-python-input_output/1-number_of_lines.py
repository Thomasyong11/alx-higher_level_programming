#!/usr/bin/python3
def number_of_lines(filename=""):
    """function that reads a text and return number of lines"""

   number_of_lines = 0
    with open(filename) as f:
        for line in f:
            number_of_lines += 1
        return (number_of_lines)

