import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # Agar password hai to yaha likho
    database="dbgls"
)

# Cursor create
cur = con.cursor()




print("enter 1 for Teacher login")
print("enter 2 for Admin login")


ch = int(input("enter a choice = "))

username = input("enter username = ")
password = input("enter password = ")

if ch == 1:
    
        query = "select * from Teacher where Username=%s and Password=%s"
        cur.execute(query,(username,password))
        data = cur.fetchall()

        if data:
             
            print("Login successfully")

            print("enter u for update")
            print("enter d for delete")
    
            c = input("enter your choice = ")
    
            if c == 'u':
                Roll_no = int(input("enter a roll no = "))
                query = f"Update Mystudent set name = 'hirva' where Roll_No = {Roll_no}"
                # Fetch data from Student table
                cur.execute(query)
                con.commit()
    
            
                cur.execute("SELECT * FROM Mystudent")
                # Print all records
                data = cur.fetchall()
    
    
                for row in data:
                    # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
                    # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
                    # Name = row
                    print(row)
                
    
            if c == 'd':
                Roll_no = int(input("enter a roll no = "))
                query = f"delete from MyStudent where Roll_No = {Roll_no}"
                # Fetch data from Student table
                cur.execute(query)
                con.commit()
    
                # print("Record Inserted Successfully")
    
                # Display all records
                cur.execute("SELECT * FROM MyStudent")
                # Print all records
                data = cur.fetchall()
    
    
                for row in data:
                    # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
                    # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
                    # Name = row
                    print(row)
        else:
            print("Invalid Username or Password")      
        
    


elif ch == 2:
    
    
        query = "select * from Myadmin where Username=%s and Password=%s"
        cur.execute(query,(username,password))
        data = cur.fetchall()


        if data:
                 
            print("Login successfully")
            query = f"Select * from MyStudent"
            # Fetch data from Student table
            cur.execute(query)
            # con.commit()
    
     
            data = cur.fetchall()
    
    
            for row in data:
                # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
                # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
                # Name = row
                print(row)        
        else:
            print("Invalid Username or Password")
else:
    print("Invalid Choice")
    

# Close connection  
cur.close()
con.close()