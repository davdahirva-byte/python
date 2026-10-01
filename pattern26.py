#    1
#   12
#  123
# 1234

n=int(input("enter the num"))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i):
        print(j,end=" ")
    print( )    
