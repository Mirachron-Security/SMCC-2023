#!/bin/bash

# simultaneous connections from multiple users 
# create a pty because the python script accepts input from a terminal
/usr/bin/socat tcp-listen:9999,fork system:'exec /usr/bin/python3 /home/chronos/challenges/pre-ctf/give-me-the-date/hosting.py',pty,raw,echo=0
