#!/usr/bin/python

import sys

prev_word = ""
value_total = 0
word = ""
max_sum = 0
result = " "

for line in sys.stdin:         
    line = line.strip()        
    word, value = line.split("\t", 1)
    value = int(value)
   
    if prev_word == word:
        value_total += value
    else:            
        value_total = value
        prev_word = word
    
    if value_total > max_sum:
    	max_sum = value_total
        result = prev_word
    


if prev_word == word: 	# For the last key-value pair
	if value_total > max_sum:
		max_sum = value_total
		result = prev_word

print result
