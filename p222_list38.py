# 38. Write a Python program to check if all elements in a list are positive.

# Sample List 1: [11, 44, 500, 22]

# Sample List 2: [11, -44, 500, 22]

# Expected Result: True for first list, False for second list

# Hint: Use a len() and count=count+1

num1=[11,44,500,22]

count=0

for x in num1:
    if x>0:
        count=count+1
if count==len(num1):
    print("true")
else:
    print("false")

num2=[11,-44,500,22]

count=0

for x in num2:
    if x>0:
        count=count+1
if count==len(num2):
    print("true")
else:
    print("false")
