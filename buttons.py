from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text="Look! I clicked a button!")
    myLabel.pack()

myButton1 = Button(root, text="Click Me!",state=DISABLED)
myButton1.pack()
myButton2 = Button(root, text="Click Me!",padx=50,pady=50)
myButton2.pack()
myButton3 = Button(root, text="Click Me!",command=myClick)
myButton3.pack()
myButton4 = Button(root, text="Click Me!",fg="blue",bg="#ffee22")
myButton4.pack()

root.mainloop()