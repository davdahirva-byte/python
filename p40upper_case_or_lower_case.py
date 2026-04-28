# 18. Write a program to see if the entered letter is in upper case or lower case.
# Example:
# •	Enter letter => a
# •	Output: a is in lowercase;
# •	Enter letter => A
# •	Output: A is in uppercase.

ch=input("enter ch  ")

if ch.islower():
    print("lower ")
elif ch.isupper():
    print("upper")
else:
    print("invalid")    
