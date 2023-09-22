#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

# Colored output
R="\033[0;31m" # Red
G="\033[0;32m" # Green
NO="\033[0m"   # No color

location=~

find "$location" -name docker-compose.yml -type f | while read -r file; do
  dir=$(dirname "$file")

  echo -e "[*] Starting containers in ${G}$dir${NO}\n"

  (cd "$dir" && docker-compose up -d)

  # Check the exit status of the previous command
  if [ $? -eq 0 ]; then
    echo -e "\n[+] Containers in ${G}$dir${NO} started successfully"
  else
    echo -e "\n[-]${R}Error${NO}: Failed to start containers in ${R}$dir${NO}"
  fi
done
