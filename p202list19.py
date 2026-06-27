# Write a Python program to find common items from two lists.

# Sample List 1: [11, 44, 500]

# Sample List 2: [77, 44, 11]

# Expected Result: [11, 44]

# Hint: Use loop to find common elements.

list1=[11, 44, 500]
list2=[77,44,11]

common=[]

for i in list1:
    if i in list2:
        common.append(i)

print(common)