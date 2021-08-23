from tkinter import *
import sqlite3

root = Tk()
root.title("Working with databases")
root.iconbitmap("./python.ico")

# creating/connecting a database
conn = sqlite3.connect("phone_book.db")

# creating the cursor
c = conn.cursor()

# creating table
c.execute(""" CREATE TABLE phonebook (
    firstName text,
    lastName text,
    phoneNum integer,
    email text
    )""")

# commit changes
conn.commit()

# closing connection
conn.close()

root.mainloop()