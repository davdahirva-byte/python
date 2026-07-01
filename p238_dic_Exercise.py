# 1. Write a Python script to store value in a dictionary and print.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# Expected Output:
# {"ram": 33, "rahul": 45, "devesh": 30, "jayul": 34, "meena": 29, "nisha": 37, "karan": 40, "anita": 18, "siddhi": 25}

# Hint: Use curly braces {} to define a dictionary and print() to display it.

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# print(marks)

# ................................................................................................................................................................................................


# 2. Write a Python script to print data in vertical form from a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }
# Expected Output:
# ram    33  
# rahul  45  
# devesh 30  
# jayul  34  
# meena  29  
# nisha  37  
# karan  40  
# anita  18  
# siddhi 25  
# Hint: Use a loop to iterate through the dictionary items and print each key-value pair.



# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "nisha": 37,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# for k, v in marks.items():
#     print(k,v)


# ................................................................................................................................................................................................

# 3. Write a Python script to check whether a given key already exists in a dictionary.

# Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "manav": 30,
#     "jayul": 34,
#     "meena": 29,
#     "siddhi": 48
# }
# Enter key for search: rahul
# Output:
# Yes, it exists.

# Hint: Use the in keyword to check if the key is present in the dictionary

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "manav": 30,
#     "jayul": 34,
#     "meena": 29,
#     "siddhi": 48
# }

# search=input("enter the name<=")

# if search in marks:
#     print("yes , it exists")
#     print(search,marks[search])
# else:
#      print("yes , it exists")   


# ................................................................................................................................................................................................

# 4. Write a Python script to print data in vertical form and display whether that student is pass or fail from the dictionary. (18 marks to pass)

# Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }
# Expected Output:

# name     mark   result  
# ram      33     pass  
# rahul    15     fail  
# devesh   30     pass  
# jayul    34     pass  
# jiya     16     fail  
# sadhana  11     fail  
# meena    19     pass  
# karan    20     pass  
# Hint: Use a loop and a conditional statement to determine if each student passed or failed.

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# for k, v in marks.items():
#     if v>18:
#         print(k,v,"pass")
#     else:
#         print(k,v,"fail")    

#  ................................................................................................................................................................................................

#5. Write a Python script to print data in vertical form and display only pass students from the dictionary. (18 marks to pass)

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }
# Expected Output:
# name     mark   result  
# ram      33     pass  
# devesh   30     pass  
# jayul    34     pass  
# meena    19     pass  
# karan    20     pass  

# Hint: Filter the results based on the passing criteria while printing.


# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# for k, v in marks.items():
#       if v>18:
#          print(k,v,"pass")


#  ................................................................................................................................................................................................

# 6. Write a Python program to sum all the items in a dictionary.

# Sample data:

# items = {
#     "maggie": 20,
#     "parleg": 10,
#     "crackjack": 20,
#     "noodles": 32,
#     "chips": 15,
#     "cookies": 18
# }
# Expected Output:
# 125 Rs

# Hint: Use the sum() function combined with values() to calculate the total.

# items = {
#     "maggie": 20,
#     "parleg": 10,
#     "crackjack": 20,
#     "noodles": 32,
#     "chips": 15,
#     "cookies": 18
# }

# total=sum(items.values())

# print("total",total)

#  ................................................................................................................................................................................................

# 7. Write a Python program to remove a key from a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19
# }
# Enter key to delete: rahul

# Expected Output:

# marks = {"ram": 33, "devesh": 30, "jayul": 34, "jiya": 16, "sadhana": 11, "meena": 19}

# Hint: Use the del statement or the pop() method to remove the key from the dictionary

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19
# }

# n = input("Enter name: ")

# if n in marks:
#     marks.pop(n)
#     print("Record deleted")
#     print(marks)
# else:
#     print("Record not found")


# ................................................................................................................................................................................................


# . Write a Python program to find the maximum and minimum marks from a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }
# Expected Output:

# Max: 45, Min: 18

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25
# }

