#!/usr/bin/env python

import sys

for line in sys.stdin:
	words = line.strip().split()

	for i in range(len(words)-1):
		print words[i] , words[i+1]