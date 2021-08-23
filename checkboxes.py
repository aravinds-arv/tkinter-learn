from tkinter import *

root = Tk()
root.title("Checkboxes")
root.iconbitmap("./python.ico")

def updateVar1():
    myLabel = Label(root, text=var1.get()).pack()

def updateVar2():
    myLabel = Label(root, text=var2.get()).pack()


var1 = IntVar()
c1 = Checkbutton(root, text="Check this box", variable=var1, command=updateVar1)
c1.pack()

var2 = StringVar()
var2.set("Off")
c2 = Checkbutton(root, text="Uncheck me!", variable=var2, command=updateVar2, onvalue="On", offvalue="Off")
c2.pack()

Button(root, text="Update", command=updateVar2).pack()

root.mainloop()
