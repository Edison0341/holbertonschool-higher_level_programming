#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (0, None)
    maximus = my_list[0]
    for item in my_list[1:]:
        if item > maximus:
            maximus = item
    return maximus
