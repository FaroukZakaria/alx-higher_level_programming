#!/usr/bin/python3
""" API JSON TEST """
import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) <= 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = requests.post(url, data={'q': q})
    try:
        joined = data.json()
        if joined:
            print("[{}] {}".format(joined['id'], joined['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
