from tkinter import * 


def submit():
    result = ""

    if india.get() == 1:
        result += "India "

    if aus.get() == 1:
        result += "Australia "

    if canada.get() == 1:
        result += "Canada "

    strans.set(result)





root = Tk()
root.title("demo")
root.geometry("400x300")


india = IntVar()
aus = IntVar()
canada = IntVar()

strans = StringVar()

check = Checkbutton(root,text="india",font=("Arial",16),variable=india)
check.grid(row=0,column=0)

check2 = Checkbutton(root,text="aus",font=("Arial",16),variable=aus)
check2.grid(row=0,column=1)

check3 = Checkbutton(root,text="canada",font=("Arial",16),variable=canada)
check3.grid(row=0,column=3)

bnt = Button(root,text="submit",command=submit)
bnt.grid(row=1,column=0)

ans = Label(root,text="Answer",font=("Arial",16))
ans.grid(row=2,column=0)

txtno = Entry(root,textvariable=strans)
txtno.grid(row=2,column=1)

root.mainloop()