#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

h = open("text.txt","r")
c = h.read()
h.close()


with open("encoded.txt","w") as f:
	for word in c:
		f.write(str(ord(word)))
		f.write(" ")
