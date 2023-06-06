#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        # If n is negative, return the original string unchanged
        return str
    # Concatenate the parts of the string before and after the character at index n
    return str[:n] + str[n+1:] 
