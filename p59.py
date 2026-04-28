# 6. Phone Battery Status

# Ask the user to enter battery percentage.

# Display:
# •	Below 20 → Low Battery
# •	20–80 → Normal
# # •	Above 80 → Fully Charged

battery=int(input("enter your battry per."))

if battery<20:
    print("low battery")
elif battery>20 and battery<80:
    print("normal") 
elif battery>80:
    print("fully charged")
else:
    print("enter valid input")
