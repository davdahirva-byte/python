t1=(1,2,3,4,5,6)

for x in t1:
    if x % 2 == 1:
        print(x,"even")

"""sum count"""

t1=(1,2,3,4,5,6,7)

count=0
sum=0

for x in t1:
    if x % 2 ==1:
        print("even",x)
        sum=sum+x
        count=count+1
print(count,"count")    
print(sum,"sum")