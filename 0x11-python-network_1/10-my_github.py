#!/usr/bin/python3
""" Github API """
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    data = requests.get(url, headers={'Authorization': f'Bearer {password}'})
    if data.status_code >= 400):
        print("None")
        exit()
    print(data.json()['id'])
