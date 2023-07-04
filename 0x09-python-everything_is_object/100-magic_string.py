#!/usr/bin/python3
iteration = 0
def magic_string():
    global iteration; iteration += 1; return (", ".join(["BestSchool"] * (iteration)))
