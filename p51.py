# 31. Ask the user to enter age, gender (M or F), and then using the following rules, print their place of service:
# •	If the employee is female, she will work only in urban areas.
# •	If the employee is male and age is between 20 to 40, he may work anywhere.
# •	If the employee is male and age is between 40 to 60, he will work in urban areas only.
# # •	Any other input of age should print "ERROR".

age=int(input("enter age=> "))
gender=input("enter gender(M-F)")

if gender=='F':
    print("she will work only urban areas")
elif gender=='M' and age>20 and age<40:
    print(" he may work anywhere")   
elif gender=='M' and age>40 and age<60:
    print("  he will work in urban areas only")
else:
    print("ERROR")            