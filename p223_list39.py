# 39. Write a Python program to split a list into two lists: one with even indices and one with odd indices.

# Sample List: [11, 44, 500, 22, 99, 77]

# Expected Result:

# Even indices: [11, 500, 99] (indices 0, 2, 4)

# Odd indices: [44, 22, 77] (indices 1, 3, 5)

# Hint: Use a loop and i %2

num=[11, 44, 500, 22, 99, 77]

odd=[]
even=[]

for i in num:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
