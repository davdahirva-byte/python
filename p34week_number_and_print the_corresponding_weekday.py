# 13. Write a Python program to input a week number and print the corresponding weekday.
# Example:
# •	Enter week number => 2
# •	Output: Tuesday.

week=int(input("enter num"))

if(week==1):
    print("monday")
elif(week==2):
    print("tuesday")
elif(week==3):
    print("wednesday")
elif(week==4):
    print("thursday")
elif(week==5):
    print("friday")
elif(week==6):
    print("saturday")
elif(week==7):
    print("sunday")
else:
    print("enter valid num")
