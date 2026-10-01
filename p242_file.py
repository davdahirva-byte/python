f1=open("abc","r")
c=0
data=f1.read()

for x in data:
    if x=='a'or x=='e'or x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U':
       print(x,end="")
       c=c+1

print(c)
f1.close()

