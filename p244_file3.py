f1=open("abc","r")
c1=0
data=f1.read()

for x in data:
    if x != x.isupper():
        c1=c1+1    

f1.close()
print("lower =",c1)