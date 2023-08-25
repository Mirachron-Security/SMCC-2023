#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

# simultaneous connections from multiple users 
# create a pty because the python script accepts input from a terminal
# redirect errors to /dev/null !!
/usr/bin/socat tcp-listen:1337,fork system:'exec /usr/bin/python3 /home/chronos/challenges/misc/faster/hosting.py 2>/dev/null',pty,raw,echo=0
