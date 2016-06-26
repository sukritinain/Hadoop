#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split()
	i = data[0]
	num = data [1:]


	for j in range(len(num)):
		print j,i,num[j]