#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import re
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
enc_flag_path = os.path.join(script_directory, 'encoded.txt')

with open(enc_flag_path, "r") as f:
    contents = f.read()

decoded = ''.join([chr(int(dec)) for dec in contents.split()])

flag_match = re.search(r'flag{(.*?)}', decoded)
if flag_match:
    flag_text = flag_match.group(1)
    print(f"Flag: flag{{{flag_text}}}")
else:
    print("Flag not found in the decoded text.")
