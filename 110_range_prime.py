for n in range(33,66):
    y=0
    for i in range(2,n):
        if n%i==0:
            y=1
            break

    if y==0:
        print(n,"prime")
