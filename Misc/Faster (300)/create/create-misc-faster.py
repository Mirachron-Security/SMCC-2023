#!/usr/bin/python3

import re
import string
import random
from inputimeout import inputimeout, TimeoutOccurred
import base64

# digits and letters
digits = string.digits
letters = string.ascii_lowercase

# random digits, letters and number of repetitions for each
r_letter = random.choice(letters)
r_num_letters = int(random.randrange(30,100))

# request a random letter typed a random number of times
print("Give me the letter \"%s\" %d times." % (r_letter,r_num_letters))
sol_letter = r_letter * r_num_letters

# read the flag from local machine
f_open = open("flag.txt","r")
f = f_open.read()

# validate input
try:
   # input gets only 3 seconds before timeout
   response= inputimeout(prompt='>> ', timeout=3)

   # compare solution with input
   if (re.match(sol_letter,response)):
      print("Nice work!", f)
   else:
      print("Too bad, try again!")
      exit()

# case if timeout is hit
except TimeoutOccurred:
   print("Too slow!")
   exit()
