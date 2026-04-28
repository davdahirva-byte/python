# A company decided to give a bonus of 5% to employees if their year of service is more than 5 years.

salary=int(input("enter the salary"))
year=int(input("emter year"))

if year>5:
    bonus=salary*5/100
    print("bonus",bonus)
    print(bonus+salary)
else:
    print("no bonus")    