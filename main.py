import os
from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as msc

win = Tk()
win.geometry("740x325")
win.title("Task Management CRUD App")

tId = Label(win, text="ID:", font=("Serif", 12))
tId.place(x=20, y=120) 
tPrio = Label(win, text="Priority:", font=("Serif", 12))
tPrio.place(x=20, y=30)
tTit = Label(win, text="Title:", font=("Serif", 12))
tTit.place(x=20, y=60)
tLoc = Label(win, text="Location:", font=("Serif", 12))
tLoc.place(x=20, y=90)

entId = Entry(win)
entId.place(x=170, y=120)
entPrio = Entry(win)
entPrio.place(x=170, y=30)
entTit = Entry(win)
entTit.place(x=170, y=60)
entLoc = Entry(win)
entLoc.place(x=170, y=90)

def insert():
    iD = entId.get()
    p = entPrio.get()
    t = entTit.get()
    l = entLoc.get()
    if(iD=="" or p=="" or t=="" or l==""):
        mb.showwarning("Cannot Insert", "All Fields Required")
    else:
        db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute("INSERT INTO task.taskDet (tId,tPrio,tTit,tLoc) VALUES (%s,%s,%s,%s)", (iD,p,t,l))
        db.commit()
        entId.delete(0, "end")
        entPrio.delete(0, "end")
        entTit.delete(0, "end")
        entLoc.delete(0, "end")
        show()
        mb.showinfo("Insert status", "Data Inserted Successfully")
        db.close()
inBtn = Button(win, text="Insert", font=("Sans", 12), bg="white", command=insert)
inBtn.place(x=45,y=160)

def update():
    iD = entId.get()
    p = entPrio.get()
    t = entTit.get()
    l = entLoc.get()
    if(p=="" or t=="" or l==""):
        mb.showwarning("Cannot Update", "All Fields Required")
    else:
        db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute("UPDATE taskDet set tPrio=%s,tLoc=%s,tTit=%s where tId=%s", (p,l,t, iD))
        db.commit()
        entId.delete(0, "end")
        entPrio.delete(0, "end")
        entTit.delete(0, "end")
        entLoc.delete(0, "end")
        show()
        mb.showinfo("Update Status:", "Data Updated Successfully")
        db.close()
upBtn = Button(win, text="Update", font=("Sans",12), bg="white", command=update)
upBtn.place(x=105,y=160)

def getTasks():
    if(entId.get()==""):
        mb.showwarning("Get Status", "Please enter the ID of the task you wish to get.")
    else:
        db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute("SELECT * FROM taskDet where tId="+entId.get()+"")
        rows = cur.fetchall()
        for row in rows:
            entPrio.insert(0, row[0])
            entTit.insert(0, row[1])
            entLoc.insert(0, row[2])
        db.close()
getBtn = Button(win, text="Get", font=("Sans", 12), bg="white", command=getTasks)
getBtn.place(x=175,y=160)

def delete():
    if(entId.get()==""):
        mb.showwarning("Please provide the ID of the task you wish to delete.")
    else:
        db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
        cur = db.cursor()
        cur.execute("DELETE FROM taskDet where tId="+entId.get()+"")
        db.commit()
        entId.delete(0, "end")
        entPrio.delete(0, "end")
        entTit.delete(0, "end")
        entLoc.delete(0, "end")
        show()
        mb.showinfo("Delete Status", "Data Deleted Successfully")
        db.close()
dltBtn = Button(win, text="Delete", font=("Sans", 12), bg="white", command=delete)
dltBtn.place(x=230,y=160)

def reset():
    entId.delete(0, "end")
    entPrio.delete(0, "end")
    entTit.delete(0, "end")
    entLoc.delete(0, "end")
rstBtn = Button(win, text="Reset", font=("Sans", 12), bg="white", command=reset)
rstBtn.place(x=20,y=210)

def show():
    db = msc.connect(host='localhost', user='root', passwd=os.environ.get('PASSWD'), database='task', auth_plugin='mysql_native_password')
    cur = db.cursor()
    cur.execute("SELECT * FROM taskDet")
    rows = cur.fetchall()
    showData.delete(0, showData.size())
    for row in rows:
        addData = str(row[0])+' '+str(row[1])+' '+row[2]+' '+row[3]
        showData.insert(showData.size()+1, addData)
    db.close()

showData = Listbox(win)
showData.place(x=450, y=85)
show()
win.mainloop()
