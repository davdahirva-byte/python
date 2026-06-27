# 41. Write a Python program to count how many times a specific value appears in a list.
# Sample List: [11, 44, 500, 22, 99, 11, 22, 66, 2]

# Input: Enter value to count: 11

# Expected Result: 2 (11 appears twice)

# Hint: Use the count() method or a loop to count occurrences of the input value.
#  

list=[11, 44, 500, 22, 99, 11, 22, 66, 2]

value=int(input("enter the value"))

count=0

for i in list:
    if i==value:
        count=count+1

print(count)
