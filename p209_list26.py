# 26. Write a Python program to swap the first and last element of a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: [2, 44, 500, 22, 99, 77, 200, 66, 11]

# Hint: Swap list[0] and list[-1] directly.

list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

list[0],list[-1]=list[-1],list[0]

print(list)