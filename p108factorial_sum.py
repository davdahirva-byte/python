n=int(input("enter num: "))
fact=1
sum=0

for i in range(n,0,-1):
    fact=fact*i
    print(i,end=" x")
    sum=sum+(i)
print("\nsum",sum)    