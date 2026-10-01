#         *   
#       *   *   
#     *   *   *   
#   *   *   *   *   
# *   *   *   *   * 

no = int(input("Enter limit => "))

for i in range(no, 0, -1):

    for j in range(i - 1):
        print("  ", end="")

    for j in range(no , i-1, - 1):
        print("*" ,"  ", end="")

    print()