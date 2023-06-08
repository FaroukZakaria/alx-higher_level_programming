#!/usr/bin/python3
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('argv', nargs='*', type=int)
    args = parser.parse_args()
    sum = 0
    i = 1
    if len(args.argv) == 0:
        print(0)
    else:
        for arg in args.argv:
            sum += arg
        print(int(sum))


if __name__ == '__main__':
    main()
