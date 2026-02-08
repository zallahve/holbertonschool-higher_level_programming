#!/usr/bin/python3
"""Fetch a URL and print the response body; handle HTTPError codes."""
import sys
import urllib.error
import urllib.request


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={"cfclearance": "true"})

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
