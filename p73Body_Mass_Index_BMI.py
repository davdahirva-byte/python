# Create a Python program that checks if a person's BMI (Body Mass Index) is underweight, 
# normal weight, overweight, or obese. 
# Use the following categories: underweight (BMI < 18.5), 
# normal (18.5 ≤ BMI < 24.9), overweight (25 ≤ BMI < 29.9),and obese (BMI ≥ 30).
#  Ask the user to enter their BMI and print the corresponding category.

BMI=float(input("enter BMI"))

if BMI<18.5:
    print("underweight")
elif 18.5<BMI<24.9:
    print("normal") 
elif 25<= BMI < 29.9:
    print("overweight")
elif BMI>= 30:
    print("obese")
else:
    print("enter valid input")              

