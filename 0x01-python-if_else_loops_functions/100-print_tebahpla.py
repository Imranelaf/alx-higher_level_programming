#!/usr/bin/python3
case = 0
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(letter - case)), end="")
    if case == 0:
        case = 32
    else:
        case=0
