#34 . Write a Python program to count the number of strings in a list that have a length greater than 3.
# Sample List: ["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]

# Expected Result: 2 (elephant and hippopotamus have length > 3)

# Hint: Use a loop or list with len() to check the length of each string.

words=["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]
 
count=0

for x in words:
    if len(x)>3:
        count=count+1

print(count)
