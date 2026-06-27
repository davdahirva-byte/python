# 3. Write a Python program to print whether the values in a list are odd or even.
# Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

# Expected Result:

# 11 is odd  
# 44 is even  
# 500 is even  
# 22 is even  
# 99 is odd  
# 77 is odd  
# 200 is even  
# 66 is even

# Hint: Loop through the list and use the modulus operator % to determine odd or even status.



list=[11, 44, 500, 22, 99, 77, 200, 66, 2]

for i in list:
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")    
