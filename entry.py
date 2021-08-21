from tkinter import *

root = Tk()

e = Entry(root, width=50,borderwidth=5)
e.insert(0, "Enter your name: ")
e.pack()

def myClick():
    myLabel = Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()