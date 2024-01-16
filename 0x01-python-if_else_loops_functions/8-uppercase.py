def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
             
            print("{}".format(char), end="")
    
    print()  
