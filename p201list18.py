# Write a Python program to append one list to another list.

# Sample List 1: [11, 44, 500, 22, 99]

# Sample List 2: [77, 200, 66, 2, 11, 22]

# Expected Result: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Hint: Use the extend() method or + operator to combine the two lists.


list1=[11, 44, 500, 22, 99]
print("list1",list1)

list2=[77, 200, 66, 2, 11, 22]
print("list2",list2)

list1.extend(list2)
print(list1)