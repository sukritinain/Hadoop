#!/usr/bin/env python

import sys
temp = None
Total = 0

for line in sys.stdin:
    data = line.strip()
   
    words = data
    if temp and temp != words:
      print temp, "\t", Total
      temp = words
      Total = 0

    temp = words
    Total += 1

if temp != None:
	print temp, "\t",Total



