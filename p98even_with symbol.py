n=int(input("enter num: "))

for i in range(1,n+1):

    if i%2==0:
        print(i,end="+")
        
    if i==n:
        print(i,end=" ")
        