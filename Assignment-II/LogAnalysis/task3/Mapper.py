#!/usr/bin/python
import sys
for line in sys.stdin:
    if len(line.split('"'))==3:
        host=line.split(" - -")[0]
        time=line[line.find("[")+1:line.find("]")-6]
        dd=time.split("/")[0]
        hh=time.split(":")[1]
        mm=time.split(":")[2]
        ss=time.split(":")[3]
        print "{0}%{1}%{2}%{3}%{4}".format(host,dd,hh,mm,ss)