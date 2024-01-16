#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""

    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result_str += "{}".format(uppercase_char)
        else:
            result_str += "{}".format(char)

    print("{}".format(result_str))
