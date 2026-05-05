# A number is said to be Duck if the digit zero is (0) 
# present in it. Write a program to accept a number and 
# check whether the number is Duck or not. The program 
# displays the message accordingly.
#  (The number must not begin with zero)


n=input("enter num")

if n[0]=='0':
    print("invalid num")
else:
    if '0' in n:
        print("duck num") 
    else:
        print("not duck")      