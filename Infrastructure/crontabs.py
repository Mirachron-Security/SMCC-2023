#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

import os
from find_path import find_path

scripts = ["start_dockers.sh", "start_scripts.py", "start_scripts.sh"]
for script in scripts:
    script_path = find_path('.', script)
    os.system(f"echo @reboot {script_path!r} >> /etc/crontab")
    os.system(f"echo 5 * * * * {script_path!r} >> /etc/reboot")
