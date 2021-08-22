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

# creating a status bar
statNum = 1            # the index number of photo
imgNum = len(imgList)  # the number of photos in the list/directory
status = Label(root, text=f"Image {statNum} of {imgNum}", bd=1, relief=SUNKEN, anchor=E)

# defining fuctions used
def prev():
    global num
    global myLabel
    global buttonPrev
    global buttonNext
    global statNum
    global status
    if num > 1:
        myLabel.grid_forget()
        num -= 1
        statNum -= 1
        myLabel = Label(image=imgList[num])
        myLabel.grid(row=0,column=0,columnspan=3)
        buttonPrev = Button(root, text="<<", command=prev, padx=80, pady=5)
        buttonPrev.grid(row=1,column=0)
        buttonNext = Button(root, text=">>", command=nxt, padx=80, pady=5)
        buttonNext.grid(row=1,column=2)
        status = Label(root, text=f"Image {statNum} of {imgNum}", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    else:
        myLabel.grid_forget()
        num -= 1
        statNum -= 1
        myLabel = Label(image=imgList[num])
        myLabel.grid(row=0,column=0,columnspan=3)
        buttonPrev = Button(root, text="<<", padx=80, pady=5, state=DISABLED)
        buttonPrev.grid(row=1,column=0)
        status = Label(root, text=f"Image {statNum} of {imgNum}", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2,column=0,columnspan=3, sticky=W+E)


def nxt():
    global num
    global myLabel
    global buttonPrev
    global buttonNext
    global statNum
    global status
    if num < 4:
        myLabel.grid_forget()
        num += 1
        statNum += 1
        myLabel = Label(image=imgList[num])
        myLabel.grid(row=0,column=0,columnspan=3)
        buttonNext = Button(root, text=">>", command=nxt, padx=80, pady=5)
        buttonNext.grid(row=1,column=2)
        buttonPrev = Button(root, text="<<", command=prev, padx=80, pady=5)
        buttonPrev.grid(row=1,column=0)
        status = Label(root, text=f"Image {statNum} of {imgNum}", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2,column=0,columnspan=3, sticky=W+E)
    else:
        myLabel.grid_forget()
        num += 1
        statNum += 1
        myLabel = Label(image=imgList[num])
        myLabel.grid(row=0,column=0,columnspan=3)
        buttonNext = Button(root, text=">>", padx=80, pady=5, state=DISABLED)
        buttonNext.grid(row=1,column=2)
        status = Label(root, text=f"Image {statNum} of {imgNum}", bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2,column=0,columnspan=3, sticky=W+E)



# defining the buttons
buttonPrev = Button(root, text="<<", command=prev, padx=80, pady=5, state=DISABLED)
buttonNext = Button(root, text=">>", command=nxt, padx=80, pady=5)
buttonClose = Button(root, text="Exit", command=root.quit, padx=75, pady=5)

# positioning  the buttons
buttonPrev.grid(row=1,column=0)
buttonClose.grid(row=1,column=1, pady=10)
buttonNext.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)


root.mainloop()