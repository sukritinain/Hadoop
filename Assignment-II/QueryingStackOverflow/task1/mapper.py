#!/usr/bin/python
import sys

def retValue(sub ,xml):
    index =xml.find(sub)
    end = xml.find(' ',index+1)
    return xml[index+len(sub)+2:end-1]

for line in sys.stdin:
    xml = line.strip()


    if (retValue('PostTypeId',xml) == '1'):

        print retValue('ViewCount',xml),'\t',retValue('Id',xml)

