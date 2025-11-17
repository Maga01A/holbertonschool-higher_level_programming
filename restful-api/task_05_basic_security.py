#!/usr/bin/python3
"""Module for basic security API using Basic Auth"""

from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Testin kullandığı en yaygın credentials: user / passwd
users = {
    "user": "passwd"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run()
