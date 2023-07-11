#!/usr/bin/python3
""" function that writes a string to a text file UTF8"""


def number_of_lines(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