# for k,v in marks.items():
#     print(min(marks[v]))


# # ................................................................................................................................................................................................


# 9. Write a Python program to count the number of students who passed (marks >= 18) in the dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20,
#     "anita": 25
# }

# Expected Output:

# Number of passed students: 5

# Hint: Use a loop and a counter variable to keep track of the number of students who meet
# the passing criteria.

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20,
#     "anita": 25
# }

# count = 0

# for k, v in marks.items():
#     if v >= 18:
#         count = count + 1

# print("Number of passed students:", count)

# ................................................................................................................................................................


# 10. Write a Python program to update a dictionary with new student marks.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45
# }
# Enter new data:
# devesh 30
# Expected Output:
# {"ram": 33, "rahul": 45, "devesh": 30}

# Hint: Use the syntax dict[key] = value to add new key-value pairs.

# marks = {
#     "ram": 33,
#     "rahul": 45
# }

# name = input("Enter student name: ")
# mark = int(input("Enter marks: "))

# marks[name] = mark

# print(marks)

# .................................................................................................................................................................................................

# 11. Write a Python program to get a list of all keys in a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }

# Expected Output:
# ["ram", "rahul", "devesh", "jayul"]

# Hint: Use the keys() method to obtain the keys and convert them to a list if needed

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }

# print(list(marks.keys()))

# ........................................................................................................................................................................................

# 12. Write a Python program to get a list of all values in a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }
# Expected Output:
# [33, 45, 30, 34]

# Hint: Use the values() method to get the values and convert them to a list if needed.


# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34
# }

# print(list(marks.values()))

# ....................................................................................................................................................................................................

# 13. Write a Python program to print only the students who failed from the dictionary (marks < 18).

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }
# Expected Output:
# name     mark   result  
# rahul    15     fail  
# jiya     16     fail  
# sadhana  11     fail  
# Hint: Use a loop and conditional statements to filter and display students who failed.

# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }

# for k , v in marks.items():
#     if v<18:
#         print(k,v,"fail")

# ...........................................................................................................................................................................

# 14. Write a Python program to get the length of a dictionary.

# Sample data:

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16
# }
# Expected Output:
# Length of dictionary: 5

# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16
# }

# print(len(marks),("length of dic"))


# ....................................................................................................................................................................................................
# . We have following information on countries and their population (population is in crores),
# Country Population
# China 	143
# India 	136
# USA 	32
# UK 	21

# Using above create a dictionary of countries and its population

# Write a program that asks user for 4 type of inputs,

# option 1 print: if user enter print then it should print all countries with their population in this format,

#         china==>143
#         india==>136
#         usa==>32
#         uk==>21

# option 2 add: if user input add then it should further ask for a country name to add. 
# If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

# option 3 remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

# option 4 query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


# country={"China":143,
# "India" :	136,
# "USA": 	32,
# "UK": 	21,}

# choice=input("enter choice: ")

# if choice == "print":
#       for k,v in country.items():
#         print(k,v)


# if choice=="add":
#     c = input("enter a country = ")
    
#     if c in country:
#        print("It exists")
#     else:
#        p = int(input("enter a population = "))

#        country[c] = p

#        for k ,v in country.items():
#           print(k,v)
        

# if choice=="remove":
#    name=input("enter country name")

#    if name in country:
#     country.pop(name)

#     for k,v in country.items():
#         print(k,v)
#    else:
#     print("not exist")


# if choice=="query":
   
#    name=input("enter the name")

#    if name in country:
#       print(name,country[name])

#    else:
#       print("country not exist") 

# ..................................................................................................................................................................................

# 16. You are given following list of stocks and their prices in last 3 days,

# Stock 	Prices
# info 	[600,630,620]
# ril 	[1430,1490,1567]
# mtl 	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,
            
# option 1, print: When user enters print it should print following,

# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33

# option 2, add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

# stocks={
# "info": 	[600,630,620],
# "ril": 	[1430,1490,1567],
# "mtl": 	[234,180,160]
# }

