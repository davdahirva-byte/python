list=['a','e','i','o','u','A','E','I','O','U']
f1=open("abc","r")
f2=open("pqr","w")
data=f1.read()
 
for x in data:
    if x in list:
      f2.write(x) 
f1.close()
f2.close()

print("copied")