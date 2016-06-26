#!/usr/bin/python
import sys

count = 0
previous = None
ListOfFiles = []
i = 0

for line in sys.stdin:
	words, FileName = line.strip().split()

	if previous and previous != words:
		ListOfFiles.insert(i,[FileName,count])
		StringListofFiles = str(ListOfFiles)
		temp = StringListofFiles.strip('[]')
		files = ('{{({})}}'.format(temp))
		print previous,":",len(ListOfFiles),":",files
		count = 0
		i += 1
		ListOfFiles = []
		
	previous = words
	count += 1

if previous != None:
	ListOfFiles.insert(i,[FileName,count])
	StringListofFiles = str(ListOfFiles)
	temp = StringListofFiles.strip('[]')
	files = ('{{({})}}'.format(temp))
	print previous,":",len(ListOfFiles),":",files

