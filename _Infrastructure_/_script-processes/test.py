#!/usr/bin/python3

import os
import os.path

files = ["discord-creds-bot.py", "verify_srv.py"]

def script_names():
    for dirpath, dirnames, filenames in os.walk("../.."):
        for filename in [f for f in filenames if f in files]:
            full_path = os.path.join(dirpath, filename)
            print(full_path)

if __name__ == "__main__":
    script_names()
