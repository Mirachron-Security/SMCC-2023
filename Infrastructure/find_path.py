#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os

def find_path(start_directory, script_name):

    for root, _, files in os.walk(start_directory):
        for file in files:
            if script_name in file:
                found_script = os.path.abspath(os.path.join(root, file))
    return found_script

if __name__ == "__main__":
    # Specify the directory you want to start searching from
    start_directory = '../../'
    script_name = 'crontabs.py'

    script_path = find_path(start_directory, script_name)
    print(script_path)

