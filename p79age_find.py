# <!-- find your current age -->

import time
t=time.localtime()

year=int(input("enter your year "))

y=t.tm_year

age=y-year

print("age",age)


