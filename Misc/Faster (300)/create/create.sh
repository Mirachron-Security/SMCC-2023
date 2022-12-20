#!/bin/bash

# accept multiple connections 
/usr/bin/socat tcp-listen:31337,fork exec:'/usr/bin/python3 ./faster.py'
