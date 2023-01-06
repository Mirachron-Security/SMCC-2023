#!/bin/bash

# To buid
# docker build -t web-request-8007 .

docker run -d -p 8007:8007 -e AUTHOR="Radu" --name "web-request-8007" -it web-request-8007
