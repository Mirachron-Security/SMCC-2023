#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

# Colored output
R="\033[0;31m"
G="\033[0;32m"
NO="\033[0m"

echo -e "$G[*] Stopping all docker containers...$NO"

if [ "$(docker ps -q)" ]; then
  docker stop $(docker ps -q)
else
  echo "[+] No running containers found."
fi

echo

echo -e "$G[*] Removing all docker containers ...$NO"

if [ "$(docker ps -aq)" ]; then
  docker rm $(docker ps -aq)
else
  echo "[+] No containers found."
fi

echo -e "$G\nDone!$NO"
