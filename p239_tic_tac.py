turn = 1
list1 = ["_","_","_","_","_","_","_","_","_"]

while turn < 10:
    if turn % 2 == 0:
        pos = int(input("enter shyam turn = "))

        if list1[pos - 1] != "_":
            print("This position is already exists")
            continue
        list1[pos - 1] = "x"
    else: 
        pos = int(input("enter hirva turn = "))

        if list1[pos - 1] != "_":
            print("This position is already exists")
            continue

        list1[pos - 1] = "o"

    print("After",turn)
    print(list1[0],"|",list1[1],"|",list1[2],"|")
    print(list1[3],"|",list1[4],"|",list1[5],"|")
    print(list1[6],"|",list1[7],"|",list1[8],"|")

    if list1[0] == list1[1] == list1[2]:
        if list1[0] == "x":
            print("Kartavya is a winner")
            break
        elif list1[0] == "o":
            print("Hirva is a winner")
            break
       
            
        

    elif list1[3] == list1[4] == list1[5]:
        if list1[3] == "x":
            print("shyam is a winner")
            break
        elif list1[3] == "o":
            print("Hirva is a winner")
            break
        
            
        

    elif list1[6] == list1[7] == list1[8]:
        if list1[6] == "x":
            print("shyam is a winner")
            break
        elif list1[6] == "o":
            print("Hirva is a winner")
            break
       
            
        

    elif list1[0] == list1[4] == list1[8]:
        if list1[0] == "x":
            print("shyam is a winner")
            break
        elif list1[0] == "o":
            print("Hirva is a winner")
            break
        
            
        

    elif list1[2] == list1[4] == list1[6]:
        if list1[2] == "x":
            print("shyam is a winner")
            break
        elif list1[2] == "o":
            print("Hirva is a winner")
            break
        
            
        

    elif list1[0] == list1[3] == list1[6]:
        if list1[0] == "x":
            print("shyam is a winner")
            break
        elif list1[0] == "o":
            print("Hirva is a winner")
            break
        
            
        

    elif list1[1] == list1[4] == list1[7]:
        if list1[1] == "x":
            print("shyam is a winner")
            break
        elif list1[1] == "o":
            print("Hirva is a winner")
            break
       
            
        

    elif list1[2] == list1[5] == list1[8]:
        if list1[2] == "x":
            print("shyam is a winner")
            break
        elif list1[2] == "o":
            print("Hirva is a winner")
            break
    if "_" not in list1:
        print("match tied")
        

    turn = turn + 1