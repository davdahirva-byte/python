
# 21. Given two integer numbers, return their product only if the product is equal to or lower than 50;
# else, return their sum.
# Example 1:
# •	number1 = 25
# •	number2 = 30
# •	Output: The result is 750. 
# Example 2:
# •	number1 = 40
# •	number2 = 3
# •	Output: The result is 43.

num1=int(input("enter the num1"  ))
num2=int(input("enter the num2"  ))

if num1<=50 and num2<=50:
    print("product",num1*num2)
else:
    print("sum",num1+num2)
