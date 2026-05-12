n = int(input("enter num: "))

for i in range(1, n+1):

    for j in range(n - i):
        print(" ", end="")
        
    if i % 2 == 1:
        for j in range(i):
            print(i, end="")
    else:
        for j in range(i):
            print("*", end="")

    print()