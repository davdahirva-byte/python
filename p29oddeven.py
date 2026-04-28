# 7. Find out whether the given number is odd, even, or 0.
# Example:
# •	Enter no => 22
# •	Output: 22 is even.
# •	Enter no => 23
# •	Output: 23 is odd.
# •	Enter no => 0
# •	Output: The number is 0.

num=int(input("enter num"))

if(num%2==0):
    print(num,"is even")
elif(num%2==1):
    print(num,"is odd")    
elif(num==0):
    print("the num is zero")    
else:
    print("enter valid no")   