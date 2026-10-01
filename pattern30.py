#         1    
#       1    2    
#     1    2    3    
#   1    2    3    4    
# 1    2    3    4    5 

no = int(input("Enter limit => "))

for i in range(1, no + 1):

    # left spaces
    for j in range(no - i):
        print("  ", end="")

    # numbers
    for j in range(1, i + 1):
        print(j, "  ", end=" ")

    print()