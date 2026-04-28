# 19. Write a program where a user enters the buying price and selling price, then the output should show if the person has made a profit or loss.
# Example:
# •	Buy = 400
# •	Sell = 600
# •	Output: The User has made a profit.

buy=float(input("enter buying price"))
sell=float(input("selling price"))

if(buy>sell):
    print("loss")
else:
    print("profit")    