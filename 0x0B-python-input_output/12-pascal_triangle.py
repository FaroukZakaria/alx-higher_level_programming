#!/usr/bin/python3
"""S"""


def pascal_triangle(n):
    start = 1
    if n <= 0:
        return []
    for i in range(2, n):
        a = []
        for j in range(1, i):
            a.append(1)
        print("--")
        print(len(a))
        print("--")
        if start >= 3:
            for k in range(1, len(a)):
                a[k] = b[k - 1] + b[k]
        b = a[:]
        start += 1
        print(a)
