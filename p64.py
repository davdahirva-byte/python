# 12. ATM Withdrawal
# Ask the user to enter:
# •	Account balance
# •	Withdrawal amount
# Check whether withdrawal is possible or not and display remaining balance.

account_balance=int(input("enter account balance"))
withdrawal_amount=int(input("enter withdrawal_amount"))

if withdrawal_amount<account_balance:
    print("withdrawl is possible")
else:
    print("withdrawel not posible")  

amount= account_balance-withdrawal_amount
print(amount)     