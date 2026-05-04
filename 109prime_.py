n = int(input("Enter number: "))

y=0

for i in range(2,n):
    if n%i==0:
        y=100
        break

if y==0:
    print("prime")
else:
    print("not prime")    