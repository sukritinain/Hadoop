#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    idm = line[0].split()

    print idm[1],'->',idm[2]