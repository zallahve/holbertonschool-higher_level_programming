#!/usr/bin/python3
"""Send a POST request with an email parameter and print the response body."""
import sys
import requests


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(
        url,
        data={"email": email},
        headers={"cfclearance": "true"}
    )
    print(r.text)


if __name__ == "__main__":
    main()
