# 13. Weather Advisory
# Ask the user to enter temperature in Celsius.
# Display:
# •	Below 15 → Cold
# •	15–30 → Pleasant
# •	Above 30 → Hot

tem=float(input("enter the temp"))

if tem<15:
    print("cold")
elif tem>15 and tem<30:
    print("pleasant") 
else:
    print("hot")       