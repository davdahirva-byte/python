
import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # Agar password hai to yaha likho
    database="dbgls"
)

cur = con.cursor()

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
    

# Close connection
cur.close()
con.close()