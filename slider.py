from tkinter import *

root = Tk()
root.title("Sliders")
root.iconbitmap("./python.ico")

def updateSlide(value):
    myLabel = Label(root, text=sliderH.get()).pack()

sliderV = Scale(root, from_=0, to=200)
sliderV.pack(anchor=E)

sliderH = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=updateSlide)
sliderH.pack()

root.mainloop()