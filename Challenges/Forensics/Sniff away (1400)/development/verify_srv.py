#!/usr/bin/env python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os
from flask import Flask, request
import sys
import logging
from logging.handlers import RotatingFileHandler
import time

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

# Configure a file handler for the Flask logger
script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_directory, 'requests.log')

file_handler = RotatingFileHandler(log_file_path, maxBytes=1024*1024, backupCount=10)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

# Load answers from file
answers_path = os.path.join(script_directory, 'answers.txt')

with open(answers_path, 'r') as f:
    answers = [line.strip().replace('\n', '') for line in f.readlines()]

# Load flag from file
flag_path = os.path.join(script_directory, 'flag.txt')
with open(flag_path, 'r') as f:
    flag = f.read().strip()

# Redirect stdout and stderr to /dev/null
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

@app.route('/sniff_away/<int:question>', methods=['POST'])
def verify(question):
    answer = request.get_data().decode('utf-8')

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info('[%s] %s %s %s', timestamp, request.method, request.url, answer)

    if answer == answers[question - 1]:
        return f"Character {question} of the flag is {flag[question - 1]}"
    else:
        return "Wrong answer! try again."


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port='31337')
    except OSError:
        print("Error: Port already in use")
        sys.exit(1)
