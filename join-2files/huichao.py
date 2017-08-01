#! /usr/bin/env python3

dict_data1 = {}
with open("./file1.txt", 'r') as df:
  for kv in [d.strip().split() for d in df]:
    dict_data1[kv[0]] = kv[1:]

dict_data2 = {}
with open("./file2.txt", 'r') as df:
  for kv in [d.strip().split() for d in df]:
    dict_data2[kv[0]] = kv[1:]

for line in dict_data1:
  if line in dict_data2:
    print(line + " ".join(dict_data1[line]) + " " +  " ".join(dict_data2[line]))
  else: 
   print(line + " ".join(dict_data1[line]))

for line in dict_data2:
  if line in dict_data1:
    continue
  else:
    print(line + " ".join(dict_data2[line]))
