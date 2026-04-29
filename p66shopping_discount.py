# 15. Online Shopping Coupon
# Ask the user to enter order amount.
# If amount ≥ ₹3000, apply ₹500 discount.
# Display final payable amount.

order_amount=int(input("enter order amount"))

if order_amount>=3000:
    discount=500
    print("discount",discount)

    final_price=order_amount-discount
    print("final price",final_price)       
else:
    print("no discount")    
