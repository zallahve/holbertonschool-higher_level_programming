#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Load items list from items.json. Return [] on any error."""
    try:
        with open("items.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("items", [])
        if isinstance(items, list):
            return items
        return []
    except (OSError, json.JSONDecodeError, AttributeError):
        return []


@app.route("/items")
def items_page():
    items = load_items()
    return render_template("items.html", items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
