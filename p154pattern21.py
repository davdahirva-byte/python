n=int(input("enter the num"))

for i in range(1,n+1):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print(i,end="")
    print()        