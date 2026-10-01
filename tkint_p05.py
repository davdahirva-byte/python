from tkinter import *
def sum():
    no = int(txtn.get())
    no2 = int(txtn2.get())
    strans.set(str(no + no2))

def sub():
    no = int(txtn.get())
    no2 = int(txtn2.get())
    strans.set(str(no - no2))

def mul():
    no = int(txtn.get())
    no2 = int(txtn2.get())
    strans.set(str(no * no2))

def div():
    no = int(txtn.get())
    no2 = int(txtn2.get())
    strans.set(str(no / no2))


root = Tk()
root.title("demo")
root.geometry("400x300")

strans = StringVar(root)
choice = StringVar()

lblno = Label(root, text="Number 1", font=("Arial",16))
lblno.grid(row=0, column=0)

txtn = Entry(root)
txtn.grid(row=0, column=1)

lblno2 = Label(root, text="Number 2", font=("Arial",16))
lblno2.grid(row=1, column=0)

txtn2 = Entry(root)
txtn2.grid(row=1, column=1)

radno = Radiobutton(root, text="sum", variable=choice, value="sum", font=("Arial",16), command=sum)
radno.grid(row=2, column=0)

radno = Radiobutton(root, text="sub", variable=choice, value="sub", font=("Arial",16), command=sub)
radno.grid(row=2, column=1)

radno = Radiobutton(root, text="mul", variable=choice, value="mul", font=("Arial",16), command=mul)
radno.grid(row=2, column=2)

radno = Radiobutton(root, text="div", variable=choice, value="div", font=("Arial",16), command=div)
radno.grid(row=2, column=3)

lblans = Label(root, text="Answer", font=("Arial",16))
lblans.grid(row=3, column=0)

txtans = Entry(root, textvariable=strans)
txtans.grid(row=3, column=1)

root.mainloop()