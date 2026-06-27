# 37. Write a Python program to find the sum of all numbers divisible by 3 in a list.

# Sample List: [11, 12, 15, 22, 99, 77, 200, 66, 2]

# Expected Result: 192 (12 + 15 + 99 + 66 = 192)

# Hint: Use a loop and the modulus operator % to check divisibility by 3, then add those numbers.

num=[11,12,15,22,99,77,200,66,2]

total=0
for i in num:
    if i % 3 == 0:
        total = total+i

print(total)        