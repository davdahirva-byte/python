# 32. You have a list of your favourite desserts.

# desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

# Using this list, find out:

# 1.	How many desserts do you have in your list?
# 2.	Add 'macaron' at the starting  of the list and show it.
# 3.	You want 'ice cream' to be left after 'pavlova'. Remove it from the end and add it at the correct position.

desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

print(len(desserts),("desserts in the list"))

desserts.insert(0,'mecaron')
print(desserts)

desserts.remove('ice cream')
desserts.append('ice cream')

print(desserts)