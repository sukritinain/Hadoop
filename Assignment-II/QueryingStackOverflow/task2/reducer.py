#!/usr/bin/python
import sys

previous = None
count = 0
questions = []
for line in sys.stdin:
    line = line.strip().split()
    this,questionId = line

    if ( previous and this != previous) :
        print total,previous, ','.join(questions)
        count = 0
        questions = []

    previous = this
    count = count + 1
    questions.append(questionId)

if (previous != None) :
    print count,previous,','.join(questions)