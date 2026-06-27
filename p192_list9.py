# Write a Python program to print a list in ascending and descending order.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
# Expected Result:
# Ascending: 2 11 22 44 66 77 99 200 500  
# Descending: 500 200 99 77 66 44 22 11 2
# Hint: Use the sort() and reverse() functions.


list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

list.sort()
print("ascending",list)

list.reverse()
print("descending",list)