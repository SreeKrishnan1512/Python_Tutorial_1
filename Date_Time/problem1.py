from datetime import datetime
import time

x=time.localtime()
dt=datetime.now()
print(dt.year,dt.strftime("%Y"))
print(dt.month,dt.strftime("%B"),dt.strftime("%b"),dt.strftime("%m"))
print(dt.day,dt.strftime("%d"),dt.strftime("%D"))
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.microsecond)
print(x.tm_isdst)


print(dt)

print(dt.strftime("%a"))#%a for day
print(dt.strftime("%c"))#Thu Dec 12 21:17:23 2024
print(dt.strftime("%e"))
print(dt.strftime("%h"))#Dec
print(dt.strftime("%j")) #347th day
print(dt.strftime("%p"))# PM
print(dt.strftime("%r")) #09:21:52 PM

