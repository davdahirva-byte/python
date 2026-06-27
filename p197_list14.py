# Write a Python program to change the sign of elements in a list.

# Sample List: [11, -44, 500, -22, -99, -77, 200, -66, 2]

# Expected Result: [-11, 44, -500, 22, 99, 77, -200, 66, -2]


l1=[11, -44, 500, -22, -99, -77, 200, -66, 2]
l2=[]

for x in l1:
    l2.append(x*-1)
print(l1)
print(l2)    