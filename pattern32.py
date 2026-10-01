#         *   
#       *   *   
#     *   *   *   
#   *   *   *   *   
# *   *   *   *   * 
# *    *    *    *    *    
#   *    *    *    *    
#     *    *    *    
#       *    *    
#         *  

n=int(input("enter the num: "))

for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i):
        print("*","   ",end=" ")
    print( )  


for i in range(1,n+1):

    for j in range(i - 1):
        print("  ", end="")
    for j in range(n , i-1, - 1):
        print("*" ,"  ", end="")

    print()            