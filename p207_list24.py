
# 24. Write a Python program to find the second largest number in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: 200

# Hint: Sort the list and get the second-to-last element or use a loop to track the two largest numbers.

list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

list.sort()
print(list)
print("second largest",list[-2])