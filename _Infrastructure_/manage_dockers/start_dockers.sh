#!/usr/bin/bash

for i in $(find /home/chronos -name runme.sh -exec realpath {} \;); do 
    $i 2>/dev/null;
done

# -_-
docker-compose -f /home/chronos/challenges/web/web-waffle-8004/docker-compose.yaml up -d
