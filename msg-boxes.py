from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")
root.iconbitmap("./python.ico")

def popup():
    response = messagebox.askyesno("This is my Popup", "Hello world!")
    if response == 1:
        Label(root, text="I thought you would have said no").pack()
    else:
        Label(root, text="I knew it was gonna be a no").pack()

Button(root, text='Popup', command=popup).pack()

root.mainloop()