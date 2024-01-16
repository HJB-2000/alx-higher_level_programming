#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if char_code not in (ord('e'), ord('q')):
        print("{:c}".format(char_code), end="")
