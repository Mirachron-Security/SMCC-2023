#!/bin/bash

# accept multiple connections 
/usr/bin/socat tcp-listen:5003,fork exec:'/usr/bin/python3 ./faster.py'
