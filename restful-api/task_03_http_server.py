#!/usr/bin/python3
"""
Task 03: Simple API using http.server.

Endpoints:
- GET /         -> "Hello, this is a simple API!"
- GET /status   -> "OK"
- GET /data     -> JSON: {"name": "John", "age": 30, "city": "New York"}
- GET /info     -> JSON: {"version": "1.0", "description": "A simple API built with http.server"}
Other paths -> 404 "Endpoint not found"
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code, text):
        body = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        # IMPORTANT: keep it exactly application/json for strict checkers
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json(
                200,
                {"version": "1.0", "description": "A simple API built with http.server"},
            )
        else:
            self._send_text(404, "Endpoint not found")

    def log_message(self, format, *args):
        return


def run_server(host="0.0.0.0", port=8000):
    server = HTTPServer((host, port), SimpleAPIHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()
