import random
x=random.randint(1,50)
y=random.randint(1,50)

print("No1 =",x," No2 = ",y)

u_add=int(input("Enter add ->"))

r_add=x+y

if u_add==r_add:
    print("true")
else:
    print("false")    