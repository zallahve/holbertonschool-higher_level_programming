#!/usr/bin/python3
"""Send a POST request and parse JSON response."""
import sys
import requests


def main():
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if not data:
        print("No result")
        return

    print("[{}] {}".format(data.get("id"), data.get("name")))


if __name__ == "__main__":
    main()
