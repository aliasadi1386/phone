from tkinter import *
from tkinter import messagebox
import sqlite3


win  =  Tk()
win.geometry('220x230+400+0')
win.title(' add number')
win.config(bg='skyblue')
win.resizable(0,0)
win.iconbitmap('')

def delete():
    con = sqlite3.connect('database1.db')
    c = con.cursor()
    name_to_delete = name.get()
    c.execute('DELETE FROM members WHERE name = ?', (name_to_delete,))
    con.commit()
    messagebox.showinfo('Attention', f'Member "{name_to_delete}" was deleted successfully')
    name.delete(0, 'end')
    tel.delete(0, 'end')
    name.focus()
    
name_label = Label(win, text='Name:', bg='skyblue', font=('Arial', 12))
name_label.place(x=10, y=20) 

name = Entry(win, bg='blue', justify='center', font=('Arial', 12))
name.place(x=10, y=50,width=200,height=50) 


btndelete = Button(win, text='DELETE', bg='blue',  font=('Arial', 12), command=delete)
btndelete.place(x=10, y=135,width=200,height=50)   

win.mainloop() 