#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

mysquare = Square(3)
mysquare.my_print()

print("--")

mysquare = Square(10)
mysquare.my_print()

print("--")
