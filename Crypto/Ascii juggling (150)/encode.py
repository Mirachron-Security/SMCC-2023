#!/usr/bin/python3

h = open("text.txt","r")
c = h.read()
h.close()


with open("encoded.txt","w") as f:
	for word in c:
		f.write(str(ord(word)))
		f.write(" ")
