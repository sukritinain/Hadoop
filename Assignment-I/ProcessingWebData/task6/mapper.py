#!/usr/bin/env python

import sys

for line in sys.stdin:
	words = line.strip().split()
	
	print words[len(words)-1] ,words[0],words[1]