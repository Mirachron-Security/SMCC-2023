#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os

# Files have specific names, so I can check them by name
# file_list = ["discord-creds-bot.py", "verify_srv.py"]

def script_names(file_list):
    path_list = []
    for dirpath, dirnames, filenames in os.walk("../.."):
        for filename in [f for f in filenames if f in file_list]:
            relative_path = os.path.join(dirpath, filename)
            path_list.append(f"{relative_path}")
    return path_list

if __name__ == "__main__":
    print(script_names(file_list))

