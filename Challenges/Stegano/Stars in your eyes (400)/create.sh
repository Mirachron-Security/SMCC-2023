#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

### define flag
/usr/bin/python3 -c 'print(" ".join([str(ord(i)) for i in "flag{the_new_guy_is_weird}"]))' > encflag
/usr/bin/cat encflag

### create blank (white) pdf file (we only need one)
/usr/bin/vim blank.txt -c "hardcopy > blank.ps | q" # blank text file
/usr/bin/ps2pdf blank.ps # created blank.pdf

### encode each character of the flag in the serial information (one character for one pdf)
for i in {1..26}; do deda_create_dots --serial $(echo -en "000";cat encflag| cut -d " " -f $i) blank.pdf; mv new_dots.pdf $i.pdf; pdftoppm $i.pdf scan -png; mv scan-1.png $i.png ; done

### merge all files together
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=stars-in-your-eyes.pdf *.pdf 
