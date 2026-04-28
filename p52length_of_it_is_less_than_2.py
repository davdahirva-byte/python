# Ask for the name of the user, and if the length of it is less than 2, then display a message.

name=input("enter the name  ")

if len(name)<2:
    print("name is too short")
else:
    print("valid name")    