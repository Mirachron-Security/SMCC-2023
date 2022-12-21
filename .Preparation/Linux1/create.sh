#!/bin/bash

# accept multiple connections 
/usr/bin/socat tcp-listen:9999,fork exec:'/usr/bin/python3 ./hosting.py'
