#!/usr/bin/python

import sys

for line in sys.stdin:    
	line = line.strip()         
	webpage = line.split()[-4]           
	print("{0}\t{1}".format(webpage, 1))