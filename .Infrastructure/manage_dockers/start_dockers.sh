#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

for i in `find /home/chronos -name runme.sh -exec realpath {} \;`; do 
    $i 2>/dev/null;
done

# -_-
docker-compose -f /home/chronos/challenges/web/web-waffle-8004/docker-compose.yaml up -d
