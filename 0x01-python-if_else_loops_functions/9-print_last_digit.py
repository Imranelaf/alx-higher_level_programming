#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints and returns the last digit of the absolute value of a given number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end=" ")
    return last_digit
