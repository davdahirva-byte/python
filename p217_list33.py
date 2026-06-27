# 33. After throwing the dice several times, you got this
# result,dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# Using a for loop find out the followings:How many times have you got 6s

dice_result = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
count=0
for x in dice_result:
    if x==6:
        count=count+1

print(count,"dice is got 6s")        
