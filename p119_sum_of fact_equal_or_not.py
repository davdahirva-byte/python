# Perfect number: (A number is called Perfect if it 
# is equal to the sum of its factors other than the 
# number itself.)

n=int(input("enter num"))
sum=0

for i in range(1,n):
    if n % i==0:
     sum=sum+i

if sum==n:
    print("prefect num")
else:
    print("not prefect")        