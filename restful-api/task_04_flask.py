#!/usr/bin/env python3
import http.server
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests for different endpoints."""

        # Root endpoint: /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint
        elif self.path == "/data":
            payload = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            data_json = json.dumps(payload)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(data_json.encode())
            return

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # /info endpoint
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            info_json = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(info_json.encode())
            return

        # Undefined endpoint → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            return


# Start server
def run_server():
    server_address = ("", 8000)  # Port 8000
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000 ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
