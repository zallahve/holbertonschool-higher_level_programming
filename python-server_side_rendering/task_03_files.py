#!/usr/bin/python3
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(path="products.json"):
    """Read products from JSON file. Return list of dicts, or [] on error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (OSError, json.JSONDecodeError):
        return []


def read_products_csv(path="products.csv"):
    """Read products from CSV file. Return list of dicts, or [] on error."""
    products = []
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except OSError:
        return []
    return products


def normalize_products(products):
    """
    Ensure each product has fields: id, name, category, price.
    Return list of dicts with consistent types (id int if possible).
    """
    normalized = []
    for p in products:
        pid = p.get("id")
        try:
            pid = int(pid)
        except (TypeError, ValueError):
            pid = pid

        normalized.append(
            {
                "id": pid,
                "name": p.get("name"),
                "category": p.get("category"),
                "price": p.get("price"),
            }
        )
    return normalized


@app.route("/products")
def products_page():
    source = request.args.get("source", "")
    pid = request.args.get("id", default=None)

    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source", products=[])

    if source == "json":
        products = read_products_json()
    else:
        products = read_products_csv()

    products = normalize_products(products)

    if pid is not None:
        try:
            pid_int = int(pid)
        except (TypeError, ValueError):
            pid_int = None

        filtered = []
        for p in products:
            if pid_int is not None and p.get("id") == pid_int:
                filtered.append(p)

        if not filtered:
            return render_template(
                "product_display.html",
                error="Product not found",
                products=[],
            )
        products = filtered

    return render_template("product_display.html", products=products, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
