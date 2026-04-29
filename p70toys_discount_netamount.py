# 34. A toy vendor supplies three types of toys: Battery-Based Toys, Battery-Based Toys, and Electrical Charging Based Toys.
# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and 
# a discount of 10% is given on orders for electrical charging-based toys of value more than Rs. 500. 
# Assume that the numeric codes 1, 2, and 3 are used for battery-based toys,
# key-based toys, and electrical charging-based toys, respectively. Write a program that reads the product code and the order
# amount and prints out the net amount that the customer is required to pay after the discount.

toys=input(" enter type of toy").lower()
amount=int(input("enter amount"))

if toys=='Battery-Based_Toys' and amount>1000:
    discount=amount*10/100
    print(discount,"discount")
    total_price=amount-discount
    print(total_price,"total_price")

elif toys== 'key-based_toys' and amount>100:
    discount=amount*5/100
    print(discount,"discount")
    total_price=amount-discount
    print(total_price,"total_price")

elif toys== 'electrical_charging-based_toys' and amount>500:
    discount=amount*5/100
    print(discount,"discount")
    total_price=amount-discount
    print(total_price,"total_price")

else:
    print("enter valid input")    


