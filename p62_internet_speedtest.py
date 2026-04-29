# 10. internet Speed Test
# Ask the user to enter download speed (Mbps).
# Display:
# •	Below 10 → Slow
# •	10–50 → Average
# •	Above 50 → Fast


internet_speed=int(input("enter internet speed "))

if internet_speed < 10:
    print("slow")
elif internet_speed > 10 and internet_speed < 50:
    print("average")
elif internet_speed > 50:
    print("fast")  
else:
    print("enter valid input")          
