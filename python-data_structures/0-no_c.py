#!/usr/bin/python3
def  no_c(my_string):

    new_string = list(my_string)
    i = 0
    while i < (len(new_string)):
        if (new_string[i] == 'c' or new_string[i] == 'C'):
            new_string.pop(i)
        else:
            i += 1
            
    string_modify = ''.join(new_string)
    return string_modify