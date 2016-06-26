#!/usr/bin/python

import sys

mean = 0 
for line in sys.stdin:
	data = line.strip().split()
	if ( len(data[1:])/2 > 4 ):
		for i in range(2,len(data),2):
			mean = mean + float(data[i])
		mean = mean / (len(data[1:])/2)
		print  mean,data[0]
	mean = 0 
			

	
