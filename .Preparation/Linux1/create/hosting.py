#!/usr/bin/python3

from pwn import *
import re
from inputimeout import inputimeout, TimeoutOccurred

# user interation
print("Salut! Concursul se apropie!")
print("Veti mai primi cateva exercitii pentru acomodare, sper sa va placa.")
print("""Pentru inceput, raspunde la aceasta intrebare (ai doar 3 secunde): 

In luna va avea loc concursul?
""")

# correct response
correct = "martie"

# read the flag from local machine
f_open = open("flag.txt","r")
f = f_open.read()

try:
   # input gets only 3 seconds before timeout
   response= inputimeout(prompt='>> ', timeout=5)

   # compare solution with input
   if (re.match(correct,response.lower())):
      print("Super! Uite un flag: ", f)
   else:
      print("Nu chiar, mai incearca.")
      exit()

# case if timeout is hit
except TimeoutOccurred:
   print("Prea lent!")
   exit()
