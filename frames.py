from tkinter import *

root = Tk()
root.title("Frames in Tkinter")
root.iconbitmap("./python.ico")

frame1 = LabelFrame(root, text="This is my Frame...", padx=50, pady=25)
frame1.pack(pady=100,padx=100)

b1 = Button(frame1, text="Don't click here!!")
b2 = Button(frame1, text="You can click here :)")
b1.grid(row=0,column=0,padx=5)
b2.grid(row=0,column=1)

root.mainloop()