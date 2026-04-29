import time

t=time.localtime()

m=t.tm_mon
d=t.tm_mday
y=t.tm_year

print(d,"-",m,"-",y)