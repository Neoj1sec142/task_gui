import os
from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as msc

win = Tk()
win.geometry("800x470")
win.title("Task Management CRUD App")

tPrio = Label(win, text="Priority:", font=("Serif", 12))
tPrio.place(x=20, y=30)
tTit = Label(win, text="Title:", font=("Serif", 12))
tTit.place(x=20, y=60)
tLoc = Label(win, text="Location:", font=("Serif", 12))
tLoc.place(x=20, y=90)

entPrio = Entry(win)
entPrio.place(x=170, y=30)
entTit = Entry(win)
entTit.place(x=170, y=60)
entLoc = Entry(win)
entLoc.place(x=170, y=90)

def insert():
    p = entPrio.get()
    t = entTit.get()
    l = entLoc.get()
    if(p=="" or t=="" or l==""):
        mb.showwarning("Cannot Insert", "All Fields Required")
    else:
        db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute("INSERT INTO task.taskDetails")

showData = Listbox(win)
showData.place(x=330, y=30)
# show()
win.mainloop()
