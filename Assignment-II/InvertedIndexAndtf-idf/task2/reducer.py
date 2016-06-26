#!/usr/bin/python
import sys
import math 

t = None
count = 0

for line in sys.stdin:
	words, num = line.split()
	num = int(num)

	if t and t != words:
		print t, ",", "d1.txt" , "=", count * math.log(float(1.0/2.0) ,10)
		t = words
		count = num

	t = words
	count += num

if t != None:
	print t,  ",", "d1.txt" , "=", count * math.log(float(1.0/2.0) ,10)