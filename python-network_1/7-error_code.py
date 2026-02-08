#!/usr/bin/python3
"""Fetch a URL and print body; print error code if status >= 400."""
import sys
import requests


def main():
    url = sys.argv[1]
    r = requests.get(url, headers={"cfclearance": "true"})

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    main()
