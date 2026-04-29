# 25. Accept the marked price from the user and calculate the net amount to pay according to the following criteria:
# Marked Price	Discount
# > 10,000	20%
# > 7,000 and <= 10,000	15%
# >= 7,000	10%

price=int(input("enter the price"))

if price>10000:
    discount=price*20/100
    print("give %20 discount",discount)

elif price>7000 and price<=10000:
    discount=price*15/100
    print("%15 discount",discount)

elif price>=5000:
    discount=price*10/100
    print("%10 discount",discount)
else:
    print("no discount")     

print(price-discount)       
