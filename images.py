from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images & Icons")
root.iconbitmap("./python.ico")

my_img = ImageTk.PhotoImage(Image.open('./Images/zen.jpg'))
myLabel = Label(image=my_img)
myLabel.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()