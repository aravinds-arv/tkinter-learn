from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("New windows")
root.iconbitmap("./python.ico")

def window2():
    global myImg
    top = Toplevel()
    top.title("NEW WINDOW")
    top.iconbitmap("./python.ico")
    myImg = ImageTk.PhotoImage(Image.open("./Images/3.jpg"))
    Label(top, image=myImg).pack()
    btn2 = Button(top, text="Close window", command=top.destroy)
    btn2.pack()

btn1 = Button(root, text="Open window", command=window2)
btn1.pack()

root.mainloop()