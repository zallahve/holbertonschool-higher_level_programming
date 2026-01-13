#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        o = ord(ch)
        if ord('a') <= o <= ord('z'):
            o -= 32
        print("{}".format(chr(o)), end="")
    print("")
