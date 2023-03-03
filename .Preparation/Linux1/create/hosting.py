#!/usr/bin/python3

import re
from inputimeout import inputimeout, TimeoutOccurred
import sys
from time import sleep


# user interation
print("Salut! Concursul se apropie!")
#sleep(0.5)
print("Veti mai primi cateva exercitii pentru acomodare, sper sa va placa.")
#sleep(0.5)
print("""Pentru inceput, raspunde la aceasta intrebare (ai doar 3 secunde): 

In ce luna va avea loc concursul?
""")

# correct response
correct = "martie"

# read the flag from local machine
f_open = open("/home/chronos/challenges/pre-ctf/give-me-the-date/flag.txt","r")
f = f_open.read()

try:
   # input gets only 3 seconds before timeout
   response= inputimeout(prompt='>> ', timeout=3)

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
# in case the user exists unexpectedly
except OSError:
    print('Input/output error occurred. Exiting.')
    sys.exit(1)
