#!/usr/bin/python3
def roman_to_int(roman_string):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reset = 0
    point = 0

    if type(roman_string) is str and roman_string:
        for i in range(len(roman_string) - 1, -1, -1):
            if value[roman_string[i]] >= point:
                reset += value[roman_string[i]]
            else:
                reset -= value[roman_string[i]]
            point = value[roman_string[i]]
    return reset
