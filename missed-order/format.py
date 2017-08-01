#! /usr/bin/env python3

import sys

try:
  before = open('./before.txt', 'r')
  after = open('./after.txt', 'w')
  num=0

  content=before.readlines()

  for line in content:
    if "topic" in line:
      num=num+1
      print(line.replace("1",str(num)), end='', file=after)
    else:
      print(line, end='', file=after)

  before.close()
  after.close()

except FileNotFoundError:
  print("before.txt is not exist in this directory")
  sys.exit()
