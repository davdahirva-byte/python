# Write a program to input a number and count the 
# number of digits. The program further checks whether 
# the number contains an odd number of digits or even
# number of digits.

n=input("enter num ")

count=len(n)

print("count",count)

if count % 2==0:
    print("even num")

else:
    print("odd")    