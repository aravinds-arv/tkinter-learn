from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images & Icons")
root.iconbitmap("./python.ico")


# accessing all the images in the directory
my_img1 = ImageTk.PhotoImage(Image.open('./Images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('./Images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('./Images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('./Images/4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('./Images/5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('./Images/6.jpg'))

# adding all images to a list for easier access
imgList = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6 ]

# image container widget
num = 0
myLabel = Label(image=imgList[num])
myLabel.grid(row=0,column=0,columnspan=3)

# defining fuctions used
def prev():
    global num
    global myLabel
    if num > 0:
        num -= 1
    else:
        num = 5
    myLabel.grid_forget()
    myLabel = Label(image=imgList[num])
    myLabel.grid(row=0,column=0,columnspan=3)



def nxt():
    global num
    global myLabel
    if num < 5:
        num += 1
    else:
        num = 0
    myLabel.grid_forget()
    myLabel = Label(image=imgList[num])
    myLabel.grid(row=0,column=0,columnspan=3)

# defining the buttons
buttonPrev = Button(root, text="<<", command=prev, padx=80, pady=5)
buttonNext = Button(root, text=">>", command=nxt, padx=80, pady=5)
buttonClose = Button(root, text="Exit", command=root.quit, padx=75, pady=5)

# positioning  the buttons
buttonPrev.grid(row=1,column=0)
buttonClose.grid(row=1,column=1)
buttonNext.grid(row=1,column=2)


root.mainloop()