import math
m=int(input("enter num"))
n=int(input("enter num"))

for i in range(m, n + 1):
    s = int(math.sqrt(i))
    
    if s * s == i:
        print(i, end=" ")
