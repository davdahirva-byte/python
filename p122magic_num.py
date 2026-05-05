n = int(input("Enter number = "))

while n > 9:   # jab tak single digit na ho
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    n = sum

if n == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")