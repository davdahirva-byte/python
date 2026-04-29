import time

currunt_time=time.localtime()

h=currunt_time.tm_hour
m=currunt_time.tm_min
s=currunt_time.tm_sec

print(h,";",m,":",s)


