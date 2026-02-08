#!/usr/bin/python3
"""Send a request and print the X-Request-Id header value."""
import sys
import requests


def main():
    url = sys.argv[1]
    r = requests.get(url, headers={"cfclearance": "true"})
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
