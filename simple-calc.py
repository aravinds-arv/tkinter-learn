from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

def myClick():
    myLabel = Label(root,text="Hello "+e.get())
    myLabel.pack()

button_1 = Button(root, text="1", padx=40, pady=20, command="button_add")

myButton = Button(root, text="Enter your name", command=myClick)

root.mainloop()