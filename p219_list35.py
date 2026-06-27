# 35. Write a Python program to replace all negative numbers in a list with zero.

# Sample List: [11, -44, 500, -22, -99, 77, 200, -66, 2]

# Expected Result: [11, 0, 500, 0, 0, 77, 200, 0, 2]

# Hint: Use a loop or list check if each number is less than 0 and replace it with 0.

l1=[11, -44, 500, -22, -99, 77, 200, -66, 2]

l2=[]
for x in l1:
    if x<0:
        l2.append(0)
    else:
        l2.append(x)
print(l2)