#!/usr/bin/python3

import os

python_sign = """#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#
"""

bash_sign = """#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#
"""

def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    if lines and lines[0].startswith('#!/'):
        if file_path.endswith('.sh'):
            lines[0] = bash_sign
        else:
            lines[0] = python_sign
    else:
        if file_path.endswith('.sh'):
            lines.insert(0, bash_sign)
        else:
            lines.insert(0, python_sign)

    with open(file_path, 'w') as f:
        f.writelines(lines)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.sh')):
                file_path = os.path.join(root, file)
                process_file(file_path)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    path = "../../SMCC-2023"  # Update this path to the desired directory
    process_directory(path)
