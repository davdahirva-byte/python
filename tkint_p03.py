from tkinter import *

def sum():
    no=int(txtn.get())
    no2=int(txtn2.get())
    strans.set(str(no+no2))


def sub():
    no=int(txtn.get())
    no2=int(txtn2.get())
    strans.set(str(no-no2)) 

def mul():
    no=int(txtn.get())
    no2=int(txtn2.get())
    strans.set(str(no*no2))

def div():
    no=int(txtn.get())
    no2=int(txtn2.get())
    strans.set(str(no/no2))           

root=Tk()
root.title("demo3")
root.geometry("400x400")

strans=StringVar(root)

lbln=Label(root,text="number",font=("Arial",18))
lbln.grid(row=0,column=0)

txtn=Entry(root)
txtn.grid(row=0,column=1)

lbln2=Label(root,text="number2",font=("Arial",18))
lbln2.grid(row=1,column=0)

txtn2=Entry(root)
txtn2.grid(row=1,column=1)

btn=Button(root,text="+",command=sum)
btn.grid(row=2,column=0)

btn=Button(root,text="-",command=sub)
btn.grid(row=2,column=1)

btn=Button(root,text="*",command=mul)
btn.grid(row=2,column=2)

btn=Button(root,text="/",command=div)
btn.grid(row=2,column=3)

lblans=Label(root,text="answer",font=("Arial",18))
lblans.grid(row=3,column=0)

txtn3=Entry(root,textvariable=strans)
txtn3.grid(row=3,column=1)

root.mainloop()