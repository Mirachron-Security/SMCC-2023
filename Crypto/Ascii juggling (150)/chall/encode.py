#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os

file_in_name = "text.txt"
file_out_name = "encoded.txt"
current_dir = os.path.dirname(__file__)
file_in_path = os.path.join(current_dir,file_in_name)
file_out_path = os.path.join(current_dir,file_out_name)

h = open(file_in_path,"r")
c = h.read()
h.close()


with open(file_out_path,"w") as f:
	for word in c:
		f.write(str(ord(word)))
		f.write(" ")
		print(str(ord(word)),end=" ")
