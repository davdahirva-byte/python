n = int(input("enter num: "))

for i in range(1, n+1):

    for j in range(n - i + 1):
        print(i, end="")


    print()