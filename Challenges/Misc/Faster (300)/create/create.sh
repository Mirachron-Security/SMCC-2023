#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

# Get the directory of the current script
script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Construct the full path to host.py script
hosting_path="$script_directory/host.py"

# simultaneous connections from multiple users
# create a pty because the python script accepts input from a terminal
# redirect errors to /dev/null !!
/usr/bin/socat tcp-listen:1337,fork system:"exec /usr/bin/python3 $hosting_path 2>/dev/null",pty,raw,echo=0
