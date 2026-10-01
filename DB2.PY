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

# Fetch data from Student table
cur.execute("SELECT * FROM Student")

# Print all records
data = cur.fetchall()

for row in data:
    no,name,eng,hindi,ss,total,per,grade=row
    print(no,name,eng,hindi,ss,total,per,grade)

# Close connection
cur.close()
con.close()