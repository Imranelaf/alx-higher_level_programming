#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list[search] = replace
    return new_list
