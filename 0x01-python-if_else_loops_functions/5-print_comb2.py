#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print("0{}".format(n), end=", ")
    else:
        print("{}".format(n), end=", ")
