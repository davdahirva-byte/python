# 14. Write a Python program that takes two values and a choice (1, 2, 3, or 4). If the user presses 1, display addition; 2 for subtraction; 3 for multiplication; 4 for division.
# Example:
# •	Enter no1 => 22
# •	Enter no2 => 2
# •	Enter 1 for Add, 2 for Sub, 3 for Mul, 4 for Div
# •	Enter => 2
# •	Output: 20.

num1=float(input("enter num1"))
num2=float(input("enter num2"))

print("enter 1 for add")
print("enter 2 for sub")
print("enter 3 for mul")
print("enter 4 for div")

choice=int(input("enter="))

if choice==1:
    print("add",num1+num2)
elif choice==2:
    print("sub",num1-num2)
elif choice==3:
    print("mul",num1*num2)
elif choice==4:
    print("div",num1/num2)

