#!/usr/bin/env python3

import os
from flask import Flask, request
import sys

app = Flask(__name__)

# Load answers from file
with open('answers.txt', 'r') as f:
    answers = [line.strip().replace('\n', '') for line in f.readlines()]

# Load flag from file
with open('flag.txt', 'r') as f:
    flag = f.read().strip()

@app.route('/sniff_away/<int:question>', methods=['POST'])
def verify(question):
    answer = request.get_data().decode('utf-8')
    if answer == answers[question - 1]:
        return f"Character {question} of the flag is {flag[question - 1]}"
    else:
        return "Wrong answer! try again."


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 verify_srv.py <port>")
        sys.exit(1)
    
    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid port number")
        sys.exit(1)

    try:
        app.run(port=port)
    except OSError:
        print("Error: Port already in use")
        sys.exit(1)