# choice=input("enter choice==>")

# if choice=="print":
#     for k,v in stocks.items():
#         avg=sum(v)/len(v)
#         print(k,v,"avg",avg)

# if choice=="add":
#     name=input("enter stock")

#     if name in stocks:
#         print("already exist")
#     else:
#         p=int(input("enter price"))

#         stocks[name]=[p]

#         for k,v in stocks.items():
#             print(k,v)

# .................................................................................................................................................................
# 17. Let's say your expenses for every month are listed below:

# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# June - 1980
# July - 2400
# August - 2250
# September - 2100
# October - 2400
# November - 2150
# December - 2500

# Create a Dictionary to store these monthly expenses and using that find out:

# 1.	In February, how many dollars did you spend extra compared to January?
# 2.	Calculate your total expenses for the first quarter (January to March) of the year.
# 3.	Check if you spent exactly 2400 dollars in any month.
# 4.	Modify the expense for June (2080 dollars) to your monthly expenses.
# 5.	You returned an item that you bought in April and received a refund of 200 dollars. 
# 6.	Determine which month had the highest expense and print the month and the amount.
# 7.	Calculate the average monthly expense for the first half of the year (January to June).
# 8.	Find the month with the lowest expense and print the month and the amount.


expenses = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190,
    "June": 1980,
    "July": 2400,
    "August": 2250,
    "September": 2100,
    "October": 2400,
    "November": 2150,
    "December": 2500
}

# extra=expenses["February"]-expenses["January"]

# print("extra expense",extra)

# print("...................2.............................")

# total_expense=expenses["January"]+expenses["February"]+expenses["March"]

# print("total_expense",total_expense)

# print("....................3............................")

# for k,v in expenses.items():
#     if v==2400:
#      print(v,k)

# print("...................4.............................")
# expenses["June"]=2080
# print(expenses)

# print("...................5.............................")
# expenses["April"]=expenses["April"]-200
# print(expenses)


# print(".....................6...........................")
# print(max(expenses.values()))

# for k,v in expenses.items():
#     if v==max(expenses.values()):
#         print(k,v)


# print(".....................7...........................")
# total=expenses["January"]+expenses["February"]+expenses["March"]+expenses["April"]+expenses["May"]+expenses["June"]

# avg=total/6

# print("avg of jan to june",avg)

# print(".....................6...........................")

# print(min(expenses.values()))

# for k,v in expenses.items():
#     if v==min(expenses.values()):
#         print(k,v)

# ..................................................................................................................................................................................................

# 18. You and your wife argued about expenses last night. You both want to know who is spending more in a month. Now you both go to the Little Yoda he is a good python programmer. He suggested that both of you add an entry in a dictionary next time you spend money. So that you can have a clear picture of your expenses and plan to reduce them. Both dictionaries are as below-
# Your expenses -

# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980
# Your Wife’s expenses -

# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999
# Find out the total expenses for each of you.
# Find out who spending more
# Find out which thing you and your wife spending more


husband_exp={
"Clothes" : 1100,
"Shoes" : 1000,
"Watch" : 900,
"Mobile Recharge" : 699,
"Petrol" : 1980
}

wife_exp={
"Mobile Recharge" : 799,
"DTH recharge" : 999,
"Clothes" : 2310,
"Makeup" : 3670,
"Shoes" : 999
}

total_husband_exp=sum(husband_exp.values())
print(total_husband_exp,"husband_exp")

total_wife_exp=sum(wife_exp.values())
print(total_wife_exp,"wife_exp")

if total_husband_exp > total_wife_exp:
    print("husband_exp",total_husband_exp)
else:
    print("wife_exp is more",total_wife_exp)    

# print(max(husband_exp.values()))

for k, v in husband_exp.items():
    if v==max(husband_exp.values()):
        print(k,v)



# print(max(wife_exp.values()))

for k, v in wife_exp.items():
    if v==max(wife_exp.values()):
        print(k,v)