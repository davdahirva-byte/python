n = int(input("enter num: "))

for i in range(1, n+1):

    for j in range(i):

        if i % 2 == 1:
            print(1, end="")
        else:
            print(0, end="")

    print()       