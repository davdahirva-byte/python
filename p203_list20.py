# . Write a Python program to check if the first and last numbers in a list are the same.

# Sample List 1: [100, 200, 320, 40, 100]

# Sample List 2: [751, 6, 3, 5, 9]

# Expected Result: True for the first list, False for the second list

# Hint: Compare list[0] with list[-1] to check if the first and last numbers are the same.


list1=[100, 200, 320, 40, 100]

if list1[0]==list1[4]:
    print("true")
else:
    print("false")


list2=[751, 6, 3, 5, 9]

if list2[0]==list2[4]:
    print("true")
else:
    print("false")

