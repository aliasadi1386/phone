from tkinter import *
from tkinter import messagebox
import sqlite3


win  =  Tk()
win.geometry('220x300+400+0')
win.title(' add number')
win.config(bg='skyblue')
win.resizable(0,0)
win.iconbitmap('')

def search():
    con = sqlite3.connect('database1.db')
    c = con.cursor()
    name_to_search = name.get()
    c.execute('SELECT * FROM members WHERE name = ?', (name_to_search,))
    result = c.fetchone()
    if result:
        messagebox.showinfo('Member Found', f'Name: {result[0]}\nTelephone: {result[1]}')
    else:
        messagebox.showinfo('Member Not Found', f'Member "{name_to_search}" was not found')
        
name_label = Label(win, text='Name:', bg='skyblue', font=('Arial', 12))
name_label.place(x=10, y=20) 
   
name = Entry(win, bg='blue', justify='center', font=('Arial', 12))
name.place(x=10, y=50,width=200,height=50) 
        
btnsearch = Button(win, text='SEARCH', bg='blue', font=('Arial', 12), command=search)
btnsearch.place(x=10, y=130,width=200,height=50)

tel = Label(win, text='Telephone:', bg='skyblue', font=('Arial', 12))
tel.place(x=10, y=190)  

tel = Entry(win, bg='blue', justify='center', font=('Arial', 12))
tel.place(x=10, y=220,width=200,height=50)

win.mainloop()        