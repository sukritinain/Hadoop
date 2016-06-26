#!/usr/bin/python

import sys
lineLength = 0
wordTotal = 0

for line in sys.stdin:
        data = line.split()

        for i in range(len(data)):
        	wordTotal += 1

        lineLength += 1

print wordTotal, lineLength
