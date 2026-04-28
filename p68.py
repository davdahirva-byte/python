# 16. Student Category
# Ask the user to enter age.
# Display category:
# •	Below 13 → Child
# •	13–19 → Teenager
# # •	Above 19 → Adult

age=int(input("enter the age "))

if age<13:
    print("child")
elif age>13 and age<19:
    print("teenage")
else:
    print("adult")        
