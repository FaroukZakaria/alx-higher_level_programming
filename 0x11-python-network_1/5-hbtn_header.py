#!/usr/bin/python3
""" Response variable X-Request-Id """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = requests.get(url)
    print(data.headers['X-Request-Id'])
