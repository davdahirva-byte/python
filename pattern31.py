# *    *    *    *    *    
#   *    *    *    *    
#     *    *    *    
#       *    *    
#         *   

no = int(input("Enter limit => "))

for i in range(1,no+1):

    for j in range(i - 1):
        print("  ", end="")

    for j in range(no , i-1, - 1):
        print("*" ,"   ", end="")

    print()