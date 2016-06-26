#!/usr/bin/python

import sys
current = '0'
for line in sys.stdin:
	data = line.strip().split()
 


	if ( current == data [0]):
		print data[len(data)-1],
	else:

		current = data[0]
		print '\n',data[len(data)-1],
			



