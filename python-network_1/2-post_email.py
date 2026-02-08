#!/usr/bin/python3
"""Send a POST request with an email parameter and print the response body."""
import sys
import urllib.parse
import urllib.request


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"cfclearance": "true"}
    )

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
