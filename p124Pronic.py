n = int(input("Enter number = "))

for i in range(n):
    if i * (i + 1) == n:
        print("Pronic Number")
        break
else:
    print("Not a Pronic Number")