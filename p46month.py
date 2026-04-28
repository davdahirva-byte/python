# 22. Write a Python program to find the number of days in a month.
# Example:
# •	Input a month number: 2
# •	Input a year: 2016
# •	Output: February 2016 has 29 days.

months=int(input("enter num of months"))
year=int(input("enter year"))

if months==1:
    print("january ",year,"has 31 days")
elif months==2:
    if year%2==0:
        print("february ",year,"has 28 days")
    else:
         print("february ",year,"has 29 days")

elif months==3:
    print("march ",year,"has 31 days")


elif months==4:
    print("april ",year,"has 30 days")


elif months==5:
    print("may ",year,"has 31 days")


elif months==6:
    print("june ",year,"has 30 days")


elif months==7:
    print("july ",year,"has 31 days")


elif months==8:
    print("aguest ",year,"has 31 days")


elif months==9:
    print("september ",year,"has 30 days")


elif months==10:
    print("octomber ",year,"has 31 days")


elif months==11:
    print("november ",year,"has 30 days")


elif months==12:
    print("december ",year,"has 31 days")

else:
    print("invalid month")