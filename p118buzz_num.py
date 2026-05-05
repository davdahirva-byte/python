# Write a program to display all the 'Buzz Numbers' 
# between p and q (where p<q). A 'Buzz Number' is the 
# number which ends with 7 or is divisible by 7.

p=int(input("enter num "))
q=int(input("enter num "))

for i in range(p,q+1):
    if i % 7==0 or i % 10 ==7:
        print(i,end=" ")