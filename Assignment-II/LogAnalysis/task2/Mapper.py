#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	if line and line.split(' ')[-2] == "404":                 
		host = line.split('- -')[0]               
		print("{0}\t{1}".format(host, 1))