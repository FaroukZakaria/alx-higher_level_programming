#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 1
    for i in my_list:
        if a < x and i != my_list[-1]:
            try:
                print(int(i))
                a += 1
            except:
                a += 1
        else:
            print()
