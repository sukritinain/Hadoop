#!/usr/bin/python

import sys

words = set()

for line in file('terms.txt'):
    words.add(line.strip())

for line in sys.stdin:
    for w in line.split():
        if w in words:
            print '%s\t1' % w