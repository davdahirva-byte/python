import time

t=time.localtime()

h=t.tm_hour
m=t.tm_min
s=t.tm_sec

h=h%12
if h==0:
    h=12

if h>=6 and h<12:
    print("GOOD MORNING")
elif h>=12 and h<4:
    print("GOOD AFTERNOON")
elif h>=4 and h<=7:
    print("GOOD EVENING")
elif h>=8 and h<=12:
    print("GOOD NIGHT")
else:
    print("enter valid input")          

print(h, ":", m, ":", s)    