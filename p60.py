# Exam Eligibility

# Ask the user to enter:
# •	Total classes conducted
# •	Classes attended
# Calculate attendance percentage and display whether the student is eligible for exam (≥ 75%).

classes_conducted=int(input("enter no of class that teacher conducted "))
classes_attended=int(input("enter attended lec. "))

per=(classes_attended/classes_conducted)*100
print(per)
if per>=75:
    print("allowed")
else:
    print("not allowed")    