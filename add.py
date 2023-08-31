from tkinter import *
from tkinter import messagebox
import sqlite3


win  =  Tk()
win.geometry('220x300+400+0')
win.title(' add number')
win.config(bg='skyblue')
win.resizable(0,0)
win.iconbitmap('')
# ===================================================================================================
# this is a test

def save():
    con = sqlite3.connect('database1.db')
    c = con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS members(name VARCHAR(50), tel INTEGER)')

    n = name.get()
    t = tel.get()
    lst = [n, t]
    c.execute('INSERT INTO members(name, tel) VALUES (?, ?)', lst)
    con.commit()
    messagebox.showinfo('Attention', 'The information was saved correctly')
    name.delete(0, 'end')
    tel.delete(0, 'end')
    name.focus() 
    
    
name_label = Label(win, text='Name:', bg='skyblue', font=('Arial', 12))
name_label.place(x=10, y=20) 
   
name = Entry(win, bg='blue', justify='center', font=('Arial', 12))
name.place(x=10, y=50,width=200,height=50)

tel = Label(win, text='Telephone:', bg='skyblue', font=('Arial', 12))
tel.place(x=10, y=100)  

tel = Entry(win, bg='blue', justify='center', font=('Arial', 12))
tel.place(x=10, y=130,width=200,height=50)

btnsave = Button(win, text='SAVE', bg='blue', font=('Arial', 12), command=save)
btnsave.place(x=10, y=200,width=200,height=50)


mainloop()