#!/usr/bin/python3
def no_c(my_string):
    new_chars = []
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_chars.append(ch)
    return ''.join(new_chars)
