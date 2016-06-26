#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.split()
	if len(data) == 4:
		markTag, courseId, studentId, grade = data
		print studentId, courseId, grade
	elif len(data) == 3:
		studentTag, studentId, sname = data
		print studentId, sname