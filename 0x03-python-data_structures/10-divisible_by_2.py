#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            x[count] = True
        else:
            x[count] = False
    return(x)
