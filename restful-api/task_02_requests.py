#!/usr/bin/python3
"""
Task 02: Consuming and processing data from an API using Python (requests).

Functions:
- fetch_and_print_posts(): Fetch posts and print response status code + all titles.
- fetch_and_save_posts(): Fetch posts and save id/title/body to posts.csv.
"""

import csv
import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print:
    - Status Code: <code>
    - title of each post (one per line) if successful
    """
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.RequestException:
        # If the request fails (DNS, timeout, etc.), we can't get a status code.
        # Keep behavior simple and consistent with the exercise expectations.
        print("Status Code: None")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save to posts.csv
    with columns: id, title, body
    """
    try:
        response = requests.get(API_URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    try:
        posts = response.json()
    except ValueError:
        return

    rows = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(rows)
