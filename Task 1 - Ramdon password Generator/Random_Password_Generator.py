from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of our password:")

def selection():
    if choice.get() == 1:
        labelchoice.config(text="POOR")
    elif choice.get() == 2:
        labelchoice.config(text="AVERAGE")
    elif choice.get() == 3:
        labelchoice.config(text="ADVANCED")

choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection)
R1.pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection)
R2.pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection)
R3.pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlength.pack()

def callback():
    lsum.config(text=passgen())

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

root.mainloop()
