
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

Roll_no=int(input("Enter roll_no"))
Name=input("Enter the name")
English=int(input("Enter english marks"))
Maths=int(input("enter maths marks"))
Science=int(input("enter science marks"))
Total=int(input("enter total marks"))
Percentage=int(input("enter per"))
Grade=input("enter grade")

query = f"INSERT INTO student VALUES ({Roll_no}, '{Name}', {English}, {Maths}, {Science}, {Total}, {Percentage}, '{Grade}')"# Fetch data from Student table
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
    

# Close connection
cur.close()
con.close()