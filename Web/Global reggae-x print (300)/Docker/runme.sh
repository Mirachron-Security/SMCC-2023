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

# To build
# docker build -t web-grep-8001 .

docker run -d -p 8001:80 -e AUTHOR="Radu" --name "web-grep-8001" --hostname "web-grep-8001" -it "web-grep-8001"
