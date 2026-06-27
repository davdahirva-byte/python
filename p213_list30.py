# 30. Using following list of cities per country,

# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# Do the following task:

# 1.	Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("enter city name=>")

if city in india:
    print(city,"in india")
elif city in pakistan:
    print(city,"in pakistan")  
elif city in bangladesh:
    print(city,"bangladesh")   
else:
    print("not found")