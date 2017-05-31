#!/bin/bash

i=1

while read line;do

if echo $line | grep topic &> /dev/null;then
	echo $line | sed "s/^[0-9]/${i}/g"
	let i=i+1
else
	echo -e "  $line"
fi

done < test.txt

