#!/bin/bash

# accept multiple connections 
/usr/bin/socat tcp-listen:1337,fork system:' exec /usr/bin/python3 ./faster.py',pty,raw,echo=0
