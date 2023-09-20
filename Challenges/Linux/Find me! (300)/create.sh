#!/bin/bash

#|##############################|#
#| Chronos Security             |#
#| https://chronossec.site      |#
#| https://github.com/ChronosPK |#
#|##############################|#

for repeat in {1..10}; do
	for i in {1..15}; do mktemp -d dir-XXXX; done
	
	
	for dir in `ls | grep -v '0-*'`; do
		for file in {0..9}{a..z}; do
			echo "flag{wrong_one!!!}" > $dir/flag${file}.txt
		done
	done

	# add the flag to a random file
	flag=`find dir-*  -type f | shuf -n 1`
	echo "flag{you_found_me}" > $flag
	
	zip -r zip${repeat}.zip dir-*
	rm -rf dir-*
	zip -r find-me.zip zip*
	rm -rf zip*
done
