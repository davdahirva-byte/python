n = int(input("enter a number = "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if (i == 2 and j == 1) or (i == 3 and (j == 1 or j == 3)) or (i == 4 and (j % 2 == 0)) or (i == 5 and (j % 2 == 0)):
            print(0,end = " ")
        else:
            print(1,end = " ")
    print( )