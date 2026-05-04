n = int(input("enter a number = "))
m = 0
y = 0
c=n

while n > 0:
    y = n % 10
    m = m * 10 + y
    n = n // 10
   
    print(y,m,n)

if c==m:
    print("Palindrome")
else:
    print("not Palindrome")    
