#!/bin/bash

# To buid
# docker build -t web-collide-8006 .

docker run -d -p 8006:80 -e AUTHOR="Radu" --name "web-collide-8006" -it web-collide-8006
  
