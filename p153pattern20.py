# 55555
# 4444
# 333
# 22
# 1

n=int(input("enter num"))

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")

    for j in range(i):
        print(i,end="") 

    print()       