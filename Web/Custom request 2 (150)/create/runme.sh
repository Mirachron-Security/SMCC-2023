#!/bin/bash

# To buid
# docker build -t web-request-8008 .

docker run -d -p 8008:8008 -e AUTHOR="Radu" --name "web-request-8008" -it web-request-8008
