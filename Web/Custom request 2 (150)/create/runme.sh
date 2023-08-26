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

# To buid
# docker build -t web-request-8008 .

docker run -d -p 8008:8008 -e AUTHOR="Radu" --name "web-request-8008" -it web-request-8008
