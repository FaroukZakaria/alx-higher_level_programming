#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return(0)
    string = []
    for i in roman_string:
        if i == 'I':
            string.append(1)
        elif i == 'V':
            string.append(5)
        elif i == 'X':
            string.append(10)
        elif i == 'L':
            string.append(50)
        elif i == 'C':
            string.append(100)
        elif i == 'D':
            string.append(500)
        elif i == 'M':
            string.append(1000)
    res = 0
    just_I = True
    for i in roman_string:
        if i != 'I':
            just_I = False
            break
    if just_I is True:
        for i in string:
            res += i
        return(res)
    for i in string:
        if i == 1 and string[-1] != 1:
            res -= 1
            continue
        else:
            res += i
    if res > 3999:
        return(0)
    return(res)
