#!/bin/bash

# To build
# docker build -t web6-login-8002 .

docker run -d -p 8002:80 -e AUTHOR="Radu" --name "web-login-8002" -it "web6-login-8002"
