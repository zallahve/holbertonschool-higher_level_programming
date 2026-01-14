#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seen = set()
    for n in my_list:
        if n not in seen:
            total += n
            seen.add(n)
    return total
