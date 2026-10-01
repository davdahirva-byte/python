from tkinter import *
import mysql.connector


def display():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbgls"
    )

    cur = con.cursor()

    roll_no = int(txt.get())
    query = f"update student set Grade = 'B' where Roll_No = {roll_no}"
    cur.execute(query)
    con.commit()
    

    cur.execute("SELECT * FROM Student")

    data = cur.fetchall()

    for row in data:
        listbox.insert(END, row)

    cur.close()
    con.close()


root = Tk()
root.title("Student Records")
root.geometry("600x400")

lbl = Label(root,text="Roll no",font=("Arial",16))
lbl.grid(row=0,column=0)

txt = Entry(root)
txt.grid(row=0,column=1)

btn = Button(root, text="Update Grade", command=display)
btn.grid(row=1, column=2, pady=10)

listbox = Listbox(root, width=100, height=15)
listbox.grid(row=2, column=0, pady=20)


root.mainloop()

