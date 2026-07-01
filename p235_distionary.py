stu={1:"kartavya",2:"om",3:"niharika",4:"sorabh"}
print(stu)

for key,value in stu.items():
    print(key,value)\

for key,value in stu.items():
    print(key,value,len(value))    

for key,value in stu.items():
    if len(value)>5:
        print(key,value)

