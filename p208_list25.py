# Write a Python program to count the number of even and odd numbers in a list.

# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result:

# Even numbers: 6  
# Odd numbers: 3

list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

even=0
odd=0

for i in list:
    if i % 2 == 0:
      even=even+1
    else:
       odd=odd+1
print("even",even)
print("odd",odd)
