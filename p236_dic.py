# import random
# stu={}
# n=int(input("enter the limite<="))

# for i in range(1,n+1):
#     marks=random.randint(1,50)
#     stu[i]=marks

# for k,v in stu.items():
#     print(k,v)   

# ................................................................................................................
# # 1) 1 22 pass

# import random
# stu={}
# n=int(input("enter the limite<="))

# for i in range(1,n+1):
#     marks=random.randint(1,90)
#     stu[i]=marks
    
# for k,v in stu.items():
#     if v<40:
#         print(k,v,"fail")
#     else:
#         print(k,v,"pass")    

# .....................................................................................................................

# import random
# emp={}
# n=int(input("enter the limite<="))

# for i in range(1,n+1):
#     salary=random.randint(5000,50000)
#     emp[i]=salary


# for k,v in emp.items():
#     if v>35000:
#         print(k,v,"good salary")
#     else:
#         print(k,v,"do ur best")

# ............................................................................................................

import random
emp={}
n=int(input("enter limite<="))

for i in range(1,n+1):
    salary=random.randint(5000,50000)
    emp[i]=salary

for k,v in emp.items():
    print(k,v)

print("Minimum Salary =", min(emp.values()))

print("Minimum Salary =", max(emp.values()))