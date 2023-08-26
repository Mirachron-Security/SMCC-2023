#!/bin/bash

<<<<<<< HEAD
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

=======
>>>>>>> parent of db8b9fe (Added signature)
# simultaneous connections from multiple users 
# create a pty because the python script accepts input from a terminal
# redirect errors to /dev/null !!
/usr/bin/socat tcp-listen:9999,fork system:'exec /usr/bin/python3 /home/chronos/challenges/pre-ctf/give-me-the-date/hosting.py 2>/dev/null',pty,raw,echo=0
