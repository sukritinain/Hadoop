#!/usr/bin/python

import sys

for line in sys.stdin:
	count, line = line.split()
	sorted(count, key=int, reverse=True)
	print count