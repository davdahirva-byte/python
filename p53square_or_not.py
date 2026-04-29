# 29. Take the values of length and breadth of a rectangle from the user and check if it is a square or not.
# Hint: If length and breadth are the same, it is a square.

length=float(input("enter the length "))
breadth=float(input("enter breadth "))

if length==breadth:
    print("it is square")
else:
    print("not square")    
