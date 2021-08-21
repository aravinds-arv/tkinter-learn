from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=45,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=15)

def button_click(number):
    e.insert(END, number)

def button_bcksp():
    l = len(e.get())
    e.delete(l-1,END)

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global sign
    sign = "+"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global sign
    sign = "-"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global sign
    sign = "*"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global sign
    sign = "/"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    global s_num 
    s_num = int(second_number)
    e.delete(0, END)
    global f_num
    global sign
    if sign == "+":
        e.insert(0, (s_num + f_num))
    elif sign == "-":
        e.insert(0, (s_num - f_num))
    elif sign == "*":
        e.insert(0, (s_num * f_num))
    elif sign == "/":
        e.insert(0, (f_num / s_num))



# defining buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", command=button_add, padx=40, pady=20)
button_subtract = Button(root, text="-", command=button_subtract, padx=40, pady=20)
button_multiply = Button(root, text="*", command=button_multiply, padx=40, pady=20)
button_divide = Button(root, text="/", command=button_divide, padx=40, pady=20)
button_equal = Button(root, text="=", command=button_equal, padx=87, pady=20)
button_bcksp = Button(root, text="BCKSP", command=button_bcksp, padx=25, pady=20)
button_clear = Button(root, text="C", command=button_clear, padx=40, pady=20)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_bcksp.grid(row=5, column=0)
button_clear.grid(row=6, column=0)
button_equal.grid(row=6, column=1,columnspan=2)


root.mainloop()