# 16. Write a Python program to remove even numbers from a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# Expected Result: [11,99, 77, 11]

# Hint: Use a loop or list comprehension to filter out even numbers by checking if number % 2 == 0.

List=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

odd=[]
for i in List:
    if i % 2==1:
        odd.append(i)

print(odd)

