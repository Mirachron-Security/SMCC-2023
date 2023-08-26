#!/usr/bin/python3

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

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

=======
>>>>>>> parent of db8b9fe (Added signature)
import re

h = open("encoded.txt")
c = h.read()
h.close()

decoded = ''.join([chr(int(dec)) for dec in c.split()])

print(''.join(re.findall('flag{.*}',decoded)))
