#!/usr/bin/python3
""" 10 Commits """
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    commits = requests.get(url).json()
    for commit in commits:
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(commit.get("sha"), name)
