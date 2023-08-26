#!/usr/bin/python3

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os


SCRIPT_FILE = "scripts.txt"
with open(SCRIPT_FILE,"r") as file:
	contents = file.read().splitlines()

for script in contents:
	print(script)
	dirname = os.path.dirname(script)
	os.system("pgrep -f {}".format(script))