# . Write a Python program to find the index of the maximum value in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result: Index of max value (500) is 2

# Hint: Use max() to find the maximum value, and list.index() to find its index.

list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

max=max(list)
index=list.index(max)

print("index of max value",max,"is",index)
