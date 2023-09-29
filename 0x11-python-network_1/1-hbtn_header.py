#!/usr/bin/python3
""" Response ID """
import urllib
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        xrq = headers['X-Request-Id']
        print(xrq)
