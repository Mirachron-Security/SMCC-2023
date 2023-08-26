#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import random
import string

nr_pairs = 10
length = 20

def generate_creds(length):
    chars_user = string.ascii_lowercase + string.digits
    chars_pass = string.ascii_letters + string.digits #+ string.punctuation
    
    user = 'user_' + ''.join(random.choice(chars_user) for i in range(round(length/2-1)))
    password = ''.join(random.choice(chars_pass) for i in range(length))
    line = user + ' : ' + password
    return line

# Generate x pairs of creds
for i in range(nr_pairs):
    print(generate_creds(length))
