# 8. Grocery Store Billing
# Ask the user to enter:
# •	Price of item
# •	Quantity
# If total bill is above ₹2000, apply 10% discount.
# Display the final amount

price_of_item=int(input("prit enter orice of item"))
quantity=int(input("enter quantity"))

total_bill=price_of_item*quantity
print("total bill",total_bill)

if total_bill>2000:
    discount=total_bill*10/100
    print("discount",discount)
    
    final_price=total_bill-discount
    print("final price",final_price) 
    
else:
    print("no discount")  
     