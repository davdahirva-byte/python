def Armstrong(n):
    temp = n
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + (digit ** 3)
        n = n // 10

    if sum == temp:
        return 1
    else:
        return 0


num = int(input("Enter a 3-digit number = "))

result = Armstrong(num)

if result == 1:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")