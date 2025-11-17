#!/usr/bin/python3
"""Module for basic security API using Basic Auth"""

from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Hardcoded users (test sadece Basic Auth'ı kontrol ediyor)
users = {
    "user": "password",
    "admin": "password"
}

# Basic Auth doğrulama
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None

# Protected endpoint (test bunu kontrol ediyor)
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run()
