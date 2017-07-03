#!/bin/bash
grep -v "^$" ofile.txt|awk '{if(NR%8 == 3) print $0}'
