#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#
# user
useradd -m user -s /bin/bash
echo "user:userpass" | chpasswd

# flag
echo "flag{who_let_the_cat_out?}" > /home/user/flag.txt

# history
ln -sf /dev/null ~/.bash_history

# aliases
echo alias cat=/bin/true >> /home/user/.bashrc
echo alias less=/bin/true >> /home/user/.bashrc
echo alias more=/bin/true >> /home/user/.bashrc
echo alias find=/bin/true >> /home/user/.bashrc
echo alias grep=/bin/true >> /home/user/.bashrc
echo alias egrep=/bin/true >> /home/user/.bashrc
echo alias vi=/bin/true >> /home/user/.bashrc
echo alias vim=/bin/true >> /home/user/.bashrc
echo alias fgrep=/bin/true >> /home/user/.bashrc
echo alias nano=/bin/true >> /home/user/.bashrc
echo alias python=/bin/true >> /home/user/.bashrc
echo alias python2=/bin/true >> /home/user/.bashrc
echo alias python3=/bin/true >> /home/user/.bashrc
echo alias source=/bin/true >> /home/user/.bashrc
echo alias who=/bin/true >> /home/user/.bashrc
echo alias last=/bin/true >> /home/user/.bashrc
echo alias w=/bin/true >> /home/user/.bashrc
