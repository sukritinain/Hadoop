#!/usr/bin/python

import sys
data = []

for line in sys.stdin.readlines():
	if line not in data:
		data.append(line)
		print line


