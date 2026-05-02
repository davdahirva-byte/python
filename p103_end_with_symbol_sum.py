n=int(input("enter num"))

sum=0
for i in range(1,n+1):
    if i == n:
        print(i,end=" ")
    else:
        print(i,end="x")

    sum=sum+(i)    