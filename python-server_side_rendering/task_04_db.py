#!/usr/bin/python3
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DB_FILE = "products.db"


def create_database():
    """Create products.db and seed initial data (id 1 and 2)."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    # Insert required rows (ignore if already there)
    cursor.execute(
        """
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        """
    )
    conn.commit()
    conn.close()


def read_products_json(path="products.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (OSError, json.JSONDecodeError):
        return []


def read_products_csv(path="products.csv"):
    products = []
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except OSError:
        return []
    return products


def read_products_sql():
    """Read products from SQLite DB. Return list of dicts."""
    try:
        create_database()  # ensure DB/table/data exist
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
            for r in rows
        ]
    except sqlite3.Error as exc:
        # Caller will show DB error in template
        raise exc


def normalize_products(products):
    """Normalize to dicts with id/name/category/price; id int when possible."""
    normalized = []
    for p in products:
        pid = p.get("id")
        try:
            pid = int(pid)
        except (TypeError, ValueError):
            pass

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

    if source not in ("json", "csv", "sql"):
        return render_template("product_display.html", error="Wrong source", products=[])

    try:
        if source == "json":
            products = read_products_json()
        elif source == "csv":
            products = read_products_csv()
        else:
            products = read_products_sql()
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error",
            products=[],
        )

    products = normalize_products(products)

    if pid is not None:
        try:
            pid_int = int(pid)
        except (TypeError, ValueError):
            pid_int = None

        filtered = []
        if pid_int is not None:
            for p in products:
                if p.get("id") == pid_int:
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
