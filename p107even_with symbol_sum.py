n=int(input("enter num: "))

sum=0
for i in range(1,n+1):

    if i%2==0:
        print(i,end="+")
        sum=sum+(i)
print("\nsum",sum)        