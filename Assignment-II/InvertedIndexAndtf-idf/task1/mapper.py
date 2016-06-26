#!/usr/bin/python
import sys
import os

filename = os.environ['mapreduce_map_input_file']

path, File = os.path.split(filename)

for line in sys.stdin:
	data = line.strip().split()

	for word in data:
		print word, File