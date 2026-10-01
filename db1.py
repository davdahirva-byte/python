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

    cur.execute("SELECT * FROM Student")

    data = cur.fetchall()

    for row in data:
        listbox.insert(END, row)

    cur.close()
    con.close()


root = Tk()
root.title("Student Records")
root.geometry("600x400")


btn = Button(root, text="Display Records", command=display)
btn.pack(pady=20)


listbox = Listbox(root, width=80, height=15)
listbox.pack()


root.mainloop()

