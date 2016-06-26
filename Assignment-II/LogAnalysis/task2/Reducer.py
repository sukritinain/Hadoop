#!/usr/bin/python




#### WRONG PROGRAM



import sys

temp = None
endTime = 0
starttime = 0

for line in sys.stdin:
	hostname, time = line.split("\t", 1)
	
	if temp and temp != hostname:
		diff = starttime - endTime
		print temp, diff
		temp = hostname

	temp = hostname
	starttime = time
	

if temp != None:
	print temp

