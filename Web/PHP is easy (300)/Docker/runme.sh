#!/bin/bash

# To buid
# docker build -t web-php-8003 .

docker run -d -p 8003:80 -e AUTHOR="Radu" --name "web-php-8003" -it web-php-8003
