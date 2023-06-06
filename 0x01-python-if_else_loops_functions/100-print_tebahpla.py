#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    l = chr(letter).lower() if (letter - ord('z')) % 2 == 0 else chr(letter).upper()
    print(l, end="")
