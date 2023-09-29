#!/usr/bin/python3
""" 10 Commits """
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    ur = f"https://api.github.com/repos/{repo}/{user}/commits?per_page={limit}"
    commits = requests.get(ur).json()
    for comit in commits:
        name = comit.get("commit").get("author").get("name")
        print("{}: {}".format(comit.get("sha"), name))
