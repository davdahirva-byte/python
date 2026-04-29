import time

t=time.localtime()

y=t.tm_year

if y%4==0:
    print(y,"leap year")
else:
    print(y,"not a leap year")    

