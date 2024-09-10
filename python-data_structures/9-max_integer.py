#!/usr/bin/python3
def max_integer(my_list=[]):
    maximus = my_list[0]

    for item in my_list[1:]:
        if item > maximus:
            maximus = item
    return maximus
