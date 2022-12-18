#!/bin/bash

# To build
# docker build -t web-lucky-6666 .

docker run -d -p 6666:80 --rm -e AUTHOR="Radu" --name "web-lucky-6666" -it "web-lucky-6666"
