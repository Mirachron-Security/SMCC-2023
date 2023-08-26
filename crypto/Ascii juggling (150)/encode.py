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
h = open("text.txt","r")
c = h.read()
h.close()


with open("encoded.txt","w") as f:
	for word in c:
		f.write(str(ord(word)))
		f.write(" ")
