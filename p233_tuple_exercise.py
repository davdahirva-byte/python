# t1 = (11, 22, 33, 44, 55)

# print(t1)

#2..........................................................................................

# t1 = (11, 22, "ram", 44, 55.66, "rahul")
# print(t1)

#.............................................................................................
# 3. Write a Python program to create a tuple with numbers and print one item.

# Hint: You can access tuple elements using their index, starting from 0.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# index=int(input("Enter index =>"))
# Expected Output: 33 (for printing the 3rd item)


# t1 = (11, 22, 33, 44, 55)

# index = int(input("Enter index => "))

# print(t1[0])

#...............................................................................................
# 4. Write a Python program to add an item in a tuple.

# Hint: Tuples are immutable, so to add an item, convert the tuple to a list, add the item, then convert it back to a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter data: 100
# Expected Output: (11, 22, 33, 44, 55, 100)

# t1=(11,22,33,44,55)
# l1=[]

# l1=list(t1)

# print(l1)

# l1.append(100)
# print(l1)

# t1=tuple(l1)
# print(t1)

#................................................................................................................................
# 5. Write a Python program to get the 4th element from last of a tuple.

# Hint: You can access tuple elements using positive and negative indices.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output: 44 (for both 4th element and 4th from last)

# t1=(11,22,33,44,55)

# print(t1[-4])

#....................................................................................................................
# 6. Write a Python program to check whether an element exists within a tuple.

# Hint: Use the in keyword to check if an element is present in a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value for search: 44
# Expected Output: Yes, 44 is there

# t1 = (11, 22, 33, 44, 55)
# n=int(input("enter the num"))

# if n in t1:
#     print("yes",n)
# else:
#     print("no",n)    

# .........................................................................................................

# 7. Write a Python program to convert a list to a tuple.

# Hint: Use the tuple() function to convert a list to a tuple.

# Sample data:
# list1 = [11, 22, 33, 44, 55]
# # Expected Output: (11, 22, 33, 44, 55)

# l1 = [11, 22, 33, 44, 55]
# t1=()

# t1=tuple(l1)
# print(t1)

# ....................................................................................................
# . Write a Python program to remove an item from a tuple.

# Hint: Since tuples are immutable, convert the tuple to a list, remove the item, then convert it back to a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value for delete: 22
# Expected Output: (11, 33, 44, 55)


# t1 = (11, 22, 33, 44, 55)
# l1=[]

# n=int(input("enter the num"))

# l1=list(t1)

# print(l1)

# l1.remove(n)
# print(l1)

# t1=tuple(l1)
# print(t1)

# ..................................................................................................

# 9. Write a Python program to find the index of an item in a tuple.

# Hint: Use the index() method to find the position of an element in a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value to find its index: 22
# Expected Output: 1

# t1 = (11, 22, 33, 44, 55)

# n=int(input("enter the num"))

# print(t1[n])

# ..................................................................................................

# 10. Write a Python program to find the length of a tuple.

# Hint: Use the len() function to find the number of elements in a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output: 5


# t1=(11,22,33,44,55)

# print(len(t1),("len"))

# .......................................................................................................

# 11. Write a Python program to reverse a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output: (55, 44, 33, 22, 11)

# t1 = (11, 22, 33, 44, 55)

# print(t1[::-1])


# ...............................................................................................

# . Write a Python program to slice a tuple.

# Hint: Use slicing syntax tuple[start:end] to extract a portion of the tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55, 66, 77)
# Slice from index 2 to 5
# Expected Output: (33, 44, 55)

# t1 = (11, 22, 33, 44, 55, 66, 77)

# print(t1[2:5])


# ........................................................................................................

# . Write a Python program to unpack a tuple into several variables.

# Hint: Use variable unpacking to assign tuple elements to variables.

# Sample data:
# t1 = (11, 22, 33)
# Expected Output:
# a = 11, b = 22, c = 33

# t1 = (11, 22, 33)
# a,b,c=t1

# print(a,"a")
# print(b,"b")
# print(c,"c")

# ...................................................................................................

# 14. Write a Python program to count the occurrences of an item in a tuple.

# Hint: Use the count() method to find how many times an element appears.

# Sample data:
# t1 = (11, 22, 33, 44, 33, 22, 33)
# Enter value to count: 33
# Expected Output: 3

# t1 = (11, 22, 33, 44, 33, 22, 33)
# count=0
# n=int(input("enter the num"))

# for x in t1:
#     if n==x:
#         count=count+1

# print(count)
# .............................................................................................

# 15. Write a Python program to multiply all elements in a tuple by 2.

# Hint: Use a list comprehension or a loop to iterate through the tuple and multiply each element, then convert it back to a tuple.

# Sample data:
# t1 = (1, 2, 3, 4)
# Expected Output: (2, 4, 6, 8)

# t1 = (1, 2, 3, 4)

# for x in t1:
#         print(x*2)


# ...............................................................................................

# . Write a Python program to find the largest and smallest items in a tuple.

# Hint: Use the max() and min() functions.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output:
# Max: 55
# Min: 11

# t1 = (11, 22, 33, 44, 55)

# print(min(t1),("min"))
# print(max(t1),("max"))


# ...............................................................................................
# 16. Write a Python program to sort a tuple of numbers in ascending order.

# Hint: Convert the tuple to a list, sort the list, and convert it back to a tuple.

# Sample data:
# t1 = (55, 22, 33, 11, 44)
# Expected Output: (11, 22, 33, 44, 55)

# t1 = (55, 22, 33, 11, 44)
# l1=[]

# l1=list(t1)
# print(l1)

# l1.sort()

# print(l1)

# t1=tuple(l1)
# print(t1)

# ...................................................................................................
# 17. Write a Python program to merge two tuples.

# Hint: Use the + operator to concatenate two tuples.

# Sample data:
# t1 = (11, 22, 33)
# t2 = (44, 55, 66)
# Expected Output: (11, 22, 33, 44, 55, 66)

# t1=(11,22,33)
# t2=(44,55,66)

# print(t1+t2)

# ..................................................................................................
# Create a list of your friends' names and now create a list of tuples. The tuple should contain the 
# friend’s name and the length of the name. For Example: if someone’s name is Aditya, the tuple would
# be: (‘Aditya’, 6)

l1=["kartavya","hirva","hiral","brinda","ishva"]
l2=[]

for x in l1:
    l2.append((x,len(x)))

print(l2)

