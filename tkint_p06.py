from tkinter import *

def sum():
    no = int(txtno.get())
    no2 = int(txtno2.get())
    strans.set(str(no+no2))

def sub():
    no = int(txtno.get())
    no2 = int(txtno2.get())
    strans.set(str(no-no2)) 


root = Tk()
root.title("demo")
root.geometry("400x300")

strans = StringVar(root)

lblno = Label(root,text="Number",font=("Arial",16))
lblno.grid(row=0,column=0)

txtno = Entry(root)
txtno.grid(row=0,column=1)

lblno2 = Label(root,text="Number2",font=("Arial",16))
lblno2.grid(row=1,column=0)

txtno2 = Entry(root)
txtno2.grid(row=1,column=1)

radno = Radiobutton(root,text="sum",font=("Arial",16),command=sum)
radno.grid(row=2,column=0)

radno2 = Radiobutton(root,text="sub",font=("Arial",16),command=sub)
radno2.grid(row=2,column=1)

checkno = Checkbutton(root,text="india",font=("Arial",16))
checkno.grid(row=3,column=0)

checkno = Checkbutton(root,text="aus",font=("Arial",16))
checkno.grid(row=3,column=1)

checkno = Checkbutton(root,text="china",font=("Arial",16))
checkno.grid(row=3,column=2)

bnt = Button(root,text="click me")
bnt.grid(row=4,column=0)

lblno3 = Label(root,text="Answer",font=("Arial",16))
lblno3.grid(row=5,column=0)

txtno3 = Entry(root,textvariable=strans)
txtno3.grid(row=5,column=1)



root.mainloop()