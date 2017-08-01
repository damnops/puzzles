#! /usr/bin/env python3

f = open('./ofile.txt', 'r')
t = open('./noblack.txt', 'w')

lines = f.readlines()

for line in lines:
  if line.split():
    print(line, end='', file=t)

f.close()
t.close()

g = open('./noblack.txt', 'r')

i = 1

context = g.readlines()

for line in context:
  if i%8 == 3:
    print(line, end='') 
  i = i+1
  
g.close()
