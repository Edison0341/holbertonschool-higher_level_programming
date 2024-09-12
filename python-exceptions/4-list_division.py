#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for number in range(list_length):
        try:
            if number >= len(my_list_1) or number >= len(my_list_2):
                raise IndexError
            if not isinstance(my_list_1[number], (int, float)) or not isinstance(my_list_2[number], (int, float)):
                raise TypeError
            division = my_list_1[number] / my_list_2[number]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
