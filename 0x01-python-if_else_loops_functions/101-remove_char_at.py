#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str # If n is negative, return the original string unchanged
    return str[:n] + str[n+1:]  # Concatenate the parts of the string before and after the character at index n
