import os 
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
os.system('cls')

win = Tk()
win.geometry('730x2000+400+0')
win.title(' phone book')
win.resizable(0,0)
win.iconbitmap('')
# ===========================================================
def add():
    os.system('py add.py')
# login
img_login = PhotoImage(file = 'phone.png')
lbl_login = Label(image = img_login , cursor='hand2')
lbl_login.place(x = 0 , y = 0 )
#============================================================
#exit
def exit():
    msg =messagebox.askyesno('Attention','Are you sure ? ')
    if msg:
        win.destroy()
#============================================================
#btn
btnadd = Button(text='ADD NUMBER:' , bg='skyblue',font=('tahoma',25) , command = add)
btnadd.place(x=220,y=80,width=330,height=80) 

btnserch = Button(text='SEARCH NUMBER:' , bg='skyblue',font=('tahoma',25))
btnserch.place(x=220,y=170,width=330,height=80)  

btndelete = Button(text='DELETE NUMBER:' , bg='skyblue',font=('tahoma',25))
btndelete.place(x=220,y=260,width=330,height=80) 
 
btnall = Button(text='SHOW ALL NUMBER:' , bg='skyblue',font=('tahoma',25))
btnall.place(x=220,y=350,width=330,height=80) 
 
btnexit = Button(text = 'EXIT',bg='blue',font=('tahoma',25),command=exit)
btnexit.place(x=220,y=650,width=330,height=80)



 
mainloop()