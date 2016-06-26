#!/usr/bin/python
import sys
host=""
prev_host=""
for line in sys.stdin:
    host,dd,hh,mm,ss=line.split("%")
    if host==prev_host:
        dd2,hh2,mm2,ss2=dd,hh,mm,ss
    else:
        if prev_host:
            if [dd1,hh1,mm1,ss1]==[dd2,hh2,mm2,ss2]:
                print "{0}: first visit:{1}".format(host,dd1+"/AUG/1995: "+hh1+":"+mm1+":"+ss1[:-1])
            else:
                ss1=int(ss1)
                mm1=int(mm1)
                hh1=int(hh1)
                dd1=int(dd1)
                ss2=int(ss2)
                mm2=int(mm2)
                hh2=int(hh2)
                dd2=int(dd2)
                if ss2<ss1:    #second difference
                    tdss=ss2+60-ss1
                    mm2-=1
                else:
                    tdss=ss2-ss1
                if mm2<mm1:    #minute difference
                    tdmm=mm2+60-mm1
                    hh2-=1
                else:
                    tdmm=mm2-mm1
                if hh2<hh1:    #hour difference
                    tdhh=hh2+60-hh1
                    dd2-=1
                else:
                    tdhh=hh2-hh1
                tddd=dd2-dd1
                timedifference=str(tddd)+"dd, "+str(tdhh)+"hh, "+str(tdmm)+"mm, "+str(tdss)+"ss"
                print "{0}: time difference:{1}".format(host,timedifference)
        dd1,hh1,mm1,ss1=dd,hh,mm,ss
        dd2,hh2,mm2,ss2=dd,hh,mm,ss
        prev_host=host
if prev_host==host:    #the last line
    if [dd1,hh1,mm1,ss1]==[dd2,hh2,mm2,ss2]:
        print "{0}: first visit:{1}".format(host,dd1+"/AUG/1995: "+hh1+":"+mm1+":"+ss1[:-1])
    else:
        ss1=int(ss1)
        mm1=int(mm1)
        hh1=int(hh1)
        dd1=int(dd1)
        ss2=int(ss2)
        mm2=int(mm2)
                                                                                                                                                            1,1           Top
        prev_host=host
if prev_host==host:    #the last line
    if [dd1,hh1,mm1,ss1]==[dd2,hh2,mm2,ss2]:
        print "{0}: first visit:{1}".format(host,dd1+"/AUG/1995: "+hh1+":"+mm1+":"+ss1[:-1])
    else:
        ss1=int(ss1)
        mm1=int(mm1)
        hh1=int(hh1)
        dd1=int(dd1)
        ss2=int(ss2)
        mm2=int(mm2)
        hh2=int(hh2)
        dd2=int(dd2)
        if ss2<ss1:    #second difference
            tdss=ss2+60-ss1
            mm2-=1
        else:
            tdss=ss2-ss1
        if mm2<mm1:    #minute difference
            tdmm=mm2+60-mm1
            hh2-=1
        else:
            tdmm=mm2-mm1
        if hh2<hh1:    #hour difference
            tdhh=hh2+60-hh1
            dd2-=1
        else:
            tdhh=hh2-hh1
        tddd=dd2-dd1
        timedifference=str(tddd)+"dd, "+str(tdhh)+"hh, "+str(tdmm)+"mm, "+str(tdss)+"ss"
        print "{0}: time difference:{1}".format(host,timedifference)
                                                                                                                                                            72,1          Bot
