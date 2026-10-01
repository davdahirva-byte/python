l=[]

while True:
   
   print("1.push")
   print("2.pop")
   print("3.insert between")
   print("4.print")
   print("5.add first")
   print("6.delete pos")
   print("7.all")
   print("8.exit")

   ch=int(input("choice"))

   if ch==1:
      a=input("enter element  ")
      l.append(a)

   elif ch==2:
         
         l.pop()

   elif ch==3:
       p=int(input("enter position"))
       a=input("enter the element")
       l.insert(p,a)    

   elif ch==4:
       print("list=",l) 

   elif ch==5:
        x = int(input("Enter Element: "))
        l.insert(0, x)

   elif ch == 6:
        pos = int(input("Enter Position: "))
        if pos >= 0 and pos < len(l):
            l.pop(pos)
            print("Element Deleted")
        else:
            print("Invalid Position")

   elif ch == 7:
        print("Program End")
        break

   else:
        print("Invalid Choice")         
          