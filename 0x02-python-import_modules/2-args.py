#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # subtract 1 to exclude the script name itself

    if num_args == 0:
        print("0 arguments.")
    else:
        plural_suffix = "s" if num_args > 1 else ""
        print("{} argument{}:".format(num_args, plural_suffix))

        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
