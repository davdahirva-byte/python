# 26. Accept the age, gender ('M', 'F'), number of days, and display the wages accordingly.
# Age	Gender	Wage/day
# >= 18 and < 30	M	700
# 	F	750
# >= 30 and <= 40	M	800
# 	F	850

age=int(input("enter age"))
gender=input("enter gender(M-F)")
days=int(input("enter days"))
wage=0

if age>=18 and age<30 and gender=='M':
    wage=700
    
elif age>=18 and age<30 and gender=='F':
    wage=750
    
elif age >= 30 and age<= 40 and gender=='M':
    wage=800

elif age >= 30 and age<= 40 and gender=='F':
    wage=850
else:
    print("invalid")    

total=wage*days

print(total)




