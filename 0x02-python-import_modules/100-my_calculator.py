#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    if args[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif args[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == '__main__':
    main()
