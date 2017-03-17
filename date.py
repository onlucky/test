
import calendar
import time
import datetime


tick=time.time()
print("时间",tick)

today=time.localtime()
print("localtime",today)

tt=time.asctime()
print("tt",tt)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y%m%d%H%M%S",time.localtime()))

if False==calendar.isleap(2017):
    print("2017不是闰年")

cal=calendar.leapdays(2001,2017)
print("cal:",cal)

cal2=calendar.month(2017,5)
print("cal2:",cal2)

print("Start : %s" % time.ctime())
time.sleep( 2 )
print("End : %s" % time.ctime())

print(calendar.calendar(2017))
print(calendar.prcal(2016))
print(calendar.weekday(2017,4,2))
