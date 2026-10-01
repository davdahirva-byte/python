
import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # Agar password hai to yaha likho
    database="dbgls"
)

cur = con.cursor()



while True:
    print("enter 1 for data")
    print("enter 2 for insert")
    print("enter 3 for update")
    print("enter 4 for delete")

    ch=int(input("enter a choice"))
    if ch==1:

        # Fetch data from Student table
        query = f"select * from student"
        cur.execute(query)

        # Print all records
        data = cur.fetchall()

        for row in data:
            print(row)
        break

    elif ch==2:
        
        Roll_no=int(input("Enter roll_no"))
        Name=input("Enter the name")
        English=int(input("Enter english marks"))
        Maths=int(input("enter maths marks"))
        Science=int(input("enter science marks"))
        Total=int(input("enter total marks"))
        Percentage=int(input("enter per"))
        Grade=input("enter grade")

        # Fetch data from Student table    
        query = f"INSERT INTO student VALUES ({Roll_no}, '{Name}', {English}, {Maths}, {Science}, {Total}, {Percentage}, '{Grade}')"
        cur.execute(query)

        #for insert
        con.commit() 
             
        # Print all records
        data = cur.fetchall()
        
        for row in data:
            # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
            # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
            print(row)
        break

    elif ch==3:
        
        Roll_no=int(input("Enter roll_no"))

        query = f"update student set name ='kp' WHERE Roll_no = {Roll_no}"# Fetch data from Student table
        cur.execute(query)
        con.commit() #for insert

        print("Record Inserted successfully")

        cur.execute("Select * from student")
        # Print all records
        data = cur.fetchall()

        for row in data:
            # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
            # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
            print(row)
        break

    elif ch==4:
            
        Roll_no=int(input("Enter roll_no"))

        query = f"DELETE FROM student WHERE Roll_no = {Roll_no}"# Fetch data from Student table
        cur.execute(query)
        con.commit() #for insert

        print("Record Inserted successfully")

        cur.execute("Select * from student")
# Print all records
        data = cur.fetchall()

        for row in data:
            # Roll_No,Name,English,Maths,Science,Total,Percentage,Grade = row
            # print(Roll_No,Name,English,Maths,Science,Total,Percentage,Grade)
            print(row)
        break


    else:
        print("invalid")      
    
    


# Close connection
cur.close()
con.close()