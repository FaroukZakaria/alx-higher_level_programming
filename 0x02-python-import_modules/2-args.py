#!/usr/bin/python3
import argparse


def main():
    par = argparse.ArgumentParser()
    par.add_argument('text', nargs='*', help='Text to print')
    argv = par.parse_args()
    args = len(argv.text)
    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
        print("1: {}".format(argv.text[0]))
    else:
        print("{} arguments:".format(args))
        i = 1
        for arg in argv.text:
            print("{}: {}".format(i, arg))
            i += 1


if __name__ == '__main__':
    main()
