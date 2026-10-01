f1=open("abc","r")
c=0
c1=0
data=f1.read()

for x in data:
    if x.isupper():
        c=c+1
    if x.islower():
        c1=c1+1    

f1.close()
print("upper =",c)
print("lower =",c1)