from tkinter import *
from tkinter import messagebox
import sqlite3


win  =  Tk()
win.geometry('220x100+400+0')
win.title(' add number')
win.config(bg='skyblue')
win.resizable(0,0)
win.iconbitmap('')

def show_all_members():
    con = sqlite3.connect('database1.db')
    c = con.cursor()
    c.execute('SELECT * FROM members')
    members = c.fetchall()
    if members:
        member_list = '\n'.join([f'Name: {member[0]}\nTelephone: {member[1]}\n' for member in members])
        messagebox.showinfo('All Members', member_list)
    else:
        messagebox.showinfo('No Members', 'There are no members in the database')
        
        
btnshowall = Button(win, text='SHOW ALL MEMBERS', bg='blue', font=('Arial', 12), command=show_all_members)
btnshowall.place(x=10, y=20,width=200,height=50)        


win.mainloop()