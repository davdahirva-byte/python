# 9. Travel Distance Checker
# Ask the user to enter distance in kilometers.
# Display whether the trip is Short (<10 km) or Long (≥10 km).

distance=int(input("enter enter distance in kilometers"))

if distance<=10:
    print("trip is short")
else:
    print("trip is long")
