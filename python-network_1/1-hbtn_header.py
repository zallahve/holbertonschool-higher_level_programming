#!/usr/bin/python3
"""Fetch a URL and print the X-Request-Id response header value."""
import sys
import urllib.request


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={"cfclearance": "true"})

    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
