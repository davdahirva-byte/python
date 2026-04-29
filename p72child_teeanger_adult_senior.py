# 36. Write a Python program that evaluates a person's age to determine if they are a child, teenager, adult, or senior. 
# Define a child as 0-12 years, a teenager as 13-19 years, an adult as 20-64 years, and a senior as 65 years and above. 
# Ask the user to enter their age and print the corresponding category.

age=int(input("enter the age"))

if age<=12:
    print("child")
elif age>12 and age<=19:
    print("teenager")
elif age>20 and age<=64:
    print("adult")
else:
    print("senior")    