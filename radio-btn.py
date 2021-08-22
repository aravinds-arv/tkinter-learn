from tkinter import *

root = Tk()
root.title("Radio buttons")
root.iconbitmap("./python.ico")

def updatePizza(pizza):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text=pizza.get())
    myLabel.pack()

toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for (topping, value) in toppings:
    Radiobutton(root, text=topping, variable=pizza, value=topping, command= lambda: updatePizza(pizza)).pack(anchor=W)

# r = IntVar()
# r.set(2)
# Radiobutton(root, text="Option 1", variable=r, value=1, command=updateR).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=updateR).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

root.mainloop()