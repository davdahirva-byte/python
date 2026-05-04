n=int(input("enter num"))
c=n
sum=0
m=0

while n>0:
    y=n % 10
    m=m*10+y
    sum=sum+y
    n=n//10
    print(y,m,n)
print(sum)
