#!/bin/bash

# To build
# docker build -t web-template-8005 .

docker run -d -p 8005:8005 --rm -e AUTHOR="Radu" --hostname="web-template-8005" --name "web-template-8005" -it "web-template-8005"
