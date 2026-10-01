f1=open("abc","r")
c1=0
data=f1.read()

for x in data:
    if x.isupper():
        x=7
    print(x,end="")    

f1.close()
print("lower =",c1)