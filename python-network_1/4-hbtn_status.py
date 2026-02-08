#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status and display response body details."""
import requests


def main():
    r = requests.get(
        "https://intranet.hbtn.io/status",
        headers={"cfclearance": "true"}
    )
    content = r.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    main()
