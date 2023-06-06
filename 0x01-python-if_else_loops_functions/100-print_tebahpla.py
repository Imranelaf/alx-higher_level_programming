#!/usr/bin/python3
n = 0
for letter in range(ord('z'), ord('a') - 1, -1):
    if n == 0:
        print(chr(letter).lower(), end="")
        n = 1
    else:
        print(chr(letter).upper(), end="")
        n = 0
