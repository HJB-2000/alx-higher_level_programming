#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_n = []
    r = 0
    for i in range(0, list_length):
        try:
            r = (my_list_1[i] / my_list_2[i])
        except TypeError:
            r = 0
            print("wrong type")
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        except IndexError:
            r = 0
            print("out of range")
        finally:
            list_n.append(r)
    return list_n
