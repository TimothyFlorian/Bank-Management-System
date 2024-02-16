from tkinter import *
import datetime
from subprocess import call

def create_user():
    call(["python", "create_user.py"])
def delete_user():
    call(["python", "delete_user.py"])
def pwd_admin():
    call(["python", "pwd_admin.py"])
def active_bankstaff():
    call(["python", "active_bankstaff.py"])
def active_customer():
    call(["python", "active_customer.py"])
def active_account():
    call(["python", "active_account.py"]) 

date = datetime.datetime.now().date()
date= str(date)

class application:
    def __init__(self,master):
        self.master=master

        #frames
        self.top=Frame(master,height=100,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=600,bg="pink")
        self.bottom.pack(fill=X)

        #frame labels
        self.image1=PhotoImage(file='icon\money.png')
        self.image1lbl=Label(self.top, image=self.image1, bg="white")
        self.image1lbl.place(x=70, y=15)

        self.image2=PhotoImage(file='icon\money.png')
        self.image2lbl=Label(self.top, image=self.image2, bg="white")
        self.image2lbl.place(x=480, y=15)

        self.heading=Label(self.top,text=" Golden Horizon Bank",font="arial 15 bold",bg="white")
        self.heading.place(x= 180, y=30)

        self.date_lbl=Label(self.bottom,text="Date : "+date,bg="pink")
        self.date_lbl.place(x=250, y=20)

        #Create User
        self.ca= Button(self.bottom, text=" Create User ", font="arial 13 bold", command=create_user, width=20)
        self.ca.place(x=40, y=50)
        self.ca_lbl = Label(self.bottom, text="--> Create new user ", bg="pink", font="arial 13 bold")
        self.ca_lbl.place(x=280, y=52)

        #Delete an User
        self.Be= Button(self.bottom, text=" Delete User ", font="arial 13 bold", command=delete_user, width=20)
        self.Be.place(x=40, y=120)
        self.be_lbl = Label(self.bottom, text="--> Delete user access", bg="pink", font="arial 13 bold")
        self.be_lbl.place(x=280, y=122)

        #Update password
        self.Caa= Button(self.bottom, text=" Update User password ", font="arial 13 bold", command=pwd_admin, width=20)
        self.Caa.place(x=40, y=190)
        self.caa_lbl = Label(self.bottom, text="--> Update User Access Password", bg="pink", font="arial 13 bold")
        self.caa_lbl.place(x=280, y=192)

        #Check all Active Management
        self.Bw= Button(self.bottom, text=" Active Management ", font="arial 13 bold", command=active_bankstaff, width=20)
        self.Bw.place(x=40, y=260)
        self.bw_lbl = Label(self.bottom, text="--> Check all active Management User", bg="pink", font="arial 13 bold")
        self.bw_lbl.place(x=280, y=262)

        #Check all Active Users
        self.Bd= Button(self.bottom, text=" Active User ", font="arial 13 bold", command=active_customer, width=20)
        self.Bd.place(x=40, y=330)
        self.bd_lbl = Label(self.bottom, text="--> Check all active Customer Access", bg="pink", font="arial 13 bold")
        self.bd_lbl.place(x=280, y=332)

        #Check all Active Accounts
        self.Au= Button(self.bottom, text=" Active Accounts ", font="arial 13 bold", command=active_account, width=20)
        self.Au.place(x=40, y=400)
        self.bd_lbl = Label(self.bottom, text="--> Check all active Accounts", bg="pink", font="arial 13 bold")
        self.bd_lbl.place(x=280, y=402)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("600x570+150+20")
root.resizable(height = 0, width = 0)
root.mainloop()