# Write a Python program to find elements larger than a given value in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Input: Enter greater than value: 50

# Expected Result: 500 99 77 200 66

# Hint: Use a loop or list comprehension to filter numbers greater than the given value.

list=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]


num=int(input("Enter num"))
print(num)
for i in list:
    if i>num:
        print(i,end=" ")