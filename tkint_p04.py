from tkinter import *

def max():
    no=int(txtn.get())
    no2=int(txtn2.get())
    if no>no2:
        strans.set(str(no))
    else:
        strans.set(str(no2))    


root=Tk()
root.title("demo1")
root.geometry("300x400")

strans=StringVar(root)

lbln=Label(root,text="number1",font=("Arial",18))
lbln.grid(row=0,column=0)

txtn=Entry(root)
txtn.grid(row=0,column=1)

lbln2=Label(root,text="number2",font=("Arial",18))
lbln2.grid(row=1,column=0)

txtn2=Entry(root)
txtn2.grid(row=1,column=1)

btn=Button(root,text="max",command=max)
btn.grid(row=2,column=0)

lblans=Label(root,text="answer",font=("Arial",18))
lblans.grid(row=3,column=0)

txtn3=Entry(root,textvariable=strans)
txtn3.grid(row=3,column=1)

root.mainloop()