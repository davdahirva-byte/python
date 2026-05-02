i=int(input("enter num"))

sum=0
for i in range(1,i+1):
   
   if i%2==0:
      print(i,end="+")
      sum=sum+(i)
   elif i%2==1:
      print(i,end="-")
      sum=sum-(i)

print("\nsum",sum)   

