# Search particular value from the list

t1=(12,23,45,67,88)

value=int(input("enter the num"))

if value in t1:
    print(value,"value found")
else:
    print(value,"not found")    