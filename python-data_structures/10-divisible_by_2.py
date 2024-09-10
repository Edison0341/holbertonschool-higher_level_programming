#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cutin2 = [num % 2 == 0 for num in my_list]
    return cutin2
