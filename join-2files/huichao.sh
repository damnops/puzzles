#!/bin/bash

while read line1;do
	var1=`echo $line1 | awk '{print $1}'`
	if !grep ${var1} file2.txt &> /dev/null;then
		echo $line1 >> join.txt
	fi
	while read line2;do
		var2=`echo $line2 | awk '{print $1}'`
		if [ $var1 == $var2 ];then
         	       echo -n $line1 >> join.txt
                       echo "$line2" | awk '{print " "$2 $3 $4}' >> join.txt
		fi
	done < file2.txt
done < file1.txt

while read line2;do
                var2=`echo $line2 | awk '{print $1}'`
		grep ${var2} file1.txt &> /dev/null
                if [ $? -eq 1 ];then
                        echo $line2 >> join.txt
                fi
done < file2.txt

