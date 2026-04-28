# 15. Write a Python program that takes two values and a choice (+, -, *, /). If the user presses +, display addition; - for subtraction; * for multiplication; / for division.
# Example:
# •	Enter no1 => 22
# •	Enter no2 => 2
# •	Enter + for Add, - for Sub, * for Mul, / for Div
# •	Enter => -
# •	Output: 20.

num1=int(input("enter num1"))
num2=int(input("enter num2"))

print("+ for add")
print("- for sub")
print("* for mul")
print("/ for div")

choice=input("enter=")

if choice=="+":
     print("output",num1+num2)
elif choice=="-":
     print("output",num1-num2)
elif choice=="*":
     print("output",num1*num2)
elif choice=="/":
     print("output",num1/num2)
else:
     print("enter valid choice")     