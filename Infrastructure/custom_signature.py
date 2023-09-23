#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os
import fnmatch

# Colored output
R = "\033[0;31m"  # Red
G = "\033[0;32m"  # Green
B = "\033[0;34m"  # Blue
NO = "\033[0m"    # No color

# Define the shebangs and banner message
python_shebang = "#!/usr/bin/python3"
bash_shebang = "#!/bin/bash"

# Define the new banner without color
banner = """
#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

"""

# Check if the banner is present
def has_banner(file_content):
    return banner.strip() in file_content.strip()

# Add the banner to file
def add_banner_to_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    if has_banner(content):
        return False

    with open(file_path, 'w') as f:
        if content.startswith(python_shebang) or content.startswith(bash_shebang):
            shebang, rest = content.split('\n', 1)
            f.write(shebang + '\n' + banner + rest)
        else:
            f.write(f"{python_shebang}\n" if file_path.endswith('.py') else f"{bash_shebang}\n")
            f.write(banner)
            f.write(content)

    return True

# Process files recursively
def process_files(directory):
    modified_count = 0
    unmodified_count = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, '*.sh') or fnmatch.fnmatch(file, '*.py'):
                file_path = os.path.join(root, file)
                if add_banner_to_file(file_path):
                    print(f"{B}Modified:{NO} {file_path}")
                    modified_count += 1
                else:
                    print(f"{G}Unmodified:{NO} {file_path}")
                    unmodified_count += 1

    print(f"\n{B}Modified files: {modified_count}{NO}")
    print(f"{G}Unmodified files: {unmodified_count}{NO}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    process_files(directory)
