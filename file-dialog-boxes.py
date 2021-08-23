from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

main = Tk()
main.title("File dialog boxes")
main.iconbitmap("./python.ico")

def open():
    global myImg
    main.filename = filedialog.askopenfilename(initialdir="./Images", title="Select a file",filetypes=(("png files", "*.png"),("jpg files", "*.jpg"),("all files", "*.*")))
    myLabel = Label(main, text=main.filename)
    myLabel.pack()
    myImg = ImageTk.PhotoImage(Image.open(main.filename))
    myImage = Label(main, image=myImg)
    myImage.pack()

myButton = Button(main, text="Open file", command=open).pack()

main.mainloop()