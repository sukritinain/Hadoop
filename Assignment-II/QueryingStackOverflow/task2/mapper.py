#!/usr/bin/python
import sys
def retValue(sub ,xml):
    index =xml.find(sub)
    end = xml.find(' ',index+1)
    return xml[index+len(sub)+2:end-1]

for line in sys.stdin:
    line = line.strip()
    if (retValue('PostTypeId',line) == '2'):
        print retValue('OwnerUserId',line),'\t',retValue('ParentId',line)