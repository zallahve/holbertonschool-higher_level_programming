#!/usr/bin/python3
"""List 10 most recent commits: <sha>: <author name>."""
import sys
import requests


def main():
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url, params={"per_page": 10})

    try:
        commits = r.json()
    except ValueError:
        commits = []

    for c in commits[:10]:
        sha = c.get("sha")
        author = (
            c.get("commit", {})
            .get("author", {})
            .get("name")
        )
        print("{}: {}".format(sha, author))


if __name__ == "__main__":
    main()
