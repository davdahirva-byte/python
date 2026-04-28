# 16. Write a program where the user enters the temperature and display a message according to the temperature:
# •	Temp < 0: Freezing Atmosphere
# •	Temp 0 to 10: Very cold atmosphere
# •	Temp 10 to 20: Cold Atmosphere
# •	Temp 20 to 30: Normal Atmosphere
# •	Temp 30 to 40: Hot atmosphere
# •	Temp > 40: Very hot atmosphere

temp=int(input("enter temperature"))

if temp<0:
    print("Freezing Atmosphere")
elif temp>0 and temp<=10:
    print("Very cold atmosphere")    
elif temp>10 and temp<=20:
    print("Cold Atmosphere")  
elif temp>20 and temp<=30:
    print("Normal Atmosphere")  
elif temp>30 and temp<=40:
    print("Hot atmosphere")   
elif temp>=40:
    print("Very hot atmosphere")    



