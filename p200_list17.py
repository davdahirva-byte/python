# Write a Python program to take a value from the user and add it at a specified index.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Input: Enter position: 2, Enter value: 999

# Expected Result: [11, 999, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Hint: Use the insert() method to add the value at the specified index.

list=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

list.insert(1,999)
print(list)