#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os

# Update this path to the desired directory
path = "." 
banner = """

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

"""
python_sign = "#!/usr/bin/python3" + banner
bash_sign = "#!/bin/bash" + banner

# Colored output
R = "\033[0;31m"  # Red
G = "\033[0;32m"  # Green
B = "\033[0;34m"  # Blue
NO = "\033[0m"    # No color

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    is_modified = False

    if python_sign not in content and bash_sign not in content:
        if file_path.endswith('.sh'):
            content = bash_sign + content
        else:
            content = python_sign + content
        is_modified = True

        with open(file_path, 'w') as f:
            f.write(content)

    return is_modified

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.sh')):
                file_path = os.path.join(root, file)
                is_modified = process_file(file_path)
                if is_modified:
                    print(f"{B}Modified:{NO} {file_path}")
                else:
                    print(f"{G}Unchanged:{NO} {file_path}")

if __name__ == "__main__":
    process_directory(path)
