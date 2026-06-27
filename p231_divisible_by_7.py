t1=(23,14,12,21,28,2,45)

sum=0
count=0

for x in t1:
    if x % 7 == 0:
        print(x)
        sum=sum+x
        count=count+1

print(sum,"sum")
print(count,"count")