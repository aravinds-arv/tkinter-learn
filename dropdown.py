from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown")
root.iconbitmap("./python.ico")
root.geometry("400x400")

def update(var):
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

days = [
     "Monday", 
     "Tueday", 
     "Wednesday", 
     "Thursday", 
     "Friday",
     "Saturday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *days, command=update)
drop.pack()

myLabel = Label(root, text=clicked.get())
myLabel.pack()

root.mainloop()