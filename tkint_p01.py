from tkinter import *

def no():
    no=int(txtno.get())
    strans.set(str(no))



root=Tk()
root.title("demo")
root.geometry("200x300")


strans=StringVar(root)

lblno=Label(root,text="Number",font=("arial",16))
lblno.grid(row=0,column=0)

txtno=Entry(root)
txtno.grid(row=0,column=1)

bnt = Button(root,text="click me",command=no)
bnt.grid(row=1,column=0)

lblans=Label(root,text="Answer",font=("Arial",16))
lblans.grid(row=2,column=0)

lblans2=Entry(root,textvariable=strans)
lblans2.grid(row=2,column=1)

root.mainloop()