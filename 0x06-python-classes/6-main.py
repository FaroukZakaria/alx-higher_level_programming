#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

mysquare = Square(3, (1, 1))
print(mysquare.size)
print(mysquare.area())
print(mysquare.position)

print("--lol7")

try:
    my_square = Square(3, "Position")
except Exception as e:
    print(e)

print("--lol8")

try:
    my_square = Square(3, (1, ))
except Exception as e:
    print(e)

print("--lol9")

try:
    my_square = Square(3, (1, -3))
except Exception as e:
    print(e)

print("--lol10")

try:
    my_square = Square(3, (1, "3"))
except Exception as e:
    print(e)
